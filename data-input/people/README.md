# People Input

维护文件：

- `people.xlsx`: 人员信息表。
- `avatars/`: 头像图片。

## Excel 字段

- `Name`: 英文名，必填。会作为作者页面标题和文件夹名。
- `Name_Chinese`: 中文名。
- `picture`: 头像文件名，例如 `ao_wang.jpg`。文件必须放在 `avatars/`。
- `user_groups`: 身份类型，例如 `Ph.D`、`Master`。
- `is_gradiate`: 状态。当前兼容旧字段名，填 `Student` 或 `Graduate`。
- `enrollment_year`: 入学年份，例如 `2023`。
- `introduction`: 自我介绍。
- `Interests`: 研究兴趣。多个兴趣用英文分号、中文分号、逗号分隔均可。
- `email`: 邮箱。
- `Website`: 个人主页。
- `organizations`: 当前单位。
- `other information`: 备注信息。

同步命令：

```bash
/Users/ran/WorkSpace/SoftWare/miniconda3/envs/research/bin/python3.10 scripts/sync_content_from_data_input.py people
```
