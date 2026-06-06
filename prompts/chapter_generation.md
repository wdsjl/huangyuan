# 章节生成 Prompt（固定模板）

根据 docs/Chapter01.md

生成完整 Ren'Py 脚本。

要求：

- 读取剧情内容
- 自动生成：scene、show、hide、menu
- 变量修改
- 角色对白
- jump 结构

输出文件：renpy/generated/chapter01.rpy

不要解释。直接输出完整代码。

---

使用时将 `Chapter01.md` 替换为对应章节文档，`chapter01.rpy` 替换为对应输出文件名。

生成后同步复制到 `game/chapters/` 以便 Ren'Py 直接运行。
