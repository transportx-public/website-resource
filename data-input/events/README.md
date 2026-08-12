# Events Input

`events.xlsx` 保存课题组文献分享记录。每一行是一篇文献，生成脚本按照 `日期` 聚合，同一天的记录生成一个组会 Event。

## Excel 字段

- `名称`: 文献标题，必填。
- `序号`: 文献分享记录的全局顺序，必填。
- `汇报人`: 文献分享成员，必填。姓名需要能够映射到网站 People 页面。
- `日期`: 组会日期，必填。推荐格式为 `2026-01-15`。
- `发布日期`: 文献发表年月，可留空。网站按 `YYYY-MM` 展示。
- `出处`: 期刊、会议或资料来源。
- `亮点`: 文献摘要或推荐理由，可留空。

可以在工作簿中增加以下可选字段：

- `原文链接`: 文献网页、DOI 或 PDF 链接。
- `文献分享PPT`: 该篇文献的阅读分享 PPT 链接。
- `组会PPT`: 本次组会的统一 PPT 链接。同一日期只需填写一次。
- `会议纪要`: 本次组会的会议纪要链接。同一日期只需填写一次。

生成后的 Event 不设置 `authors`，避免把文献分享成员误标为组会汇报人。成员会显示在各篇文献旁，并链接到 People 页面。

同步命令：

```bash
/Users/ran/WorkSpace/SoftWare/miniconda3/envs/research/bin/python3.10 scripts/sync_content_from_data_input.py events
```
