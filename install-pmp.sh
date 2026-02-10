#!/bin/bash
# 极简项目管理 Skill 一键安装脚本
# 用法: curl -fsSL https://raw.githubusercontent.com/qiangu/chuanchuan-skill/main/install-pmp.sh | bash

set -e

SKILL_NAME="pmp-jijian-project-management"
REPO_URL="https://github.com/qiangu/chuanchuan-skill.git"
TEMP_DIR="/tmp/chuanchuan-skill-$$"

# 检测 OpenClaw/Codex 安装路径
if [ -n "$OPENCLAW_HOME" ]; then
    SKILLS_DIR="$OPENCLAW_HOME/skills"
elif [ -n "$CODEX_HOME" ]; then
    SKILLS_DIR="$CODEX_HOME/skills"
elif [ -d "$HOME/.openclaw" ]; then
    SKILLS_DIR="$HOME/.openclaw/skills"
elif [ -d "$HOME/.codex" ]; then
    SKILLS_DIR="$HOME/.codex/skills"
else
    # 默认创建 OpenClaw 路径
    SKILLS_DIR="$HOME/.openclaw/skills"
    mkdir -p "$SKILLS_DIR"
fi

echo "🎯 安装极简项目管理 Skill"
echo "📁 目标目录: $SKILLS_DIR/$SKILL_NAME"
echo ""

# 克隆仓库
echo "⬇️  下载中..."
git clone --depth 1 "$REPO_URL" "$TEMP_DIR" 2>/dev/null || {
    echo "❌ Git 克隆失败，尝试使用 ZIP 下载..."
    curl -fsSL "https://github.com/qiangu/chuanchuan-skill/archive/refs/heads/main.zip" -o "$TEMP_DIR.zip"
    unzip -q "$TEMP_DIR.zip" -d /tmp/
    mv "/tmp/chuanchuan-skill-main" "$TEMP_DIR"
}

# 安装 skill
echo "📦 安装中..."
mkdir -p "$SKILLS_DIR"
rsync -a --delete "$TEMP_DIR/skills/$SKILL_NAME/" "$SKILLS_DIR/$SKILL_NAME/"

# 清理
rm -rf "$TEMP_DIR" "$TEMP_DIR.zip" 2>/dev/null || true

echo ""
echo "✅ 安装完成！"
echo ""
echo "📚 Skill 内容:"
echo "  - SKILL.md (主技能文件)"
echo "  - references/methodology.md (方法论)"
echo "  - references/templates.md (文档模板)"
echo "  - references/checklists.md (清单和反模式)"
echo "  - scripts/init_project_pack.py (一键生成脚本)"
echo ""
echo "🚀 使用方法:"
echo "  在对话中提及: '用极简项目管理 skill 帮我做项目规划'"
echo "  或直接调用: \$pmp-jijian-project-management"
echo ""
echo "📖 查看文档: $SKILLS_DIR/$SKILL_NAME/SKILL.md"
