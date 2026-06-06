## 中文字体配置

define gui.text_font = "fonts/NotoSansSC-Regular.ttf"
define gui.name_text_font = "fonts/NotoSansSC-Regular.ttf"
define gui.interface_text_font = "fonts/NotoSansSC-Regular.ttf"
define gui.button_text_font = "fonts/NotoSansSC-Regular.ttf"
define gui.label_text_font = "fonts/NotoSansSC-Regular.ttf"
define gui.choice_button_text_font = "fonts/NotoSansSC-Regular.ttf"

init python:
    config.font_replacement_map["DejaVuSans.ttf"] = gui.text_font
    config.font_replacement_map["DejaVuSans-Bold.ttf"] = gui.text_font

style default:
    font gui.text_font

style say_dialogue:
    font gui.text_font

style say_label:
    font gui.name_text_font

style choice_button_text:
    font gui.choice_button_text_font
