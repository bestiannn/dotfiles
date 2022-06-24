from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy
from colors import colors

screens = [
    Screen(bottom=bar.Bar(
        [
            widget.TextBox(text="", font="Mononoki Nerd Font", fontsize=40, foreground=colors["black"], padding=0),
            widget.Spacer(length=10, background=colors["black"]),
            widget.TextBox(text="死", font="Cascadia Code", fontsize=20, foreground=colors["blue"], padding=0),
            widget.Spacer(length=30, background=colors["black"]),
            widget.WindowName(background=colors["black"], foreground=colors["white"], font="Cascadia Code", max_chars=50),
            widget.GroupBox(foreground=colors["black"],
                            background=colors["black"],
                            other_screen_border=colors["black"],
                            other_current_screen_border=colors["black"],
                            this_screen_border=colors["black"],
                            this_current_screen_border=colors["black"],
                            inactive=colors["gray"],
                            block_highlight_text_color=colors["pink"],
                            fontsize=25,
                            padding_x=20,
                            use_mouse_wheel=False,
                            font='Pixel Icons Compilation'),
            widget.Spacer(length=bar.STRETCH, background=colors["black"]),

            widget.Systray(padding=15,
                           icon_size=25),
            
            widget.Spacer(length=20),

            widget.TextBox(text="墳 ", font="Mononoki Nerd Font", fontsize=25, background=colors["black"], foreground=colors["white"]),
            widget.PulseVolume(background=colors["black"], font="Cascadia Code", fontsize=20, mouse_callbacks={'Button3': lazy.spawn('pavucontrol -t 4')}),
            widget.Spacer(length=15, background=colors["black"]),
            widget.Clock(background=colors["black"],
                         foreground=colors["white"],
                         format=" %d/%m/%Y   %H:%M",
                         font="Cascadia Code",
                         fontsize=20,
                         padding=10),
            widget.TextBox(text="", font="Mononoki Nerd Font", fontsize=40, foreground=colors["black"], padding=0),
        ],size=40, margin=[0, 90, 10, 90], background=colors["black"]),
        ),

    Screen(bottom=bar.Bar([
        widget.GroupBox(foreground=colors["black"],
                            background=colors["black"],
                            other_screen_border=colors["black"],
                            other_current_screen_border=colors["black"],
                            this_screen_border=colors["black"],
                            this_current_screen_border=colors["black"],
                            inactive=colors["gray"],
                            block_highlight_text_color=colors["pink"],
                            fontsize=25,
                            padding_x=20,
                            use_mouse_wheel=False,
                            font='Pixel Icons Compilation'),
        widget.Spacer(length=bar.STRETCH, background=colors["black"]),
    ],
        size=25,
        opacity=0.95), ),
]
