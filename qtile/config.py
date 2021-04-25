from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import datetime

now = str(datetime.datetime.now()).replace(" ", "_")


mod = "mod4"
terminal = guess_terminal()

keys = [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),

    # Change window sizes (MonadTall)
    Key([mod, "control"], "Up", lazy.layout.grow()),
    Key([mod, "control"], "Down", lazy.layout.shrink()),

    # Move windows up or down in current stack
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    Key([mod], "w", lazy.window.kill()),

    # Restart Qtile
    Key([mod, "control"], "r", lazy.restart()),

    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    Key([mod], "m", lazy.spawn("rofi -show drun")),

    # Window Nav
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    Key([mod], "b", lazy.spawn("google-chrome-stable")),

    # File Explorer
    Key([mod], "e", lazy.spawn("thunar")),

    # Terminal
    Key([mod], "Return", lazy.spawn("alacritty")),

    # ------------ Hardware Configs ------------

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),


    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # Screenshot
    Key([mod], "s", lazy.spawn("scrot -s /home/bestian/Imágenes/screenshots/" + str(now) + ".png")),

]

groups = [Group(i) for i in ["     ", "    ", "  ﭮ  ", "    ", "    "]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

layout_conf = {
    "border_focus": "#18dcff",
    "border_width": 2,
    "margin": 13
}

layouts = [
    layout.MonadTall(**layout_conf),
    # layout.Tile(**layout_conf),
    # layout.MonadWide(**layout_conf),
    # layout.Bsp(),
    layout.Max(),
    # layout.Zoomy(**layout_conf),

    # layout.Columns(border_focus_stack='#d75f5f'),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=3),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
]

widget_defaults = dict(
    font='Mononoki Nerd Font',
    fontsize=17,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    foreground=["#2f3542", "#2f3542"],
                    background=["#57606f", "#57606f"],
                    font='Mononoki Nerd Font',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=["#ffffff", "#ffffff"],
                    inactive=["#ffffff", "#ffffff"],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border=['#ff4757', "#ff4757"],
                    this_current_screen_border=["#2d3436", "#2d3436"],
                    this_screen_border=["#2d3436", "#2d3436"],
                    other_current_screen_border=["#2d3436", "#2d3436"],
                    other_screen_border=["#2d3436", "#2d3436"],
                    disable_drag=True
                ),
                #widget.Prompt(),
                widget.WindowName(
                    foreground=["#ffffff", "#ffffff"],
                    background=["#2f3542", "#2f3542"],
                    font="Mononoki Nerd Font",
                    padding=20,
                ),
                widget.TextBox(
                    text="", # Icon: nf-oct-triangle_left
                    fontsize=17,
                    padding=10,
                    foreground=["#ffffff", "#ffffff"],
                    background=["#2f3542", "#2f3542"],
                ),
                widget.CurrentLayout(
                    foreground=["#ffffff", "#ffffff"],
                    background=["#2f3542", "#2f3542"],
                    padding=10),
                widget.TextBox(
                    text="", # Icon: nf-oct-triangle_left
                    fontsize=17,
                    padding=10,
                    foreground=["#ffffff", "#ffffff"],
                    background=["#2f3542", "#2f3542"],
                ),    
                widget.Systray(
                    background=["#2f3542", "#2f3542"],
                    foreground=["#ffffff", "#ffffff"],
                    padding=10,
                    ),
                widget.TextBox(
                    text="", # Icon: nf-oct-triangle_left
                    fontsize=17,
                    padding=10,
                    foreground=["#ffffff", "#ffffff"],
                    background=["#2f3542", "#2f3542"],
                ),
                widget.Clock(
                    background=["#2f3542", "#2f3542"],
                    foreground=["#ffffff", "#ffffff"],
                    format="%d/%m/%Y - %H:%M",
                    padding=10
                ),
            ],
            24,
            opacity=0.9
        ),
    ),
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    foreground=["#2f3542", "#2f3542"],
                    background=["#57606f", "#57606f"],
                    font='Mononoki Nerd Font',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=["#ffffff", "#ffffff"],
                    inactive=["#ffffff", "#ffffff"],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border=['#ff4757', "#ff4757"],
                    this_current_screen_border=["#2d3436", "#2d3436"],
                    this_screen_border=["#2d3436", "#2d3436"],
                    other_current_screen_border=["#2d3436", "#2d3436"],
                    other_screen_border=["#2d3436", "#2d3436"],
                    disable_drag=True
                ),
                #widget.Prompt(),
                widget.WindowName(
                    foreground=["#ffffff", "#ffffff"],
                    background=["#2f3542", "#2f3542"],
                    font="Mononoki Nerd Font",
                    padding=20,
                ),
                widget.TextBox(
                    text="", # Icon: nf-oct-triangle_left
                    fontsize=17,
                    padding=10,
                    foreground=["#ffffff", "#ffffff"],
                    background=["#2f3542", "#2f3542"],
                ),
                widget.CurrentLayout(
                    foreground=["#ffffff", "#ffffff"],
                    background=["#2f3542", "#2f3542"],
                    padding=10),
                widget.TextBox(
                    text="", # Icon: nf-oct-triangle_left
                    fontsize=17,
                    padding=10,
                    foreground=["#ffffff", "#ffffff"],
                    background=["#2f3542", "#2f3542"],
                ),
            ],
            24,
            opacity=0.9
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.toggle_floating())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"
