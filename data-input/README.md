# TransportX Website Data Input

这个目录是给非代码人员维护网站内容用的。原则是：

1. 在这里填 Excel、放图片、放 Markdown/PDF。
2. 运行同步脚本，把录入材料生成到 Hugo 的 `content/` 目录。
3. 本目录是“原始录入材料”，`content/` 是“网站源码内容”。

## 目录

- `people/`: 人员信息。维护 `people.xlsx` 和 `avatars/`。
- `posts/`: News/Post 信息。维护 `posts.xlsx`、`pictures/`、`markdown/`。
- `events/`: 活动信息。维护 `events.xlsx` 和 `pictures/`。
- `publications/`: 论文信息。维护 `publications.xlsx`、`pictures/`、`markdown/`、`pdfs/`。

## 常用命令

在仓库根目录运行：

```bash
python3 scripts/sync_content_from_data_input.py people
```

同步全部内容：

```bash
python3 scripts/sync_content_from_data_input.py
```

只同步某一类：

```bash
python3 scripts/sync_content_from_data_input.py events
python3 scripts/sync_content_from_data_input.py posts
python3 scripts/sync_content_from_data_input.py publications
```

同步后，用 Hugo 检查：

```bash
hugo --minify --cleanDestinationDir
```
