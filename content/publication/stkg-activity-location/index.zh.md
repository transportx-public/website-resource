---
title: "A spatiotemporal knowledge graph-based method for identifying individual activity locations from mobile phone data"
authors:
  - "Jian Li"
  - "Tian Gan"
  - "Weifeng Li"
  - "Yuhang Liu"
date: "2025-04-01T00:00:00+08:00"
doi: "10.1016/j.jtrangeo.2025.104157"
publishDate: "2025-04-01T00:00:00+08:00"
publication_types:
  - "Journal Publications"
publication: "Journal of Transport Geography, 124, 104157"
publication_short: "JTG"
abstract: "This study proposes a spatiotemporal knowledge graph method for identifying individual activity locations from mobile phone data. Spatial adjacency and temporal co-occurrence are modeled as separate graphs, fused into a weighted spatiotemporal graph, and partitioned with Louvain community detection. A Shanghai case study shows tighter spatial boundaries and more stable temporal identification than conventional threshold-based and spatiotemporal clustering methods."
summary: "A parameter-light graph method that fuses spatial and temporal relationships to identify activity locations."
tags:
  - "Human mobility"
  - "Mobile phone data"
  - "Activity location"
  - "Spatiotemporal knowledge graph"
  - "Community detection"
featured: false
url_pdf: ""
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: "https://mp.weixin.qq.com/s/3xVU8HID9ejc3gHx6BX3Lw"
url_video: ""
image:
  caption: "Spatiotemporal knowledge graph framework for activity-location identification. Source: [paper](https://doi.org/10.1016/j.jtrangeo.2025.104157)."
  focal_point: Center
  preview_only: false
projects: []
slides: ""
---

## 研究概览

本研究针对手机信令数据时间稀疏、空间定位不确定以及传统聚类方法依赖人工阈值的问题，将个体轨迹组织为时空知识图谱。方法同时推断停留点的空间邻接关系和时间相似关系，再识别紧密关联的活动地点群。

## 核心方法与发现

- 用三元组表示个体、停留点、时间片及其关系，形成可解释的轨迹语义结构。
- 基于 Queen 邻接构建空间图，基于时间片余弦相似度构建时间图，并将两者融合。
- 使用 Louvain 社区发现自动识别活动地点，在上海案例中改善空间边界精度和日间稳定性。

## 资料来源

- [论文 DOI](https://doi.org/10.1016/j.jtrangeo.2025.104157)
- [TransportX Lab 公众号解读](https://mp.weixin.qq.com/s/3xVU8HID9ejc3gHx6BX3Lw)
