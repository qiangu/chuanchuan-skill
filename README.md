# chuanchuan-skill

个人技能仓库（Codex Skills）。当前包含 1 个 skill：

- `pmp-jijian-project-management`：将《极简项目管理》的核心框架（五大过程组 + “如来十掌”）沉淀为可直接复用的项目交付物与模板（任务书/相关方/三落实+RACI/WBS/里程碑/风险/状态报告/变更九步法/收尾与经验教训）。

## 安装（推荐）

> 说明：Codex 通常从 `$CODEX_HOME/skills/` 读取 skills。若你没有设置 `$CODEX_HOME`，一般默认在 `~/.codex/`。

1) 克隆仓库（或下载 ZIP 解压）：

```bash
git clone <YOUR_REPO_URL> ~/chuanchuan-skill
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

2) 重新同步到 Codex skills 目录（同“安装”第 2 步）。

## 仓库结构

```text
.
└── skills/
    └── pmp-jijian-project-management/
        ├── SKILL.md
        ├── agents/openai.yaml
        ├── references/*.md
        └── scripts/init_project_pack.py
```

