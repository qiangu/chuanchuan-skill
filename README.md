# chuanchuan-skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个简洁的 AI Skill 集合，方便下载和使用。

---

## 包含的 Skills

| Skill | 说明 | 安装 |
|-------|------|------|
| `pmp-jijian-project-management` | 极简项目管理：一页任务书、RACI、WBS、里程碑、风险、状态报告 | [一键安装](#安装) |

---

## 安装

### 方式 1：一键安装（推荐）

```bash
curl -fsSL https://raw.githubusercontent.com/qiangu/chuanchuan-skill/main/install-pmp.sh | bash
```

### 方式 2：手动安装

```bash
# 1. 下载
git clone https://github.com/qiangu/chuanchuan-skill.git

# 2. 安装 skill
mkdir -p ~/.openclaw/skills
cp -r chuanchuan-skill/skills/pmp-jijian-project-management ~/.openclaw/skills/

# 3. 完成
```

---

## 使用

安装后，在 AI 对话中直接调用：

> "用极简项目管理 skill 帮我做项目规划"

或

> `$pmp-jijian-project-management 输出一页任务书、WBS、里程碑`

---

## 贡献

欢迎提交新的 skill！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 协议

[MIT](LICENSE) © 2026 chuanchuan-skill
