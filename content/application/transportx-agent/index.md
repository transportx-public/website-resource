---
title: "TransportX Agent"
date: "2026-09-30T00:00:00+08:00"
summary: "Ask transport questions, inspect evidence on a shared map, and deliver cited reports from one desktop workspace."
product_stage: "Open-source transport analysis workspace"
hero_image: "product-video-preview.gif"
hero_headline: "From question to decision"
hero_summary: "Analyze data, explore maps, and deliver reports with an open-source desktop agent."
source_url: "https://github.com/Ran2424/transportx-agent"
guide_url: "/application/transportx-agent/guide/#start"
release_url: "https://github.com/Ran2424/transportx-agent/releases/tag/v3.23.0"
release_version: "v3.23.0"
download_intro: "Choose the desktop build for your platform. The application runs locally and requires a Pi-compatible model configured on first use."
release_notice: "3.23.0 is available for Windows x64 and macOS Apple Silicon. The Windows installer is unsigned; the Mac build is ad-hoc signed without Apple notarization. Install manually once when upgrading from 3.22."
release_notes_title: "What's new in 3.23"
release_notes: |
  3.23 improves conversation readability, file reuse, and reliability, and adds local model access and in-app updates. The **3.23.0 stable release** is available for Windows x64 and macOS Apple Silicon.

  ### Features and improvements

  - **Clearer update status**: see both the installed version and the latest version on the website. No available update or an unpublished update manifest now produces a normal status message. If a newer build is available only on the website, a manual download option is shown.
  - **Download and install updates in the app**: view download progress and restore verified downloads. Installation requires your confirmation to restart, waits until tasks are idle, and does not run on an ordinary quit.
  - **Local model access**: connect to Chat Completions-compatible services on your computer or local network, with address presets for Ollama and LM Studio. Test the connection, retrieve available models, and select one; an API key is optional depending on the service.
  - **Easier conversation reading**: thinking and tool calls collapse into expandable Working sections with elapsed time. Text, tables, and code have improved widths, spacing, and font sizes, with more readable supporting text across Light, Dark, and Sand themes.
  - **Reuse uploaded files**: browse, preview, and select files already uploaded to a task. Removing a file from the next message does not delete it. Attachments, map selections, and Canvas context have clearer pending, uploading, and failed states.
  - **Inspect results and citations**: result cards show filenames and an open action. Canvas shows the selected view's title and version, and citations expand to reveal excerpts, dates, and source details.
  - **Find the cause of problems**: open the runtime log folder from Settings. Model failures show a reason, retry status, and diagnostic identifier, with an option to put the original question back in the composer for editing and resubmission.

  ### Bug fixes

  - Fixed unsent text and attachments getting lost or appearing in another conversation. Drafts are saved per conversation and survive refreshes; you can return to an upload after switching conversations.
  - Fixed Enter submitting a message while confirming Chinese input. Uploads still in progress or failed-only attachments no longer trigger an invalid submission.
  - Fixed blank or outdated map screenshots caused by capturing before rendering finished. Rendering failures now show an error instead of saving an invalid screenshot.
  - Fixed the end of a streamed reply remaining out of view, tool expansion choices being lost after switching conversations, and inaccurate timing across Working sections.
  - Fixed context association and history restoration for messages combining files, map selections, and Canvas context, and kept internal attachment hints out of the user message.
  - Improved oversized-upload errors with readable limits and file details; fixed concurrent upload indexing and temporary-file cleanup after failed uploads.
  - Fixed stale responses overwriting the current conversation after reconnection or navigation. Improved message confirmation and cancellation handling to reduce inconsistent state and repeated operations.
  - Strengthened configuration and attachment-index writes, backups, and crash recovery. Improved shutdown and task-deletion cleanup, preserving records for retry when cleanup fails.

  ### Installation and updates

  - **Requirements**: macOS 12 or later on Apple Silicon (arm64). [Download Mac 3.23.0](https://download.transkgllm.com/releases/v3.23.0/TransportX-Agent-3.23.0-mac-arm64.dmg).
  - **Upgrading from 3.22 or an older build**: install this version manually once. Later compatible builds can be downloaded in the app and installed by confirming restart-to-update.
  - **First launch**: the Mac build is ad-hoc signed and has not been notarized by Apple. If macOS blocks it, follow the system prompts in Finder or Privacy & Security to allow it to open.
  - **Windows users**: requires Windows 10 22H2 or Windows 11 (x64). [Download Windows 3.23.0](https://download.transkgllm.com/releases/v3.23.0/TransportX-Agent-3.23.0-win-x64-setup.exe) and verify it with the accompanying SHA-256 file. The installer has no Authenticode signature.
product_facts:
  - label: "Platforms"
    value: "macOS arm64 / Windows x64"
  - label: "License"
    value: "AGPL-3.0-only"
  - label: "Clients"
    value: "Desktop / Web / CLI"
downloads:
  - platform: "Windows"
    version: "v3.23.0"
    system: "Windows 10 22H2 or Windows 11"
    architecture: "x64"
    format: "EXE installer"
    size: "220.2 MiB"
    url: "https://download.transkgllm.com/releases/v3.23.0/TransportX-Agent-3.23.0-win-x64-setup.exe"
    checksum_url: "https://download.transkgllm.com/releases/v3.23.0/TransportX-Agent-3.23.0-win-x64-setup.exe.sha256"
  - platform: "macOS"
    version: "v3.23.0"
    system: "macOS 12 or later"
    architecture: "Apple Silicon"
    format: "DMG"
    size: "274.5 MiB"
    url: "https://download.transkgllm.com/releases/v3.23.0/TransportX-Agent-3.23.0-mac-arm64.dmg"
    checksum_url: "https://download.transkgllm.com/releases/v3.23.0/TransportX-Agent-3.23.0-mac-arm64.dmg.sha256"
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
