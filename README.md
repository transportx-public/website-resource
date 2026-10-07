# TransportX Website

TransportX 课题组的中英文静态网站，基于 Hugo 与 Hugo Blox 构建。线上地址：<https://transportxlab.com/>。

## 技术栈

- Hugo Extended `0.134.1`
- Hugo Blox Bootstrap v5
- Python 3.10、`openpyxl`、`PyYAML`（内容同步）
- GitHub Actions、GitHub Pages（构建与发布）

## 内容维护

人员、新闻、活动和论文统一在 `data-input/` 中维护；字段说明见 [`data-input/README.md`](data-input/README.md)。不要直接修改脚本生成的对应页面。以下命令均从仓库根目录运行。

同步全部结构化内容：

```bash
python3 scripts/sync_content_from_data_input.py
```

只同步某一类内容：

```bash
python3 scripts/sync_content_from_data_input.py people
python3 scripts/sync_content_from_data_input.py posts
python3 scripts/sync_content_from_data_input.py events
python3 scripts/sync_content_from_data_input.py publications
```

首页、课题组介绍、应用产品和联系页等非结构化页面直接在 `content/` 中维护。

## 本地预览与构建

```bash
hugo server
```

提交前执行正式构建：

```bash
hugo --minify --cleanDestinationDir
```

构建产物位于 `public/`。`resources/_gen/` 是 Hugo 生成的资源缓存，两者都不应手工编辑。

## 发布

TransportX Agent 使用文档部署在 `/application/transportx-agent/guide/`，产品页的“快速上手”按钮直达 `#start`。唯一内容来源是 [`Ran2424/transportx-agent/docs/guide/`](https://github.com/Ran2424/transportx-agent/tree/main/docs/guide)。网站目录 `static/application/transportx-agent/guide/` 是部署副本，不直接维护内容。

每次网站发布前，工作流拉取产品仓库 `main` 中的最新 `docs/guide/`，同步全部文件并清除已删除的旧文件。脚本和样式按内容生成带哈希的文件名，并改写首页引用，避免更新后继续加载旧资源；历史哈希文件保留，供尚在缓存中的旧首页使用。工作流还会每小时自动运行一次（每小时第 17 分钟，GitHub 可能延迟）；推送产品文档到 GitHub 后无需再手工复制。没有变化时，发布 action 不会创建新的页面仓库提交。

需要立即同步时，在网站仓库 Actions 中手动运行 `web-deploy`，或执行：

```bash
gh workflow run gh-pages.yml --repo transportx-public/website-resource --ref main
```

本地预览未推送的产品文档，从网站仓库根目录执行：

```bash
python3 scripts/sync_transportx_guide.py "/Users/ran/WorkSpace/3 Code Project/pi-tau-traffic/docs/guide"
hugo server
```

同步脚本只复制文档，不修改内容；返回产品页的链接也在源目录维护。本地修改不会自动上传。正式发布读取 GitHub `main`，因此先将源目录的修改提交并推送。

推送 `main` 分支后，`.github/workflows/gh-pages.yml` 会构建站点，并将 `public/` 发布到 `transportx-public/transportx-public.github.io` 仓库。

项目组成与目录职责见 [`architecture.md`](architecture.md)。
