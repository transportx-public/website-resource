# Publications Input

维护文件：

- `publications.xlsx`: 论文信息表。
- `pictures/`: 论文配图。Excel 的 `picture` 填这里的文件名。
- `markdown/`: 论文详情补充正文。Excel 的 `markdown_file` 填这里的文件名。
- `pdfs/`: 论文 PDF。Excel 的 `pdf_file` 填这里的文件名。

## Excel 字段

当前 `publications.xlsx` 已支持这些基础字段：

- `publish`: 是否发布。只有填 `TRUE`、`yes`、`1`、`是`、`发布` 的行会生成页面。
- `title`: 论文标题，必填。
- `authors`: 作者，多个用分号分隔。
- `date`: 发表日期。推荐格式：`2025-03-15`。
- `doi`: DOI。
- `publication_types`: 分类，例如 `Publication in English`、`Publication in Chinese`。
- `publication`: 期刊、会议或项目来源。
- `abstract`: 摘要。
- `tags`: 标签，多个用分号分隔。

以后可以按需新增这些列：

- `summary`: 短摘要。
- `publication_short`: 期刊或会议简称。
- `featured`: 是否精选。填 `TRUE` 或留空。
- `picture`: 配图文件名，例如 `paper-cover.jpg`。
- `markdown_file`: 补充正文 Markdown 文件名，例如 `paper-note.md`。
- `pdf_file`: PDF 文件名，例如 `paper.pdf`。
- `url_pdf`, `url_code`, `url_dataset`, `url_poster`, `url_project`, `url_slides`, `url_source`, `url_video`: 外部链接。
- `caption`: 配图说明。
- `slides`: 关联 slides 名称。
- `slug`: 页面地址，可选。留空时脚本会用日期和标题自动生成。

同步命令：

```bash
python3 scripts/sync_content_from_data_input.py publications
```
