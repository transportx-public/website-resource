---
title: "TransportX Agent"
date: "2026-09-30T00:00:00+08:00"
summary: "用自然语言分析道路、公交、轨道、出行需求与交通数据，并将结果整理为地图、图表、带引用的结论和报告。"
product_stage: "开源交通分析工作台"
hero_image: "product-video-preview.gif"
hero_headline: "从问题，到决策。"
hero_summary: "开源交通分析工作台，用自然语言分析数据、查看地图并交付报告。"
source_url: "https://github.com/Ran2424/transportx-agent"
guide_url: "/application/transportx-agent/guide/#start"
release_url: "https://github.com/Ran2424/transportx-agent/releases/tag/v3.22.0"
release_version: "v3.22.0"
download_intro: "请选择适合当前系统的桌面安装包。应用在本机运行，首次使用前需要配置一个兼容 Pi 的模型。"
release_notice: "macOS 安装包采用 ad-hoc 签名，未经过 Apple 公证。首次启动时，请在 Finder 中右键点击应用并选择“打开”。交通数据库、知识库原文、模型凭据和用户安装的 Module 不随安装包提供。"
product_facts:
  - label: "支持平台"
    value: "macOS arm64 / Windows x64"
  - label: "开源许可"
    value: "AGPL-3.0-only"
  - label: "使用界面"
    value: "桌面端 / Web / CLI"
downloads:
  - platform: "Windows"
    system: "Windows 10 22H2 或 Windows 11"
    architecture: "x64"
    format: "EXE 安装程序"
    size: "205.5 MiB"
    url: "https://download.transkgllm.com/releases/v3.22.0/TransportX.Agent-3.22.0-win-x64-setup.exe"
  - platform: "macOS"
    system: "macOS 12 或更高版本"
    architecture: "Apple Silicon"
    format: "DMG"
    size: "274.1 MiB"
    url: "https://download.transkgllm.com/releases/v3.22.0/TransportX-Agent-3.22.0-arm64.dmg"
    checksum_url: "https://download.transkgllm.com/releases/v3.22.0/TransportX-Agent-3.22.0-arm64.dmg.sha256"
demo_video: "transportx-v6-en-68s-1080p.mp4"
demo_poster: "product-event-traffic.png"
demo_intro: "查看从创建交通任务、在共享地图中分析，到完成报告交付的完整工作流。"
demo_caption: "68 秒英文产品演示，包含声音。"
story:
  workspace_title: 一个问题，展开一张交通分析工作台。
  workspace_intro: 对话、地图和分析结果并排呈现。切换下面的案例，看看一个问题如何变成可核查的成果。
  example_label: 示例提问
  result_label: 在工作台中查看
  screenshot_label: 真实任务截图，点击可查看大图
  scenes:
  - name: 活动交通
    image: product-event-traffic.png
    alt: 上海体育场周边道路速度与停车需求地图，以及 Agent 分析
    question: 上海体育场活动结束后，周边哪些道路需要重点关注？
    result: 在同一张地图上对照道路速度、停车需求与场馆位置，结合 Agent 的分析核查重点区域。
  - name: 站点接驳
    image: product-bike-transfer.png
    alt: 地铁线路、共享单车需求最高的五个站点与排名表
    question: 哪些地铁站的共享单车接驳需求最高？
    result: 把站点排名放回地图，查看需求分布与轨道线路，继续追问具体站点及周边范围。
  - name: 节假日出行
    image: product-holiday-ridehail.png
    alt: 节假日网约车需求图表与对比分析
    question: 节前、节中和节后，网约车需求有什么变化？
    result: 对照需求趋势与铁路到发量，检查时间范围和统计口径，再形成解释。
  features_title: 地图不是终点，报告也不只是一段回复。
  features_intro: 在地图上圈出要继续研究的区域；在报告里核查图表、引用和源文件。分析与交付连在一起。
  features:
  - kind: map
    label: 共享地图
    title: 圈出一个区域，继续问。
    image: product-map-selection.png
    alt: 上海轨道线路地图上的蓝色框选区域与需求图层
    intro: 点位、要素、矩形或当前视野，都可以成为下一轮分析的地理上下文。
    details: Agent 发布图层，你查看和选择。选区带着地图版本进入下一条消息，后续问题可以沿用同一空间范围，无需重新描述位置。
  - kind: report
    label: 成果交付
    title: 结论有图表，依据有出处。
    image: product-monthly-report.png
    alt: 客流月报中的趋势图、目录、引用和 PDF 导出入口
    intro: 图表、引用和分析说明进入同一份报告，原文件与 PDF 都能交付。
    details: 在文档画布里查看生成的 Markdown 报告，核对时间、单位、计算口径与引用，再下载原文件或生成 PDF。报告中的证据仍可回到源文件和工具输出核查。
  expand_label: 了解更多
  zoom_label: 查看大图
  close_label: 关闭预览
  module_title: 不同任务，装配不同能力。
  module_intro: 模型与 Module 在任务开始时选择。数据、知识、方法和工具按任务装配，具体版本随任务保留。
  module_image: product-task-setup.png
  module_alt: 新建交通任务中选择名称、模型和 Module 版本
  module_items:
  - title: 数据与知识
    description: 接入领域数据、知识原文与分析材料。
  - title: 方法与工具
    description: 通过 Skill、Extension 和运行时加入分析能力。
  - title: 图表与视频
    description: 生成图表，按需安装视频检索与处理能力。
  - title: 模板与版本
    description: 复用报告模板，保留任务使用的 Module 版本。
  module_link: 了解 Module 的使用方式 →
  video_title: 看一次从提问到报告的完整过程。
  about_title: 为什么做 TransportX？
  source_label: 查看开源仓库 →
---

Codex、Claude Code 等编程 Agent 进步很快，但实际使用通常仍离不开代码、终端和文件结构。对于需要分析交通数据、制作地图，却没有编程背景的业务人员，这仍是一道明显门槛。

TransportX 的出发点很简单：让交通分析人员能直接使用 Agent 完成提问、分析、制图和成果交付，并保留结果所依据的数据与过程。平台本身保持轻量，具体数据、知识、方法和工具通过 Module 装配，因此也可以适配交通之外的数据分析场景。
