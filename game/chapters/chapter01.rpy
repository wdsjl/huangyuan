# Chapter01.rpy - 第一章完整脚本（更新版，含阿洛立绘）

label chapter01:

    ## Scene 01 - 研究所废墟
    scene bg research_ruins
    "风吹过研究所废墟。"
    "远处断裂的钢架在阴沉天空下显得格外荒凉。"

    mc "这里曾是父亲的实验室……如今只剩废墟。"
    "你找到了一本父亲留下的笔记。"
    $ player_has_note = True

    "任务已更新：寻找四把钥匙"

    ## Scene 02 - 荒原小镇 / 药剂事件
    scene bg town
    show alo normal at sprite_left
    show cg last_medicine at cg_overlay

    alo "欢迎来到荒原。第一次见到这种场面？"
    mc "每天都会这样？"
    alo "每天。每个聚居地都在决定谁活，谁死。"

    menu:
        "把药剂给生病的孩子":
            $ humanity += 2
            $ logic -= 1
            $ alo_affection += 5
            mc "孩子先得到药剂吧。"
            "孩子活了下来，母亲感激，老人遗憾死亡。"

        "把药剂给年迈老人":
            $ authority += 1
            $ humanity += 1
            mc "老人先吧。"
            "老人存活，孩子病情恶化，小镇出现不满。"

        "保留药剂用于研究":
            $ logic += 2
            $ transcendence += 1
            $ future_research += 1
            mc "暂时保留药剂。"
            "双方都没有得到药剂，研究数据保存。"

    hide cg last_medicine
    hide alo

    ## Scene 03 - 钟楼夜谈
    scene bg clocktower
    show alo normal at sprite_left

    alo "你知道为什么药剂这么少吗？"
    mc "生产失败？"
    alo "不。有人故意控制数量。"
    mc "谁？"
    alo "不知道。但你父亲一直在调查这件事。"

    hide alo

    "获得线索：第一把钥匙可能位于湿地区域。"

    ## Scene 04 - 湿地清晨
    scene bg wetland
    show xia normal at sprite_center

    "春雨轻洒湿地，河流缓缓流动，野花点缀四周。"

    xia "你踩到它们了。"
    mc "什么？"
    xia "刚发芽的新苗，它们比你更难活下来。"
    mc "这里只有你一个人吗？"
    xia "还有很多生命，只是你看不见。"
    mc "你认识我父亲？"
    xia "他曾经想拯救世界，后来发现……世界并不想被拯救。"

    "新目标已更新：协助林夏调查湿地异常"

    ## 第二个关键选择
    menu:
        "帮助林夏采集样本":
            $ xia_affection += 10
            $ humanity += 1
            mc "我来帮你采集样本。"
            "开启支线：湿地调查"

        "优先寻找钥匙":
            $ xia_affection += 5
            $ logic += 1
            mc "我先继续寻找钥匙。"

    ## Scene 05 - 湿地深处 / CG
    show xia happy at sprite_center
    "玩家发现大量异常植物，植物组织中检测出药剂成分。"
    xia "如果这是真的，整个世界都会被改变。"

    show xia serious at sprite_center
    "玩家在废弃观测站发现父亲留下的录音。"
    "录音：第一把钥匙已经苏醒。不要相信任何单一路线，人类无法依靠一个答案存活。"

    hide xia

    ## Chapter End - 顾青禾剪影
    scene cg qinghe_teaser at cg_scene
    "镜头拉远，湿地之外，远方山谷实验室灯光亮起。"
    "顾青禾剪影首次登场。"

    scene black with dissolve

    "第一章完。"
    return
