---
title: "组会 | 2026-05-29"
event: "课题组组会"
summary: "本次组会收录 3 篇文献阅读分享。"
abstract: ''
date: "2026-05-29T00:00:00+08:00"
all_day: true
publishDate: "2026-05-29T00:00:00+08:00"
authors: []
tags:
  - "组会"
  - "文献分享"
featured: false
image:
  caption: ''
  focal_point: Center
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
slides: ''
projects: []
meeting_slides: ""
meeting_notes: ""
reading_members:
  - name: "果金杉"
    profile: "Jinshan Guo"
  - name: "卢永晟"
    profile: "Yongsheng Lu"
  - name: "夏强"
    profile: "Qiang Xia"
readings:
  - title: "Travel Demand Modeling and Estimation for High-Dimensional Mobility"
    sequence: 113
    reader_name: "果金杉"
    reader_profile: "Jinshan Guo"
    published: "2025-03"
    source: "IEEE Transactions on Mobile Computing"
    highlight: "本文针对城市出行数据高维度、大规模的特点，提出了一种基于概率张量分解的出行需求建模与预测方法。具体而言，作者将出行数据表示为起点、终点、出发时间三维概率张量，通过潜在类别模型将其分解为少数几个空间基础模式及反映模式时序交互的核心张量 Π，并设计 EM 算法对上述参数进行推断。在预测阶段，作者固定空间模式，仅对低维核心张量 Π 进行时序预测（结合 DMD、LSTM、ARIMA 三种算法），再重建完整的未来 OD 概率分布，使输入维度从 265×265 压缩至 10×10，仅为原来的 0.14%。以纽约市黄色出租车与网约车数据为案例，实验结果表明，该方法在建模精度和预测精度上均优于直接对全维 OD 矩阵进行预测的基线方法，其中 LSTM 组合方案在长时域预测中表现最优，验证了利用低维时空模式进行高效出行需求概率预测的可行性。"
    url: ""
    slides: ""
  - title: "Pedestrian-Aware LLM-Driven Behavioral Planning for Autonomous Vehicles"
    sequence: 114
    reader_name: "卢永晟"
    reader_profile: "Yongsheng Lu"
    published: "2026-05"
    source: "arXiv"
    highlight: "本文提出了一个创新的、基于大语言模型（LLM）的自动驾驶决策框架。该框架通过将驾驶场景转化为自然语言提示，利用LLM的强大推理能力来理解行人意图、预测风险并生成安全的驾驶决策，解决了传统强化学习方法泛化能力差、决策不透明的问题。"
    url: ""
    slides: ""
  - title: "TransitLM: A Large-Scale Dataset and Benchmark for Map-Free Transit Route Generation"
    sequence: 115
    reader_name: "夏强"
    reader_profile: "Qiang Xia"
    published: "2026-05"
    source: "arXiv"
    highlight: "传统上，公共交通路线规划依赖于结构化的地图基础设施和复杂的路径规划引擎，而现有的数据集无法支持训练模型绕过这种依赖性。我们推出了 TransitLM，这是一个大规模数据集，包含来自中国四个城市的超过 1300 万条公交路线规划记录，涵盖 120,845 个站点和 13,666 条线路。该数据集以持续预训练语料库和基准数据集的形式发布，用于三个评估任务，并采用互补的评估指标。实验表明，基于 TransitLM 训练的 LLM 模型能够生成结构有效的高精度路线，并且无需任何显式映射即可将任意 GPS 坐标隐式地映射到相应的站点。这些结果表明，公交路线规划可以完全从数据中学习，从而能够直接从起点-终点信息生成端到端、无需地图的路线。"
    url: ""
    slides: ""
---
