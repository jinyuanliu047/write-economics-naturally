# Write Economics Naturally

**试用版 v0.2.0 · 2026-10-30**

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

## 一次完整使用

入口是 `SKILL.md`。它已经整合了作者的默认风格、段落论证、全文各节的写法和交付检查；不依赖原项目的文件或聊天记录。默认不用 em dashes，避免生僻词、长句和机械重复的 “We”，要求每句话有动机、前后有承接。显著性和数字应有证据支持，研究设定随当前论文确定。

首次让新的 AI 学习时，可以直接复制：

> Use $write-economics-naturally. Follow the first-use study guide to read the 150 source articles, keep your own source-based progress record, and synthesize the writing practices across the whole paper. Do not inherit another assistant's read status. Then apply the method to my paper while preserving its research choices and evidence.

`references/first-use-study.md` 提供可续接的逐篇学习流程。阅读记录从 150 篇“未读”开始，保存实际来源、版本、阅读位置及具体写法分析。打不开的单独标记，不能当作读过。`scripts/reading_tracker.py` 可初始化和检查记录；记录检查不能替代实际阅读。完成学习后可复用总结，不用每次改段落都重读。工具没有原文访问能力时，应如实说明学习尚未完成。

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
- `references/reading-ledger.json`：150 篇文章的公开来源、参考版本和阅读位置，不携带新读者的“已读”状态。
- `references/first-use-study.md` 与 `scripts/reading_tracker.py`：首次学习、逐篇记录和进度检查。
- `agents/openai.yaml`：技能显示名称与简短说明。
- `TRY_IT.md`：可复制的试用题和检查点。

## 阅读来源与范围

源目录涵盖 AER、QJE、JPE、Econometrica、ReStud 各 30 篇文章，并区分正式发表稿、校样和作者稿。原始整理记录了摘要、完整引言、选定结果或理论论证及完整结论的位置；新读者按首次学习流程阅读完整正文并另存自己的记录。还参考了 Lin 的 1992 年 AER 文章及 Goldin 的历史写作。包内不含期刊 PDF、论文项目文件、私人路径或原始研究数据。

## 试用反馈

可以用 `TRY_IT.md` 比较启用前后的同一段改写。反馈时最有用的信息是：哪一句更流畅、哪处改变了研究含义、遗漏了什么比较对象，以及是否出现了新的套话。请勿在反馈中附上不能公开的原始数据。

## 参与改进

欢迎通过 [Issues](https://github.com/jinyuanliu047/write-economics-naturally/issues) 提出反馈，或提交 Pull Request。主分支由维护者审核和合并；请参阅 [贡献说明](CONTRIBUTING.md)。
