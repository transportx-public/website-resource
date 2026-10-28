---
title: "组会 | 2026-04-24"
event: "课题组组会"
summary: "本次组会收录 3 篇文献阅读分享。"
abstract: ''
date: "2026-04-24T00:00:00+08:00"
all_day: true
publishDate: "2026-04-24T00:00:00+08:00"
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
  - name: "董昱菡"
    profile: "Yuhan Dong"
  - name: "果金杉"
    profile: "Jinshan Guo"
  - name: "夏强"
    profile: "Qiang Xia"
readings:
  - title: "AgentMove 复现汇报：基于 GPT-4o-mini 的零样本下一位置预测"
    sequence: 103
    reader_name: "董昱菡"
    reader_profile: "Yuhan Dong"
    published: "2026-04"
    source: "技术报告"
    highlight: "AgentMove 面向的是 next location prediction，也就是根据用户过去的活动轨迹，预测他下一次最可能到达的地点。这个项目的核心思路不是直接把历史轨迹扔给大模型让它“猜答案”，而是先把问题拆解成三个子任务：个人移动规律建模、城市空间知识建模、群体迁移规律建模，再把三部分结果统一组织成 prompt，交给 LLM 做最终推理。"
    url: ""
    slides: ""
  - title: "Learning Universal Human Mobility Patterns with a Foundation Model for Cross-domain Data Fusion"
    sequence: 104
    reader_name: "果金杉"
    reader_profile: "Jinshan Guo"
    published: "2025-07"
    source: "Preprint submitted to Elsevier"
    highlight: "本文提出了一种基于跨域数据融合的人类出行模式基础模型框架，通过整合GPS轨迹、兴趣点、家庭出行调查等多模态异构数据源，构建兼顾隐私保护与语义完整性的合成出行数据集。框架包含三项核心创新：其一，以大语言模型为语义融合核心组件，对GPS停留点进行活动语义标注，突破传统规则方法在多功能场所识别上的语义理解瓶颈；其二，设计三层次迁移学习机制，覆盖从有调查数据的监督适配到数据稀缺地区的半监督迭代适配，实现跨地区、跨文化的知识迁移；其三，提出人口适配模块，无需个体级配对标签即可将合成活动链与人口社会经济特征对齐。框架在洛杉矶县通过百万级智能体交通仿真完成端到端验证，并在埃及数据稀缺场景下完成跨文化迁移测试。"
    url: ""
    slides: ""
  - title: "A Review of Human Mobility: Linking Data, Models, and Real-World Applications"
    sequence: 105
    reader_name: "夏强"
    reader_profile: "Qiang Xia"
    published: "2025-08"
    source: "Journal of Computational Social Science"
    highlight: "研究对象足够重要\n人类移动连接人口分布、经济活动、文化交流和社会结构。\n它既影响个体日常出行，也影响跨区域传播、城市组织和基础设施配置。\n这篇综述的价值它把数据源、模型和应用放到同一篇文章里讨论，延续了 Barbosa 等人的综述\n框架。 读下来最清楚的一点是：数据怎么支撑模型，模型又怎么落到真实问题里"
    url: ""
    slides: ""
---
