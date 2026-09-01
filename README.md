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

推送 `main` 分支后，`.github/workflows/gh-pages.yml` 会构建站点，并将 `public/` 发布到 `transportx-public/transportx-public.github.io` 仓库。

项目组成与目录职责见 [`architecture.md`](architecture.md)。
