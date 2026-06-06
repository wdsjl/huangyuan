# 好感度系统
# 变量定义见 personality.rpy

init python:
    def get_affection_level(value):
        if value >= 80:
            return "亲密"
        elif value >= 50:
            return "信任"
        elif value >= 20:
            return "友好"
        else:
            return "陌生"
