# 立绘与画面定位
# 素材：背景 1536x1024，立绘 1024x1536，游戏 1920x1080

define SPRITE_ZOOM = 0.52
define SPRITE_YOFFSET = -285

transform sprite_left:
    zoom SPRITE_ZOOM
    xalign 0.22
    yalign 1.0
    yoffset SPRITE_YOFFSET

transform sprite_center:
    zoom SPRITE_ZOOM
    xalign 0.5
    yalign 1.0
    yoffset SPRITE_YOFFSET

transform sprite_right:
    zoom SPRITE_ZOOM
    xalign 0.78
    yalign 1.0
    yoffset SPRITE_YOFFSET

transform cg_overlay:
    fit "contain"
    xalign 0.5
    yalign 0.5
    xysize (1920, 1080)

transform cg_scene:
    fit "cover"
    xalign 0.5
    yalign 0.5
    xysize (1920, 1080)
