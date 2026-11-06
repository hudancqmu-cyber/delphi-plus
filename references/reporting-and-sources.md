# 报告审查与已核验来源

## 先确定规范的用途

- **ACCORD（2024）** 面向生物医学共识研究的报告透明度，不是决定研究如何设计的统一方法标准，也不等同于质量评分。教育、工程等领域可借鉴其透明报告思路，但应说明这是参照，不能直接声称其适用于所有领域。
- **CREDES（2017）** 源自缓和医疗 Delphi 的方法学综述与建议；跨领域使用应说明适用性。
- **RAND DCAT（2023）** 是 Delphi 研究的批判性评价工具。判定需给证据；不确定的信息标为不确定。整体评级需要理由，手册的降级建议不应被编成脱离研究情境的自动评分器。

用户明确要求官方清单逐项核对时，取得适用版本原文及附件，对每项给出证据位置、缺失和不适用理由。下列项目是本 skill 自编的写作检查框架，不冒充任何官方逐字清单或完整编号映射。

## 按交付物审查

| 核查域 | 需要看到的证据 | 缺失时如何写 |
|---|---|---|
| 目的与适用范围 | 为什么使用共识方法、输出是什么、面向谁 | 缩小结论或列具体待补项 |
| 设计与分工 | 实际变体、组织者/评分者职责 | 不以“修正Delphi”代替过程描述 |
| 条目来源 | 资料获得方式、条目形成和预审记录 | 不把一般检索改称系统综述 |
| 面板与招募 | 资格、角色覆盖、人数理由、邀请/参与记录 | 不仅给最终人数而遗漏过程 |
| 评分工具 | 全部锚点、各维度、无法判断及文字反馈 | 指出规则无法操作的具体位置 |
| 预设决策 | 共识、条目处理、稳定性和终止各自定义 | 不把事后规则写成事先规定 |
| 反馈与匿名 | 反馈材料、身份可见边界、重评机会 | 只描述实际提供的反馈 |
| 参与及缺失 | 每轮计数、分母、流失/补招、逐项有效n | 不拿回收率代替偏倚评估 |
| 条目演进 | 稳定ID、版本与增删合并拆分理由 | 不只展示最终入选名单 |
| 定量与定性发现 | 实际分布、意见摘要、未达共识与异议 | 不把未提供的统计写成已分析 |
| 解释与局限 | 与研究输出相符的结论、适用边界 | 不把共识外推为有效性证明 |
| 研究治理与材料 | 实际伦理/同意、注册状态、资助/利益冲突、材料可得性 | 未做/未注册如实写；缺记录先确认 |

审查结论分为“有记录支持”“需补报告”“需确认实际执行”“实质设计问题”。报告缺失不能自动判为程序未做；没有证据也不能默认已经完成。

## 来源目录

以下来源于制作时核验，核验日期 **2026-11-06**。实际投稿应再查看期刊要求及指南版本；不得声称已自动覆盖日后的修订。此处均为摘要性方法说明或书目信息，不复制完整清单。

1. Gattrell WT, et al. *ACCORD (ACcurate COnsensus Reporting Document): A reporting guideline for consensus methods in biomedicine developed via a modified Delphi.* PLOS Medicine. 2024;21:e1004326. DOI: [10.1371/journal.pmed.1004326](https://doi.org/10.1371/journal.pmed.1004326)。用于判断报告指南的范围与用途。
2. Logullo P, et al. *ACcurate COnsensus Reporting Document (ACCORD) explanation and elaboration: Guidance and examples to support reporting consensus methods.* PLOS Medicine. 2024;21:e1004390. DOI: [10.1371/journal.pmed.1004390](https://doi.org/10.1371/journal.pmed.1004390)。用于核查具体报告解释，不凭摘要补造逐字清单。
3. Jünger S, Payne SA, Brine J, Radbruch L, Brearley SG. *Guidance on Conducting and REporting DElphi Studies (CREDES) in palliative care: Recommendations based on a methodological systematic review.* Palliative Medicine. 2017;31:684–706. DOI: [10.1177/0269216317690685](https://doi.org/10.1177/0269216317690685)；[EQUATOR索引](https://www.equator-network.org/reporting-guidelines/credes/)；[PubMed](https://pubmed.ncbi.nlm.nih.gov/28190381/)。
4. Khodyakov D, Grant S, Kroger J, Bauman M. *RAND Methodological Guidance for Conducting and Critically Appraising Delphi Panels.* RAND Corporation. 2023;TL-A3082-1. DOI: [10.7249/TLA3082-1](https://doi.org/10.7249/TLA3082-1)；[官方发布页](https://www.rand.org/pubs/tools/TLA3082-1.html)；[完整PDF](https://www.rand.org/content/dam/rand/pubs/tools/TLA3000/TLA3082-1/RAND_TLA3082-1.pdf)。用于核查 DCAT 结构及评价建议。
5. Saaty TL. *Decision making with the analytic hierarchy process.* International Journal of Services Sciences. 2008;1:83–98. DOI: [10.1504/IJSSCI.2008.017590](https://doi.org/10.1504/IJSSCI.2008.017590)。用于区分成对比较判断、赋权与所谓“客观”评价。
6. R package `irr`, [`kendall` 官方手册](https://search.r-project.org/CRAN/refmans/irr/html/kendall.html)。用于核查 W 的输入、并列校正与检验解释；不是默认依赖包，也不表示此 skill 已执行 R。
7. 原始实证研究 [BMJ Open 2021;11:e055422（PDF）](https://bmjopen.bmj.com/content/bmjopen/11/12/e055422.full.pdf)。用于说明 Ca 赋值存在不同实现；该研究中的阈值不能自动推广到其他课题。

RAM、FDM、RI表和各学科实证数值未逐一收入本来源目录；研究实际涉及这些内容时，取得所采用版本的原始文献后再写具体参数和判定。
