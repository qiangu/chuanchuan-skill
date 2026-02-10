#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TemplateFile:
    filename: str
    content: str


def _write_file(path: Path, content: str, *, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"File exists: {path} (use --force to overwrite)")
    path.write_text(content, encoding="utf-8")


def _mkdir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def build_templates(project_name: str) -> list[TemplateFile]:
    safe_name = project_name.strip() or "未命名项目"

    readme = f"""# {safe_name}（项目文档包）

用法建议：
1) 先填 `01-任务书.md`（一页对齐与授权）
2) 再填 `02-相关方.md`、`03-RACI.md`
3) 再做 `04-WBS.md` → `05-里程碑计划.md` → `06-风险登记册.md`
4) 执行期每周更新 `07-状态报告.md`，有变更走 `08-变更申请.md`
5) 收尾时补齐 `09-收尾报告.md`、`10-经验教训.md`、`11-归档清单.md`
"""

    charter = f"""# 一页项目任务书（章程/任务书）— {safe_name}

## 背景/商业价值（为什么做）

## 可测量目标 & 成功标准（怎么才算成功）
- 目标：
- 成功标准（量化/可验收）：

## 总体要求（约束）
- 进度约束：
- 成本/预算上限：
- 质量/合规：

## 范围（交付什么 / 不交付什么）
- In scope：
- Out of scope：

## 关键里程碑（总体）
| 里程碑 | 目标日期 | 验收口径 | Owner |
|---|---|---|---|
|  |  |  |  |

## 总体预算（按阶段/里程碑即可）

## 主要风险（Top 5）
| 风险事件 | 概率 | 影响 | 应对策略 | Owner |
|---|---|---|---|---|
|  |  |  |  |  |

## 审批要求（怎么批准/谁拍板）
- 决策人/审批人：
- 审批机制（会议/书面/时限）：

## 项目经理（职责与权限）
- PM：
- 权限边界：
- 升级机制：
"""

    stakeholders = """# 相关方登记册 + 权力-利益方格

## 登记册
| 姓名 | 单位/角色 | 期望/诉求 | 态度 | 权力(1-10) | 利益(1-10) | 象限 | 管理策略 | 沟通节奏 |
|---|---|---|---|---:|---:|---|---|---|
|  |  |  | 支持/中立/反对 |  |  |  |  |  |

## 象限策略速查
- 高权力高利益：持续管理，争取成为支持者
- 高权力低利益：谨慎管理，避免成为反对者
- 低权力低利益：少投入，监控即可
- 低权力高利益：多倾听，提供信息与反馈通道
"""

    raci = """# RAM / RACI（责任分配矩阵）

规则：
- 每项工作只能有一个 R
- A（批准/负责最终结果）尽量明确到 1 人

| WBS/工作包 | 负责人R | 批准A | 咨询C | 知悉I | 备注 |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
"""

    wbs = """# WBS + WBS词典（面向可交付成果）

## WBS（树形/缩进均可）
- 1.0 交付物A
  - 1.1 子交付物A1
    - 1.1.1 工作包A1-1

## WBS词典（建议对每个工作包填）
| WBS编码 | 名称 | 交付内容 | 验收标准 | 不包含 | Owner | 依赖 | 估算(工时/成本) |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
"""

    schedule = """# 里程碑计划（简版进度）

| 里程碑 | 交付物 | 目标日期 | 依赖 | 风险点 | Owner |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

备注：
- 若要压缩周期，优先看关键路径；非关键工作压了也不改变总工期。
"""

    risk = """# 风险登记册（概率×影响）

| 风险事件 | 触发器/信号 | 概率(低/中/高) | 影响(低/中/高) | 优先级 | 应对策略 | 预案/缓冲 | Owner |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
"""

    status = """# 状态报告（周报/双周报）

**周期**：YYYY-MM-DD ~ YYYY-MM-DD

## 一页结论（红黄绿 + 结论）

## 本期完成
- 

## 下期计划
- 

## 偏差与原因（范围/进度/成本/质量）
- 

## 风险与问题（Top 5）
- 

## 变更汇总（本期批准/待决）
- 

## 需要决策/升级事项
- 
"""

    change = """# 变更申请（九步法配套）

## 变更标题

## 变更描述（是什么/为什么）

## 影响分析（十掌全覆盖）
- 范围：
- 进度：
- 成本：
- 质量：
- 资源/采购：
- 沟通/相关方：
- 风险：
- 整合（权衡结论）：

## 解决方案（至少 3 个：上/中/下策）
1) 上策：
2) 中策：
3) 下策：

## 建议决策

## 审批
- 审批人：
- 决策：批准/否决
- 决策日期：

## 执行与跟踪
- Owner：
- 计划完成日：
- 验证方式：
"""

    closing = """# 收尾报告（五部分）

1) 原计划概况：范围/进度/成本/质量  
2) 偏差说明：与原计划的差异与原因  
3) 客户关系：关键互动、满意度、遗留沟通事项  
4) 风险总结：主要威胁/机会、应对与结果  
5) 经验教训：经过+措施+受益者（务必可落实/可度量）  
"""

    lessons = """# 经验教训（可复用写法）

| 场景/背景 | 发生了什么 | 根因 | 做得好的 | 做得不好的 | 具体改进动作（可执行/可检查） | 适用范围 | 受益者 | 存放位置/标签 |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
"""

    archive = """# 归档清单（最小版）

- 任务书/章程（含变更后版本）
- 范围基准：WBS + 词典 + 验收标准
- 进度基准：里程碑/关键路径/甘特（如有）
- 风险登记册 + 问题清单
- 状态报告（全周期）
- 变更申请与审批记录
- 验收记录/签收
- 收尾报告
- 经验教训（可复用条目）
"""

    return [
        TemplateFile("00-README.md", readme),
        TemplateFile("01-任务书.md", charter),
        TemplateFile("02-相关方.md", stakeholders),
        TemplateFile("03-RACI.md", raci),
        TemplateFile("04-WBS.md", wbs),
        TemplateFile("05-里程碑计划.md", schedule),
        TemplateFile("06-风险登记册.md", risk),
        TemplateFile("07-状态报告.md", status),
        TemplateFile("08-变更申请.md", change),
        TemplateFile("09-收尾报告.md", closing),
        TemplateFile("10-经验教训.md", lessons),
        TemplateFile("11-归档清单.md", archive),
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize a minimal project documentation pack (Markdown templates)."
    )
    parser.add_argument("--dir", required=True, help="Output directory for the project pack.")
    parser.add_argument("--name", required=True, help="Project name (used in headings).")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files if they already exist.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    out_dir = Path(args.dir).expanduser().resolve()
    _mkdir(out_dir)

    templates = build_templates(args.name)
    for tf in templates:
        _write_file(out_dir / tf.filename, tf.content, force=args.force)

    print(f"Initialized {len(templates)} files in: {out_dir}")


if __name__ == "__main__":
    # Avoid locale issues on some shells.
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    main()
