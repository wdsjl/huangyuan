define config.name = _("荒原")
define config.version = "0.1.0"
define gui.show_name = True

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.main_menu_music = None

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

default preferences.text_cps = 0
default preferences.afm_time = 15

define config.save_directory = "wasteland"

define config.screen_width = 1920
define config.screen_height = 1080

define config.defer_styles = True

init python:
    config.developer = True
