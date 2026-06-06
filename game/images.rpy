# 图像定义
# 素材目录：game/images/{bg,characters,cg}/
# 上传对应 PNG 后自动生效；未上传时使用纯色占位

# ── 背景 ──────────────────────────────────────────
# game/images/bg/bg_research_ruins.png
# game/images/bg/bg_town.png
# game/images/bg/bg_clocktower.png
# game/images/bg/bg_wetland.png

image bg research_ruins = ConditionSwitch(
    "renpy.loadable('images/bg/bg_research_ruins.png')", "images/bg/bg_research_ruins.png",
    "True", Solid("#1e2a3a"),
)

image bg town = ConditionSwitch(
    "renpy.loadable('images/bg/bg_town.png')", "images/bg/bg_town.png",
    "True", Solid("#2a3a2e"),
)

image bg clocktower = ConditionSwitch(
    "renpy.loadable('images/bg/bg_clocktower.png')", "images/bg/bg_clocktower.png",
    "True", Solid("#2e2a3a"),
)

image bg wetland = ConditionSwitch(
    "renpy.loadable('images/bg/bg_wetland.png')", "images/bg/bg_wetland.png",
    "True", Solid("#1a2e2e"),
)

image bg wasteland = Solid("#1a1a2e")

# ── 角色立绘 ──────────────────────────────────────
# game/images/characters/xia_normal.png
# game/images/characters/xia_happy.png
# game/images/characters/xia_serious.png
# game/images/characters/alo_normal.png
# game/images/characters/qinghe_normal.png  （待上传）
# game/images/characters/suli_normal.png    （待上传）
# game/images/characters/yehan_normal.png   （待上传）

image xia normal = ConditionSwitch(
    "renpy.loadable('images/characters/xia_normal.png')", "images/characters/xia_normal.png",
    "True", Solid("#3a2a2a", xsize=400, ysize=800),
)

image xia happy = ConditionSwitch(
    "renpy.loadable('images/characters/xia_happy.png')", "images/characters/xia_happy.png",
    "True", Solid("#3a3a2a", xsize=400, ysize=800),
)

image xia serious = ConditionSwitch(
    "renpy.loadable('images/characters/xia_serious.png')", "images/characters/xia_serious.png",
    "True", Solid("#2a2a3a", xsize=400, ysize=800),
)

image alo normal = ConditionSwitch(
    "renpy.loadable('images/characters/alo_normal.png')", "images/characters/alo_normal.png",
    "True", Solid("#2a3a3a", xsize=400, ysize=800),
)

image qinghe normal = ConditionSwitch(
    "renpy.loadable('images/characters/qinghe_normal.png')", "images/characters/qinghe_normal.png",
    "True", Solid("#2a3a2e", xsize=400, ysize=800),
)

image suli normal = ConditionSwitch(
    "renpy.loadable('images/characters/suli_normal.png')", "images/characters/suli_normal.png",
    "True", Solid("#3a2e3a", xsize=400, ysize=800),
)

image yehan normal = ConditionSwitch(
    "renpy.loadable('images/characters/yehan_normal.png')", "images/characters/yehan_normal.png",
    "True", Solid("#2e2a2a", xsize=400, ysize=800),
)

# ── CG ────────────────────────────────────────────
# game/images/cg/cg_last_medicine.png
# game/images/cg/cg_qinghe_teaser.png

image cg last_medicine = ConditionSwitch(
    "renpy.loadable('images/cg/cg_last_medicine.png')", "images/cg/cg_last_medicine.png",
    "True", Solid("#1a1a2e"),
)

image cg qinghe_teaser = ConditionSwitch(
    "renpy.loadable('images/cg/cg_qinghe_teaser.png')", "images/cg/cg_qinghe_teaser.png",
    "True", Solid("#1e1e2e"),
)
