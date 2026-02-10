# chuanchuan-skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

个人技能仓库（Codex Skills），开源共享给社区使用。

当前包含 1 个 skill：

- `pmp-jijian-project-management`：将《极简项目管理》的核心框架（五大过程组 + "如来十掌"）沉淀为可直接复用的项目交付物与模板（任务书/相关方/三落实+RACI/WBS/里程碑/风险/状态报告/变更九步法/收尾与经验教训）。

---

## 🚀 一键安装（推荐）

最简单的方式，复制粘贴执行即可：

```bash
curl -fsSL https://raw.githubusercontent.com/qiangu/chuanchuan-skill/main/install-pmp.sh | bash
```

或下载 ZIP 手动安装：

```bash
# 下载并解压
curl -fsSL https://github.com/qiangu/chuanchuan-skill/archive/refs/heads/main.zip -o chuanchuan-skill.zip
unzip -q chuanchuan-skill.zip

# 安装 skill
mkdir -p ~/.openclaw/skills
rsync -a --delete \
  chuanchuan-skill-main/skills/pmp-jijian-project-management/ \
  ~/.openclaw/skills/pmp-jijian-project-management/

# 清理
cd chuanchuan-skill-main && rm -rf ../chuanchuan-skill.zip
```

---

## 安装（其他方式）

> 说明：Codex 通常从 `$CODEX_HOME/skills/` 读取 skills。若你没有设置 `$CODEX_HOME`，一般默认在 `~/.codex/` 或 `~/.openclaw/`。

### 方式 A：用 Codex 自带的 Skill Installer（最省事）

如果你的环境里有系统 skill `skill-installer`，可以直接从 GitHub 安装指定路径：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo qiangu/chuanchuan-skill \
  --path skills/pmp-jijian-project-management
```

安装后重启 Codex 以加载新 skills。

### 方式 B：git clone + rsync（通用）

1) 克隆仓库（私有仓库建议用 SSH；或下载 ZIP 解压）：

```bash
git clone git@github.com:qiangu/chuanchuan-skill.git ~/chuanchuan-skill
```

2) 拷贝/同步到 Codex skills 目录：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
rsync -a --delete \
  ~/chuanchuan-skill/skills/pmp-jijian-project-management/ \
  "${CODEX_HOME:-$HOME/.codex}/skills/pmp-jijian-project-management/"
```

## 调用（怎么用）

在 Codex 里直接提需求，并显式点名 skill（触发最稳定）：

- `用 $pmp-jijian-project-management 帮我把这个项目输出：一页任务书、相关方登记册、RACI、WBS、里程碑、风险登记册、状态报告节奏、变更流程。`

如果需要把模板落到文件上，可让它运行脚本：

- `python3 .../init_project_pack.py --dir ./my-project --name "项目名"`

## 更新（持续迭代）

1) 在本仓库拉取更新：

```bash
cd ~/chuanchuan-skill
git pull
```

2) 重新同步到 Codex skills 目录（同"安装"第 2 步）。

## 发布到 GitHub（首次）

由于不同账号/组织、公开性（public/private）选择不同，推荐你先在 GitHub 网页创建一个空仓库（不要勾选初始化 README / .gitignore / License），仓库名建议：`chuanchuan-skill`。

创建后，在本地执行：

```bash
cd ~/chuanchuan-skill
git remote add origin git@github.com:<YOUR_GITHUB_USERNAME_OR_ORG>/chuanchuan-skill.git
git push -u origin main
```

## 仓库结构

```text
.
├── LICENSE                       # MIT 开源许可证
├── CONTRIBUTING.md               # 贡献指南
├── install-pmp.sh               # 一键安装脚本
└── skills/
    └── pmp-jijian-project-management/
        ├── SKILL.md
        ├── agents/openai.yaml
        ├── references/*.md
        └── scripts/init_project_pack.py
```

---

## 开源协议

本项目采用 [MIT 许可证](LICENSE) 开源。

你可以自由使用、修改、分发本项目的代码，包括商业用途。

## 贡献

欢迎贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与。

## Star History

如果这个项目对你有帮助，请给我们一个 ⭐️ Star！
