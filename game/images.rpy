# 图像定义 — 全部素材映射
# 背景裁切铺满 1920x1080，立绘由 transforms.rpy 控制位置

# ── 背景（cover 铺满屏幕，避免两侧黑边）──────────────────

image bg research_ruins = ConditionSwitch(
    "renpy.loadable('images/bg/bg_research_ruins.png')",
    Transform("images/bg/bg_research_ruins.png", fit="cover", xysize=(1920, 1080)),
    "True", Solid("#1e2a3a"),
)

image bg town = ConditionSwitch(
    "renpy.loadable('images/bg/bg_town.png')",
    Transform("images/bg/bg_town.png", fit="cover", xysize=(1920, 1080)),
    "True", Solid("#2a3a2e"),
)

image bg clocktower = ConditionSwitch(
    "renpy.loadable('images/bg/bg_clocktower.png')",
    Transform("images/bg/bg_clocktower.png", fit="cover", xysize=(1920, 1080)),
    "True", Solid("#2e2a3a"),
)

image bg wetland = ConditionSwitch(
    "renpy.loadable('images/bg/bg_wetland.png')",
    Transform("images/bg/bg_wetland.png", fit="cover", xysize=(1920, 1080)),
    "True", Solid("#1a2e2e"),
)

image bg wasteland = Solid("#1a1a2e")

# ── 角色立绘 ──────────────────────────────────────

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

image cg last_medicine = ConditionSwitch(
    "renpy.loadable('images/cg/cg_last_medicine.png')", "images/cg/cg_last_medicine.png",
    "True", Solid("#1a1a2e"),
)

image cg qinghe_teaser = ConditionSwitch(
    "renpy.loadable('images/cg/cg_qinghe_teaser.png')", "images/cg/cg_qinghe_teaser.png",
    "True", Solid("#1e1e2e"),
)
