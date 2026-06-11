# Events Input

维护文件：

- `events.xlsx`: 活动信息表。
- `pictures/`: 活动配图。

## Excel 字段

- `publish`: 是否发布。只有填 `TRUE`、`yes`、`1`、`是`、`发布` 的行会生成页面。
- `title`: 活动标题，必填。
- `event`: 活动类型或系列名，例如 `Seminar`。
- `location`: 地点。
- `date`: 开始时间，必填。推荐格式：`2026-01-15 14:00`。
- `date_end`: 结束时间。推荐格式：`2026-01-15 16:00`。
- `all_day`: 是否全天活动。填 `TRUE` 或留空。
- `summary`: 列表页摘要。
- `abstract`: 详情页摘要。
- `authors`: 相关人员，多个用分号分隔。
- `tags`: 标签，多个用分号分隔。
- `featured`: 是否精选。填 `TRUE` 或留空。
- `picture`: 配图文件名，例如 `seminar.jpg`。文件放在 `pictures/`。
- `caption`: 图片说明。
- `body`: 详情页正文，可写 Markdown。
- `slug`: 页面地址，可选。留空时脚本会用日期和标题自动生成。

同步命令：

```bash
/Users/ran/WorkSpace/SoftWare/miniconda3/envs/research/bin/python3.10 scripts/sync_content_from_data_input.py events
```
