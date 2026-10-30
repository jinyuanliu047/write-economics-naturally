# Write Economics Naturally

**试用版 v0.1.0 · 2026-10-30**

一个用于英文经济学论文的写作 skill。它帮助作者把研究动机、识别比较和实证结果写成连贯的论证，覆盖摘要、引言、数据、设计、结果、机制、稳健性、结论及图表注释。

它学习的是经济学论文的行文习惯，并不套用期刊版式或模仿某一位作者的原句。改写应保留作者声音、研究设定和证据强弱。

## 安装与使用

在 Codex 中，可以直接说：

> Install the skill from https://github.com/jinyuanliu047/write-economics-naturally

也可手动安装到尚不存在的 skill 目录：

```bash
git clone https://github.com/jinyuanliu047/write-economics-naturally.git ~/.codex/skills/write-economics-naturally
```

已有同名 skill 时，请先比较版本，保留自己的修改。ZIP 版可从 [Releases](https://github.com/jinyuanliu047/write-economics-naturally/releases) 下载；将解压后的 `write-economics-naturally` 文件夹放入 `~/.codex/skills/`，保持 `SKILL.md` 与 `references/` 的相对位置。

在新的任务中使用 `$write-economics-naturally`，并给出需要修改的文字、当前结果和重要约束。其他支持文件式 skills 的工具也可使用这些文件，具体导入方式以所用工具为准；或让助手先阅读 `SKILL.md` 及相关参考文件，再修改文字。

## 建议的首次试用

> Use $write-economics-naturally to revise the following results paragraph. Explain the economic comparison naturally, preserve the estimates and inference, and make only changes justified by the supplied evidence. Return the revised paragraph and a short explanation of the main edits.

请同时提供：估计值和单位、样本、对照组或比较对象、主要设定，以及你希望保留的用词或风格。仅提供一段文字时，skill 应保留现有事实，并标明需要核实的地方。

## 它具体改善什么

- 先把人、制度和比较讲清楚，再引入技术标签。
- 让后一句承接前一句，而非逐行翻译回归表。
- 根据论证选择句子主语，减少机械重复的 “We”。
- 用有依据的数字说明结果；支持时可以使用 “significantly”。
- 先解释发现的经济含义，再给出确实影响解释的具体条件。
- 明确区分核心概念、代理变量、机制证据和后续结果。
- 在正文、附录和表注间保持一致，避免无归属的 Panel 引用。

它不会自行换样本、变换变量、改变固定效应，或为了显著性选择模型。重要的敏感性结果也应保留。

## 包内文件

- `SKILL.md`：入口和核心工作流程。
- `references/prose-craft.md`：用词、句子主语与段落衔接。
- `references/empirical-sections.md`：实证比较、结果、机制、稳健性与注释。
- `references/editing-examples.md`：合成示例，不含未发表项目的实证结果。
- `references/reading-ledger.json`：150 篇文章的公开来源、阅读版本和章节位置。
- `agents/openai.yaml`：技能显示名称与简短说明。
- `TRY_IT.md`：可复制的试用题和检查点。

## 阅读来源与范围

阅读记录涵盖 AER、QJE、JPE、Econometrica、ReStud 各 30 篇文章。记录区分正式发表稿、校样和作者稿。范围是摘要（若有）、完整引言、选定结果或理论论证、完整结论；并非宣称逐字阅读了所有文章及附录。还参考了 Lin 的 1992 年 AER 文章及 Goldin 的历史写作。包内不含期刊 PDF、论文项目文件、私人路径或原始研究数据。

## 试用反馈

可以用 `TRY_IT.md` 比较启用前后的同一段改写。反馈时最有用的信息是：哪一句更流畅、哪处改变了研究含义、遗漏了什么比较对象，以及是否出现了新的套话。请勿在反馈中附上不能公开的原始数据。
