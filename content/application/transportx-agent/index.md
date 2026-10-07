---
title: "TransportX Agent"
date: "2026-09-30T00:00:00+08:00"
summary: "Ask transport questions, inspect evidence on a shared map, and deliver cited reports from one desktop workspace."
product_stage: "Open-source transport analysis workspace"
hero_image: "product-video-preview.gif"
hero_headline: "From a transport question to a cited report."
hero_summary: "Analyze data, explore maps, and deliver reports with an open-source desktop agent."
source_url: "https://github.com/Ran2424/transportx-agent"
guide_url: "/application/transportx-agent/guide/#start"
release_url: "https://github.com/Ran2424/transportx-agent/releases/tag/v3.22.0"
release_version: "v3.22.0"
download_intro: "Choose the desktop build for your platform. The application runs locally and requires a Pi-compatible model configured on first use."
release_notice: "The macOS build uses ad-hoc signing and is not Apple-notarized. On first launch, right-click the app in Finder and choose Open. Traffic databases, source knowledge collections, model credentials, and user-installed Modules are not included."
product_facts:
  - label: "Platforms"
    value: "macOS arm64 / Windows x64"
  - label: "License"
    value: "AGPL-3.0-only"
  - label: "Clients"
    value: "Desktop / Web / CLI"
downloads:
  - platform: "Windows"
    system: "Windows 10 22H2 or Windows 11"
    architecture: "x64"
    format: "EXE installer"
    size: "205.5 MiB"
    url: "https://github.com/Ran2424/transportx-agent/releases/download/v3.22.0/TransportX.Agent-3.22.0-win-x64-setup.exe"
  - platform: "macOS"
    system: "macOS 12 or later"
    architecture: "Apple Silicon"
    format: "DMG"
    size: "274.1 MiB"
    url: "https://github.com/Ran2424/transportx-agent/releases/download/v3.22.0/TransportX-Agent-3.22.0-arm64.dmg"
    checksum_url: "https://github.com/Ran2424/transportx-agent/releases/download/v3.22.0/TransportX-Agent-3.22.0-arm64.dmg.sha256"
demo_video: "transportx-v6-en-68s-1080p.mp4"
demo_poster: "product-event-traffic.png"
demo_intro: "See the full workflow from creating a traffic task to shared-map analysis and report delivery."
demo_caption: "68-second product overview with sound."
story:
  workspace_title: One question. A shared transport workspace.
  workspace_intro: Keep conversation, maps, and findings side by side. Explore the examples to see a question become a result
    you can inspect.
  example_label: Example question
  result_label: Inspect in the workspace
  screenshot_label: Real task screenshot. Click to view full size.
  scenes:
  - name: Event traffic
    image: product-event-traffic.png
    alt: Road speeds and parking demand around Shanghai Stadium beside the agent analysis
    question: Which roads need attention after an event at Shanghai Stadium?
    result: Compare road speeds, parking demand, and venue location on one map, then review the agent findings.
  - name: Station connections
    image: product-bike-transfer.png
    alt: Metro lines, shared-bike station demand, and a ranking table
    question: Which metro stations have the highest shared-bike connection demand?
    result: Place station rankings on the map, inspect nearby transit lines, and ask about a specific station or area.
  - name: Holiday travel
    image: product-holiday-ridehail.png
    alt: Holiday ride-hailing demand chart beside comparative analysis
    question: How does ride-hailing demand change before, during, and after a holiday?
    result: Compare demand trends with rail arrivals and departures. Check time ranges and definitions before drawing conclusions.
  features_title: Keep the map in the conversation. Keep evidence in the report.
  features_intro: Select an area to investigate further. Review charts, citations, and source files in the report. Analysis
    and delivery stay connected.
  features:
  - kind: map
    label: Shared map
    title: Select an area. Ask the next question.
    image: product-map-selection.png
    alt: A selected area and demand layers on a Shanghai transit map
    intro: Return a point, feature, rectangle, or viewport as geographic context for the next question.
    details: The agent publishes layers; you inspect and select. Selections enter the next message with their map revision,
      keeping the same spatial scope without describing the location again.
  - kind: report
    label: Report delivery
    title: Findings with charts. Evidence with sources.
    image: product-monthly-report.png
    alt: Passenger-flow report with trend chart, citations, outline, and PDF export
    intro: Charts, citations, and findings become one report. Deliver the original file or a PDF.
    details: Review the generated Markdown report in the document canvas. Check dates, units, methods, and citations, then
      download the source or export a PDF. Findings remain connected to source files and tool output.
  expand_label: Learn more
  zoom_label: View full size
  close_label: Close preview
  module_title: Different tasks. Different capabilities.
  module_intro: Choose a model and Modules when creating a task. Add the data, knowledge, methods, and tools needed for the
    work, with exact versions retained.
  module_image: product-task-setup.png
  module_alt: New traffic task dialog with model and Module version choices
  module_items:
  - title: Data and knowledge
    description: Bring domain datasets, source knowledge, and analysis material.
  - title: Methods and tools
    description: Add Skills, Extensions, and native analysis runtimes.
  - title: Charts and video
    description: Create charts and install video search and processing capabilities.
  - title: Templates and versions
    description: Reuse report templates and retain the Module versions used by each task.
  module_link: Explore Modules (中文) →
  video_title: Watch a question become a finished report.
  about_title: Why TransportX?
  source_label: Explore the source on GitHub →
---

Coding agents such as Codex and Claude Code have improved quickly, but using them still often means working with code, terminals, and unfamiliar file structures. That remains a real barrier for many domain specialists, particularly non-programmers who need to analyze traffic data or build map-based explanations.

TransportX began with a simple goal: make agent-assisted analysis practical for transport professionals. It is a lightweight desktop workspace for asking questions, inspecting maps and charts, and delivering results with their evidence attached. The core stays small. Modules add the data, knowledge, methods, and tools required by a field, which also makes the platform useful beyond transport.
