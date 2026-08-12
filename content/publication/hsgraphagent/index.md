---
title: "HSGraphAgent: Knowledge-Graph-Guided Large Language Models for Harmonized System Code Classification"
authors:
  - "Qiang Xia"
  - "Zijian Zhang"
  - "Ao Wang"
  - "Wenhan Wang"
  - "Xiangyu Wang"
  - "Jian Li"
date: "2026-07-01T00:00:00+08:00"
doi: "10.18653/v1/2026.acl-long.2072"
publishDate: "2026-07-01T00:00:00+08:00"
publication_types:
  - "Conference Papers"
publication: "Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics, 44761-44773"
publication_short: "ACL 2026"
abstract: "HSGraphAgent represents the Harmonized System hierarchy and exclusion notes as an explicit knowledge graph that guides large language models through legal classification paths. Its Select-Redirect mechanism restricts each decision to valid child nodes and redirects reasoning when an exclusion rule is triggered. Experiments on four-digit headings and six-digit HS codes show that rule-aware graph reasoning substantially improves fine-grained accuracy and interpretability over direct generation and retrieval-augmented baselines."
summary: "A rule-aware graph agent for accurate and explainable Harmonized System code classification."
tags:
  - "Harmonized System"
  - "Customs classification"
  - "Knowledge graph"
  - "Large language models"
  - "Rule-guided reasoning"
featured: true
url_pdf: ""
url_code: "https://github.com/VoldeMordddddd/HSBench"
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: "https://mp.weixin.qq.com/s/RV14fJCbhqTD2RtKYkaPwQ"
url_video: ""
image:
  caption: "HSGraphAgent knowledge-graph-guided reasoning framework. Source: [paper](https://doi.org/10.18653/v1/2026.acl-long.2072)."
  focal_point: Center
  preview_only: false
projects: []
slides: ""
---

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
