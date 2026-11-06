# Delphi Plus

**Add clarity to expert consensus.**

一个面向德尔菲专家函询研究的写作与润色 skill，采用 Agent Skills 标准格式，适配 **Codex、Google Antigravity 和 Claude Code**。*Plus* 体现写作之外的配套支持：方法核查、问卷模板、统计口径与报告检查。让文字更清晰，同时保留异议与依据。

中文场景也支持“德尔菲涵询、专家咨询”等常见写法。默认按用户语言工作，适用于中文及英文学术表达。

## 可以完成什么

- 起草或审查研究方案、开题与方法设计。
- 制作致专家信、首轮问卷、后续轮次反馈及条目修订台账。
- 撰写和核查论文方法、结果、统计表与报告完整性。
- 润色中英文学术文本，并区分语言修改、实质方法建议和待补事实。
- 起草基于实际修改的审稿回复。

它会检查几个常见问题：把 W 显著写成“已达共识”、把经验阈值写成强制标准、把 AHP 写成必需的客观赋权、把未实施的程序写成已经完成。没有真实数据时给明确占位符；不会替课题编造结果或审批信息。

## 安装

仓库根目录就是 skill 目录，核心入口为 [SKILL.md](SKILL.md)。三端共用一套内容，无须修改正文。可克隆或解压仓库，然后使用 Python 3.9+ 的无依赖安装器：

```bash
git clone https://github.com/hudancqmu-cyber/delphi-plus.git
cd delphi-plus
```

```bash
python3 scripts/install.py --target codex --dry-run
python3 scripts/install.py --target codex
python3 scripts/install.py --target antigravity
python3 scripts/install.py --target claude-code
```

根据使用的客户端选择相应命令；不是必须安装三份。安装器只复制入口、参考材料、模板及可选 Codex 元数据；目标已存在时拒绝覆盖，原文件不会被改写。再次安装新版本前，先自行比较并另行保留旧版本。Windows 可用 `py -3` 替换 `python3`。

| 客户端 | 个人安装目录 | 项目安装目录 | 显式调用 |
|---|---|---|---|
| Codex | `~/.agents/skills/delphi-plus/` | `.agents/skills/delphi-plus/` | `$delphi-plus` |
| Antigravity | `~/.gemini/config/skills/delphi-plus/` | `.agents/skills/delphi-plus/` | App/CLI：`/delphi-plus`；IDE：按名称请求使用 |
| Claude Code | `~/.claude/skills/delphi-plus/` | `.claude/skills/delphi-plus/` | `/delphi-plus` |

项目安装示例：

```bash
python3 scripts/install.py --target claude-code --scope project --project "/path/to/your/project"
```

可手动将 `SKILL.md`、`references/`、`assets/`、`agents/` 放入上表的目录。选择项目范围时，Codex 与当前 Antigravity 可共享同一个 `.agents/skills/delphi-plus`；无需重复覆盖。避免同时在某一客户端的多个检索位置安装同名副本。

截至 **2026-11-06** 的官方目录核对见 [Codex](https://developers.openai.com/codex/skills/)、[Antigravity](https://antigravity.google/docs/skills)、[Claude Code](https://code.claude.com/docs/en/skills) 和 [Agent Skills规范](https://agentskills.io/specification)。部分旧版 Codex 使用 `~/.codex/skills`；旧版 Antigravity 使用 `.agent/skills` 或 `~/.gemini/antigravity/skills`，可依实际版本手动调整。新安装优先采用上表路径，安装后按客户端要求刷新技能或开启新会话。

## 使用示例

Codex：

```text
使用 $delphi-plus，基于我提供的材料起草护理质量评价指标的德尔菲函询方案。
目前尚未确定专家人数和共识阈值，请提出有理由的选项并标记待定项，不要编造结果。
```

Claude Code / Antigravity App 或 CLI：

```text
/delphi-plus 请润色下面的论文方法与结果段落，保留真实数值，
将语言修改、实质方法问题和待核实事实分开说明。
```

也可直接要求“使用 Delphi Plus 帮我设计第二轮反馈表”。自动匹配取决于客户端的技能发现与设置。

## 文件与方法学来源

```text
delphi-plus/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── methodology.md
│   ├── statistics.md
│   ├── writing-playbook.md
│   ├── reporting-and-sources.md
│   └── source-notes.md
├── assets/
│   ├── questionnaire-template.md
│   └── protocol-and-report-template.md
├── scripts/install.py
├── tests/test_install.py
├── VALIDATION.md
├── README.md
└── LICENSE
```

基于用户提供的《德尔菲法专家函询方法与实操(1).docx》提炼，并对主要方法边界作纠偏。原始 Word、嵌入图片和全文抽取不在仓库中。主要核验来源包括 ACCORD、CREDES、RAND DCAT、AHP原始方法文献及 Kendall’s W 官方包文档，见[来源目录](references/reporting-and-sources.md)与[提炼记录](references/source-notes.md)。

ACCORD 面向生物医学共识报告；CREDES 源自缓和医疗；DCAT用于批判性评价。其他领域可参照合适的透明报告原则，不能自动声称已符合全部指南。该 skill 支持写作和方法核查；研究设计选择和实际执行由研究者确认。

## 验证范围

采用标准 YAML 元数据和 Markdown，未引入客户端专属必需工具或执行指令。安装器只使用 Python 标准库，写作本身无需 Python 或联网。结构、引用路径、安装器及独立情景验证见 [VALIDATION.md](VALIDATION.md)。未逐一启动三个客户端做端到端运行测试。

原创 skill 文件与安装器按 MIT 许可提供；第三方指南和用户源文档保留其各自权利，见 [LICENSE](LICENSE)。
