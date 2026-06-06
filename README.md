# 荒原（Wasteland）

剧情分支 AVG 游戏项目，基于 Ren'Py 8.x 开发。

## 仓库结构

```
├── docs/                  # 剧情与世界观文档（唯一事实源）
│   ├── World.md
│   ├── Characters.md
│   ├── Events.md
│   ├── Chapter01.md
│   └── Chapter02.md
│
├── game_design/           # 游戏设计文档
│   ├── GDD.md
│   ├── Systems.md
│   └── Endings.md
│
├── game/                  # 可运行的 Ren'Py 项目
│   ├── script.rpy
│   ├── options.rpy
│   ├── images.rpy
│   ├── systems/
│   ├── chapters/
│   └── images/
│
├── renpy/                 # Cursor 生成输出目录
│   ├── generated/
│   ├── systems/
│   └── ui/
│
├── assets/                # 美术与音频素材
│   ├── bg/
│   ├── characters/
│   ├── cg/
│   └── audio/
│
├── prompts/               # AI 生成 Prompt 模板
│   ├── backgrounds.md
│   ├── characters.md
│   ├── cg.md
│   └── chapter_generation.md
│
└── .cursor/rules/         # Cursor 开发规范
    └── renpy.mdc
```

## 开发流程

```
ChatGPT 生成剧情文档
        ↓
docs/ChapterXX.md（提交到 GitHub）
        ↓
Cursor 读取文档，生成 Ren'Py 脚本
        ↓
renpy/generated/chapterXX.rpy
        ↓
同步到 game/chapters/chapterXX.rpy
        ↓
Ren'Py Launcher 打开本项目根目录运行
```

## 快速开始

1. 安装 [Ren'Py 8.x](https://www.renpy.org/)
2. 用 Ren'Py Launcher 添加本项目根目录
3. 启动游戏

## 核心变量

### 人格四维

| 变量 | 含义 |
|------|------|
| `humanity` | 人性 |
| `logic` | 理性 |
| `authority` | 权威 |
| `transcendence` | 超越 |

### 好感度

| 变量 | 角色 |
|------|------|
| `xia_affection` | 林夏 |
| `qinghe_affection` | 顾青禾 |
| `suli_affection` | 苏璃 |
| `yehan_affection` | 叶寒 |

## 生成新章节

在 Cursor 中使用以下 Prompt：

```
根据 docs/Chapter01.md

生成完整 Ren'Py 脚本。

要求：
- 读取剧情内容
- 自动生成 scene、show、hide、menu
- 变量修改、角色对白、jump 结构

输出文件：renpy/generated/chapter01.rpy

不要解释。直接输出完整代码。
```

生成后将脚本同步到 `game/chapters/` 目录。

## 下一步

- [ ] 完善 `docs/World.md` 世界观
- [ ] 完善 `docs/Characters.md` 角色档案
- [ ] 完善 `docs/Events.md`（38 个关键事件树）
- [ ] 完成 `docs/Chapter01.md` 正式版剧情
- [ ] 替换占位背景与角色立绘素材
