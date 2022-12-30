from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"

keys = [

    #################
    #  BASIC MOVES  #
    #################

    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),

    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow()
        ),

    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink()
        ),

    Key([mod, "control"], "Left", lazy.layout.grow_left()),
    Key([mod, "control"], "Right", lazy.layout.grow_right()),

    Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),

    Key([mod], "bar", lazy.spawn("python .config/qtile/toggle_between_screens.py")),
    Key([mod], "p", lazy.layout.flip()),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "space", lazy.window.toggle_floating()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "b", lazy.hide_show_bar("all")),


    ################
    #     APPS     #
    ################

    Key([mod], "m", lazy.spawn(".config/rofi/launchers/type-2/launcher.sh")),
    Key([mod], "e", lazy.spawn("thunar")),
    Key([mod], "Return", lazy.spawn("alacritty")),
    Key([mod], "s", lazy.spawn("mkdir -p Screenshots"),
        lazy.spawn("scrot -u Screenshots/%Y-%m-%d-%H-%M-%S.png")
        ),
    Key([mod, "shift"], "s", lazy.spawn("mkdir -p Screenshots"),
        lazy.spawn("scrot -s Screenshots/%Y-%m-%d-%H-%M-%S.png --line mode=edge")),

    ################
    # SPECIAL KEYS #
    ################

    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]
