# 第一章：最后一支药剂
# 根据 docs/Chapter01.md 生成

label chapter01:

    scene bg research_ruins with dissolve

    "春末。"

    "荒原边缘。"

    "枯黄的草地间仍残留着零星绿色，远处乌云压低天空。"

    "曾经繁华的研究所如今只剩断裂的钢架，风吹过废墟，发出低沉的呜咽。"

    "二十年前，季节开始失控。"

    "春天越来越短，夏天越来越热，秋天带来疾病，冬天夺走生命。"

    "而人类最后的希望，是一种被称为「灵魂药剂」的东西。"

    # ── Scene 01：研究所废墟 ──

    mc "父亲曾经在这里工作……"

    "实验室早已被掠夺，只剩一间地下储藏室还未完全坍塌。"

    "你在角落发现一本笔记。"

    "\"如果你能看到这段话，说明我已经失败了。\""

    "\"药剂无法拯救所有人，但钥匙或许可以。\""

    "\"找到她们，找到四把钥匙，然后做出选择。\""

    $ _quest_keys = True

    "【获得主线任务：寻找四把钥匙】"

    # ── Scene 02：荒原小镇 ──

    scene bg town with dissolve

    "最近的聚居地正在发生骚乱。"

    "疫病爆发，镇上只剩最后一支灵魂药剂。"

    "居民围绕诊所争吵。"

    "\"我快死了！药剂应该给我！\""

    "\"我的孩子发烧三天了！\""

    "\"别吵了！只有一支！只有一支！\""

    scene cg last_medicine with dissolve

    alo "欢迎来到荒原。"

    alo "第一次见到这种场面？"

    mc "每天都会这样？"

    alo "每天。每个聚居地，都在决定谁活，谁死。"

    hide cg last_medicine with dissolve

    scene bg town

    menu:
        "交给生病的孩子":
            $ humanity += 2
            $ logic -= 1
            jump chapter01_choice_child

        "交给年迈老人":
            $ authority += 1
            $ humanity += 1
            jump chapter01_choice_elder

        "保留药剂寻找研究用途":
            $ logic += 2
            $ transcendence += 1
            $ future_research += 1
            jump chapter01_choice_research

label chapter01_choice_child:

    "孩子活了下来，母亲感激涕零。"

    "而那位老人，在当晚停止了呼吸。"

    jump chapter01_scene03

label chapter01_choice_elder:

    "老人得以续命，但孩子的病情每况愈下。"

    "小镇上开始弥漫不满的情绪。"

    jump chapter01_scene03

label chapter01_choice_research:

    "双方都没有得到药剂。"

    "但你保留了珍贵的研究样本。"

    jump chapter01_scene03

label chapter01_scene03:

    # ── Scene 03：钟楼避难所 ──

    scene bg clocktower with dissolve

    "夜晚，钟楼避难所。"

    alo "你知道为什么药剂这么少吗？"

    mc "生产失败？"

    alo "不。有人故意控制数量。"

    mc "谁？"

    alo "不知道。但你父亲一直在调查这件事。"

    "【获得线索：第一把钥匙可能位于湿地区域】"

    # ── Scene 04：湿地 ──

    scene bg wetland with dissolve

    "第二天清晨，春雨降临。"

    "空气中出现久违的青草气味，河流仍在流动。"

    show xia serious at center with dissolve

    xia "你踩到它们了。"

    mc "什么？"

    xia "刚发芽的新苗。它们比你更难活下来。"

    "林夏蹲下整理植物，动作十分轻柔。"

    mc "这里只有你一个人？"

    show xia normal

    xia "还有很多生命，只是你看不见。"

    mc "你认识我父亲？"

    show xia serious

    "林夏沉默，随后点头。"

    xia "他曾经想拯救世界。后来发现，世界并不想被拯救。"

    "【获得新目标：协助林夏调查湿地异常】"

    menu:
        "帮忙采集样本":
            $ xia_affection += 10
            $ humanity += 1
            jump chapter01_help_sample

        "优先寻找钥匙":
            $ xia_affection += 5
            $ logic += 1
            jump chapter01_find_key

label chapter01_help_sample:

    show xia happy

    xia "谢谢。这些数据很重要。"

    jump chapter01_scene05

label chapter01_find_key:

    show xia normal

    xia "……好吧。跟我来。"

    jump chapter01_scene05

label chapter01_scene05:

    # ── Scene 05：湿地深处 ──

    scene bg wetland

    show xia serious at center

    "你们在湿地深处发现大量异常植物。"

    "植物组织中检测出药剂成分——灵魂药剂可能并非人工制造，而是来源于自然。"

    xia "如果这是真的，整个世界都会被改变。"

    "在废弃观测站，你发现了父亲留下的录音。"

    "\"第一把钥匙已经苏醒。\""

    "\"不要相信任何单一路线。人类无法依靠一个答案存活。\""

    hide xia with dissolve

    # ── 章节结束 ──

    scene cg qinghe_teaser with dissolve

    "湿地之外，远方山谷中，一道实验室灯光亮起。"

    "一个陌生的身影，在窗前停驻片刻，随即隐入黑暗。"

    "【解锁角色档案：林夏】"
    "【解锁新区域：河谷实验站】"

    scene black with dissolve

    "第一章 · 完"

    "下一章：《进化之路》"

    return
