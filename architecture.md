# 项目架构

TransportX 是一个无后端、无数据库的中英文静态网站。Hugo Blox 提供基础主题能力，仓库中的配置、模板和样式负责站点定制。

## 数据流

```text
data-input/（Excel、图片、Markdown、PDF）
                ↓ Python 同步脚本
content/（Hugo 内容）
                ↓ Hugo + config/ + layouts/ + assets/ + static/
public/（静态站点）
                ↓ GitHub Actions
GitHub Pages / transportxlab.com
```

人员、新闻、活动和论文以 `data-input/` 为主要维护入口；脚本将其转换为 Hugo 页面，并完成所需的中英文变体处理。首页、课题组介绍、应用产品和联系页等内容直接在 `content/` 中维护。

## 目录职责

| 目录 | 管理事项 |
| --- | --- |
| `.github/workflows/` | CI/CD；`main` 分支推送后构建并发布站点。 |
| `assets/` | 经 Hugo Pipes 处理的 SCSS、JavaScript 和站点媒体资源。 |
| `config/_default/` | Hugo 全局配置、语言、导航、主题模块及站点参数。 |
| `content/` | Hugo 页面内容；包含首页、成员、新闻、活动、论文、应用、介绍和联系页。部分内容由脚本生成。 |
| `data-input/` | 面向内容维护者的原始数据；按 `people`、`posts`、`events`、`publications` 分类保存 Excel 与配套素材。 |
| `i18n/` | 模板界面的中英文翻译文本。 |
| `images/` | 仓库说明与主题预览图片，不作为主要网站内容入口。 |
| `layouts/` | 覆盖 Hugo Blox 的页面模板与局部组件，负责成员、活动、论文和应用等页面的定制展示。 |
| `scripts/` | 将 `data-input/` 转换到 `content/`，并生成语言变体的 Python 脚本。总入口为 `sync_content_from_data_input.py`。 |
| `static/` | 构建时原样复制到站点根目录的文件，如 `CNAME`、`.nojekyll` 和上传目录。 |
| `public/` | Hugo 构建产物，也是发布目录；不要手工编辑。 |
| `resources/_gen/` | Hugo 生成的图片和样式缓存；不要手工编辑。 |

## 根目录文件

| 文件 | 作用 |
| --- | --- |
| `go.mod` / `go.sum` | 锁定 Hugo Blox 模块依赖。 |
| `theme.toml` | 主题元数据。 |
| `netlify.toml` | Netlify 构建配置；当前正式发布流程以 GitHub Actions 为准。 |
| `README.md` | 内容维护、构建与发布入口。 |
| `LICENSE.md` | 项目许可证。 |

## 维护边界

- 结构化内容先修改 `data-input/`，再运行同步脚本；不要在生成页面上做长期维护。
- 页面结构修改放在 `layouts/`，样式和脚本修改放在 `assets/`，站点级设置放在 `config/_default/`。
- `public/` 和 `resources/_gen/` 可由构建重新生成，应视为产物而非源文件。
