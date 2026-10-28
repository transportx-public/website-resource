---
title: "CityWeave: Weaving User Needs and World Constraints for Personalized and Reliable Mobility Planning"
authors:
  - "Ao Wang"
  - "Zhiwen Chen"
  - "Shen Wang"
  - "Qiang Xia"
  - "Yi Zhou"
  - "Jian Li"
date: "2026-08-08T00:00:00+08:00"
doi: "10.1145/3770855.3818979"
publishDate: "2026-08-08T00:00:00+08:00"
publication_types:
  - "Conference Papers"
publication: "Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2, 12173-12182"
publication_short: "KDD 2026"
abstract: "CityWeave is a multimodal agent framework for personalized and reliable mobility planning under user and world constraints. It structures reasoning around Who, When, Where, and How, uses User-World Grounding to verify preferences and route feasibility, and trains the agent with supervised fine-tuning and reinforcement learning. Evaluations on 180,000 real-world planning records show strong gains in final pass rate, commonsense compliance, personalization, and reliability."
summary: "A grounded multimodal agent that reconciles traveler preferences with real-world route constraints."
tags:
  - "Mobility planning"
  - "Multimodal agents"
  - "User-world grounding"
  - "Reinforcement learning"
  - "Urban computing"
featured: true
url_pdf: ""
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: "https://mp.weixin.qq.com/s/4rybhLtB3IxCyckLV2na6A"
url_video: ""
image:
  caption: "CityWeave training and grounding framework. Source: [paper](https://doi.org/10.1145/3770855.3818979)."
  focal_point: Center
  preview_only: false
projects: []
slides: ""
---

## 研究概览

CityWeave 面向真实的门到门出行规划，同时考虑用户画像、时间窗口、地图拓扑和交通方式等约束。方法将规划过程拆解为 Who、When、Where 和 How 四个结构化槽位，再通过 User-World Grounding 模块检查个性化需求与导航可行性。

## 核心方法与发现

- 以 3W1H 结构约束多模态智能体的长链路推理和工具调用。
- 联合优化用户偏好、地点存在性、路线连通性、换乘合法性和时刻表约束。
- 在 18 万条真实出行规划记录上进行训练和评测，显著提升最终方案通过率、常识约束通过率、个性化和可靠性。

## 资料来源

- [ACM 论文 DOI](https://doi.org/10.1145/3770855.3818979)
- [TransportX Lab 公众号解读](https://mp.weixin.qq.com/s/4rybhLtB3IxCyckLV2na6A)
