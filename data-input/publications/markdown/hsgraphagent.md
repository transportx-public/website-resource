## 研究概览

HSGraphAgent 将海关 HS 编码体系建模为包含层级关系和排除规则的知识图谱，引导大语言模型从 Section、Chapter、Heading 到 Subheading 逐级完成商品归类。该方法强调规则约束与可解释推理，避免仅凭文本相似度选择编码。

## 核心方法与发现

- Select 阶段只在当前节点的合法子节点中选择，保证层级路径有效。
- Redirect 阶段在触发税则排除条件时动态修正推理路径。
- 在 6 位 HS Code 细粒度任务上，图谱引导的分层推理明显优于直接生成和常规 RAG 基线。

## 资料来源

- [ACL Anthology DOI](https://doi.org/10.18653/v1/2026.acl-long.2072)
- [HSBench 代码与数据](https://github.com/VoldeMordddddd/HSBench)
- [TransportX Lab 公众号解读](https://mp.weixin.qq.com/s/RV14fJCbhqTD2RtKYkaPwQ)
