# 由 Cursor 根据 docs/Chapter01.md 自动生成
# 当前为占位脚本，待正式剧情文档完成后重新生成

label chapter01:

    scene bg wasteland

    "荒原之上，风声如刀。"

    mc "这里是哪里……"

    menu:
        "向前探索":
            $ humanity += 2
            jump chapter01_explore

        "原地观察":
            $ logic += 2
            jump chapter01_observe

label chapter01_explore:

    "你迈出脚步，脚下的沙砾发出细碎的声响。"

    jump chapter01_end

label chapter01_observe:

    "你蹲下身，仔细观察周围的地形与痕迹。"

    jump chapter01_end

label chapter01_end:

    "第一章，待续。"

    return
