# News/Post Input

维护文件：

- `posts.xlsx`: News 信息表。
- `pictures/`: News 配图。Excel 的 `picture` 填这里的文件名。
- `markdown/`: News 正文 Markdown。Excel 的 `markdown_file` 填这里的文件名。

## Excel 字段

- `publish`: 是否发布。只有填 `TRUE`、`yes`、`1`、`是`、`发布` 的行会生成页面。
- `title`: News 标题，必填。
- `date`: 发布日期。推荐格式：`2025-03-19`。
- `summary`: 列表页短摘要。
- `authors`: 作者，多个用分号分隔。
- `tags`: 标签，多个用分号分隔。
- `featured`: 是否精选。填 `TRUE` 或留空。
- `picture`: 配图文件名，例如 `news-cover.jpg`。
- `caption`: 配图说明。
- `markdown_file`: 正文 Markdown 文件名，例如 `news.md`。
- `body`: 直接写在 Excel 里的正文，可选。若同时填了 `markdown_file`，优先使用 Markdown 文件。
- `slug`: 页面地址，可选。留空时脚本会用日期和标题自动生成。

同步命令：

```bash
python3 scripts/sync_content_from_data_input.py posts
```
