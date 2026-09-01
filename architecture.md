# 项目架构

TransportX 是一个无后端、无数据库的中英文静态网站。Hugo 负责构建，Hugo Blox 提供基础主题，仓库内的内容、模板、样式和脚本负责业务数据与页面定制。

## 构建链路

```text
data-input/（Excel、图片、Markdown、PDF）
                ↓ scripts/ 中的 Python 同步脚本
content/（结构化内容生成页 + 人工维护页）
                ↓ Hugo 读取 config/、layouts/、assets/、static/ 和主题模块
public/（完整静态站点）
                ↓ main 分支触发 GitHub Actions
GitHub Pages → transportxlab.com
```

## 目录树

```text
.
├── .github/
│   └── workflows/
│       └── gh-pages.yml                 # main 分支的构建与发布流程
├── assets/                              # 由 Hugo Pipes 加工的前端资源
│   ├── js/
│   │   └── transportx-publications.js  # 论文列表搜索和筛选
│   ├── media/                           # 首页、介绍页等使用的站点图片
│   ├── scss/
│   │   └── template.scss               # 全站自定义样式
│   └── jsconfig.json                    # JavaScript 编辑器配置
├── config/
│   └── _default/
│       ├── hugo.yaml                    # 域名、语言默认值、链接和构建规则
│       ├── languages.yaml               # 中英文信息及各语言导航菜单
│       ├── menus.yaml                   # 菜单兼容说明；实际菜单在 languages.yaml
│       ├── module.yaml                  # Hugo Blox 和插件模块
│       └── params.yaml                  # 外观、页头页脚、搜索、SEO 等站点参数
├── content/                             # Hugo 页面内容
│   ├── _index.md / _index.zh.md         # 中英文首页
│   ├── admin/index.md                   # Decap CMS 管理入口配置页
│   ├── application/                     # 应用产品列表及详情页
│   │   ├── _index.md / _index.zh.md
│   │   └── <product>/                   # 单个产品的页面与配图
│   ├── authors/<name>/                  # 成员资料；由 people.xlsx 生成
│   │   ├── _index.md / _index.zh.md
│   │   └── avatar.*
│   ├── contact/                         # 中英文联系页
│   ├── event/                           # 活动列表与组会页面
│   │   ├── _index.md / _index.zh.md
│   │   └── group-meeting-<date>/        # 由 events.xlsx 按日期聚合生成
│   ├── people/                          # 中英文成员列表页
│   ├── post/                            # 新闻列表及新闻页面
│   │   ├── _index.md / _index.zh.md
│   │   └── <post>/                      # 正文、封面等页面资源
│   ├── publication/                     # 论文列表及论文详情页
│   │   ├── _index.md / _index.zh.md
│   │   └── <publication>/               # 元数据、正文、配图和 PDF
│   └── tour/                            # 中英文课题组介绍页
├── data-input/                          # 非代码维护者使用的结构化内容源
│   ├── README.md                        # 总体录入和同步说明
│   ├── people/
│   │   ├── people.xlsx                  # 成员信息主表
│   │   ├── avatars/                     # 成员头像原图
│   │   └── README.md                    # 成员字段说明
│   ├── posts/
│   │   ├── posts.xlsx                   # 新闻信息主表
│   │   ├── markdown/                    # 可选的新闻正文
│   │   ├── pictures/                    # 新闻封面原图
│   │   └── README.md                    # 新闻字段说明
│   ├── events/
│   │   ├── events.xlsx                  # 组会与文献分享主表
│   │   ├── pictures/                    # 预留的活动图片目录
│   │   └── README.md                    # 活动字段说明
│   └── publications/
│       ├── publications.xlsx            # 论文信息主表
│       ├── markdown/                    # 可选的论文补充正文
│       ├── pictures/                    # 论文配图原图
│       ├── pdfs/                        # 可选的论文 PDF
│       └── README.md                    # 论文字段说明
├── i18n/
│   ├── en.yaml                          # 英文模板文案
│   └── zh.yaml                          # 中文模板文案
├── images/                              # 仓库或主题展示图片，不是网站内容主入口
├── layouts/                             # 覆盖 Hugo Blox 的自定义模板
│   ├── application/single.html          # 应用产品详情页
│   ├── authors/list.html                # 成员详情及关联动态
│   ├── event/single.html                # 组会详情页
│   ├── landing/contact.html             # 联系页
│   ├── section/
│   │   ├── application.html             # 应用产品列表页
│   │   ├── event.html                   # 活动按年份分组列表
│   │   └── publication.html             # 论文搜索、分类和年份筛选页
│   └── partials/transportx/             # 站点内复用的局部组件
│       ├── event-list-item.html
│       ├── member-chip.html
│       └── publication-item.html
├── scripts/                             # Excel 到 Hugo 内容的同步工具
│   ├── sync_content_from_data_input.py  # 总入口，可同步全部或指定模块
│   ├── generate_authors_from_people.py  # people.xlsx → content/authors/
│   ├── generate_posts_from_xlsx.py      # posts.xlsx → content/post/
│   ├── generate_events_from_xlsx.py     # events.xlsx → content/event/
│   ├── generate_publications_from_xlsx.py # publications.xlsx → content/publication/
│   └── generate_language_variants.py    # 生成或规范化部分中英文页面
├── static/                              # 构建时原样复制到站点根目录
│   ├── CNAME                            # 自定义域名
│   ├── .nojekyll                        # 禁用 GitHub Pages 的 Jekyll 处理
│   └── uploads/                         # CMS 上传目录占位
├── public/                              # Hugo 最终构建产物和发布目录
├── resources/_gen/                      # Hugo 生成的图片与 SCSS 缓存
├── go.mod / go.sum                      # Hugo 模块依赖及版本锁定
├── netlify.toml                         # 保留的 Netlify 构建配置
├── theme.toml                           # 上游主题元数据
├── preview.png                          # 仓库预览图
├── README.md                            # 使用、维护、构建和发布入口
├── architecture.md                      # 本架构说明
└── LICENSE.md                           # 项目许可证
```

目录树中的 `<name>`、`<date>`、`<post>` 等表示同类页面目录，不代表真实文件名。

## 内容层

### 结构化内容

四类结构化内容以 `data-input/` 为数据源，`content/` 中的对应页面是同步结果：

| 数据源 | 生成脚本 | 输出位置 | 生成行为 |
| --- | --- | --- | --- |
| `people/people.xlsx`、`avatars/` | `generate_authors_from_people.py` | `content/authors/<name>/` | 重新生成整个成员目录，并复制头像。 |
| `posts/posts.xlsx`、`markdown/`、`pictures/` | `generate_posts_from_xlsx.py` | `content/post/<slug>/` | 为标记发布的记录写入页面、正文和封面；不会自动清理已移除的旧目录。 |
| `events/events.xlsx` | `generate_events_from_xlsx.py` | `content/event/group-meeting-<date>/` | 按日期聚合文献记录；同步前清理已有的 `group-meeting-*` 目录。 |
| `publications/publications.xlsx` 及配套素材 | `generate_publications_from_xlsx.py` | `content/publication/<slug>/` | 为标记发布的记录写入元数据、正文、配图和 PDF；不会自动清理已移除的旧目录。 |

`sync_content_from_data_input.py` 是统一入口。未指定模块时依次同步 `people`、`posts`、`events` 和 `publications`，随后调用 `generate_language_variants.py`：

- 为成员页生成中文字段变体；
- 为组会页生成中英文标题与摘要变体；
- 为论文页补齐中文页面副本；
- 新闻页不由该脚本自动生成中文变体。

### 人工维护内容

以下内容不以 Excel 为主数据源，直接编辑 `content/`：

- `content/_index.*`：首页结构和内容；
- `content/tour/`：课题组介绍；
- `content/people/`：成员列表页的分组与排序；
- `content/contact/`：联系页；
- `content/application/`：应用产品列表和产品详情；
- 各内容类型的 `_index.*`：列表页标题、简介和展示参数。

## 展示层

Hugo 构建页面时按以下顺序组合资源：

1. `config/_default/` 定义站点、语言、菜单、主题模块和功能开关；
2. `content/` 提供页面 Front Matter、正文和页面包资源；
3. `layouts/` 覆盖 Hugo Blox 默认模板，决定页面结构；
4. `i18n/` 为模板中的按钮、标题和提示提供双语文案；
5. `assets/` 经 Hugo Pipes 编译、压缩和指纹化；
6. `static/` 不经处理，直接复制到输出目录。

页面模板之间通过 `layouts/partials/transportx/` 复用成员标签、活动条目和论文条目。论文列表模板还会加载 `assets/js/transportx-publications.js` 实现前端搜索与筛选。全站视觉调整集中在 `assets/scss/template.scss`。

## 页面与语言约定

- `index.md` 表示单个普通页面，`_index.md` 表示首页或栏目页。
- `.zh.md` 是中文版本；没有语言后缀的 Markdown 是默认英文版本。
- 页面专属图片、PDF 等资源与 `index.md` 放在同一个页面包目录。
- `featured.*` 通常作为列表封面，`avatar.*` 作为成员头像。
- 中英文导航统一在 `config/_default/languages.yaml` 中维护。

## 构建与发布

`hugo --minify --cleanDestinationDir` 会读取源码并重建 `public/`，图片转换和 SCSS 编译缓存写入 `resources/_gen/`。这两个目录都属于生成结果，不应手工修改。

推送 `main` 后，`.github/workflows/gh-pages.yml` 使用 Hugo Extended `0.134.1` 构建站点，并把 `public/` 发布到 `transportx-public/transportx-public.github.io` 仓库。`static/CNAME` 使发布站点通过 `transportxlab.com` 访问。

## 修改入口速查

| 需要修改的事项 | 首选位置 |
| --- | --- |
| 成员、新闻、组会或论文数据 | `data-input/<type>/`，随后运行同步脚本 |
| 首页或普通栏目正文 | `content/` 对应页面 |
| 页面布局或内容排列 | `layouts/` |
| 全站样式 | `assets/scss/template.scss` |
| 论文筛选交互 | `assets/js/transportx-publications.js` |
| 导航名称和顺序 | `config/_default/languages.yaml` |
| 域名、固定链接和构建选项 | `config/_default/hugo.yaml` |
| 主题模块 | `config/_default/module.yaml`、`go.mod` |
| 页头、页脚、搜索和 SEO | `config/_default/params.yaml` |
| 模板双语文案 | `i18n/en.yaml`、`i18n/zh.yaml` |
| 发布流程 | `.github/workflows/gh-pages.yml` |

## 维护边界

- 先修改数据源，再运行生成脚本；不要把生成页面当作长期维护入口。
- 修改模板、样式或配置时，不顺带改动内容数据。
- `public/` 和 `resources/_gen/` 可由 Hugo 重新生成，应视为产物而非源码。
- 同步脚本的覆盖范围不同；删除 Excel 记录后，应特别检查新闻和论文的旧页面目录是否仍需保留。
