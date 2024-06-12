 # Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess

from libqtile import hook

from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import ThermalSensor
from libqtile.widget import PulseVolume


mod = "mod4"
terminal = guess_terminal()


#Declrar varibles 
#Para color de la barra (Screen)
dispositivo_red = "wlan0"
color_barra =  "#282a36"
tamaño_barra = 28
tamaño_icono = 20
fuente_predetermindada = "Ubuntu Mono Nerd Font"
tamaño_fuente = 16
color_wd = "1a237e" #Blanco
color_ico = color_wd 
color_activo = "#f1fa8c" #Amarillo de iconos de pantalla
color_fg = "473463" # Azul gris - "#ffffff" - Blanco
color_bg = "#282a36" #Gris de la barra
color_inactivo = "#6272a4" #Azul pastel de iconos creo
color_oscuro = "#44475a" #Gris=Barra De cuando esta inactivo 
color_claro = "#bd93f9" #Purpura pastel de seleccion
color_urgent = "#ff5555" #Rojo pastel
color_texto1 = "#bd93f9" #Color del texto purpura
color_actualizaciones = "#bc0000" #Rojo
color_grupo1 = "f4d03f" #Naranja pastel	- "ff7f00" #Naranja
color_grupo2 = "#af7ac5" #"#d600f7"-Rosa oscuro
color_grupo3 = "48c9b0"	#Azul verdoso pastel- "#007bff" -Azul
color_grupo4 = "ff0066" #Rosa pastel - "#c60000"-rojo





#Espacio para definir las funciones

#Funcion para definir un separador
def fc_separador():
    return widget.Sep(
                    linewidth = 0,
                    padding = 6,
                    foreground = color_fg,
                    background = color_bg,
                )

#Funcion para dibujar el rectangulo de izquiera(0), y derecha (1)
def fc_rectangulo(vColor,tipo,color_bg_icon):
    if tipo == 0:
        icono ="" #nf-ple-left_half_circle_thick
    else:
        icono = "" #nf-ple-right_half_circle_thick
    return  widget.TextBox(
                    text = icono, #nf-ple-left_half_circle_thick
                    fontsize = tamaño_barra + 15,
                    foreground = vColor,
                    background = color_bg_icon #color_bg,
                    #padding = -3,
                )

#Funcion para escribir un texto o un icono 
def fc_icono(icono,color_grupo,color_ico):
    return widget.TextBox(
        text = icono,
        foreground = color_ico,
        background = color_grupo,
        fontsize = tamaño_icono,
    )


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),

    #teclas para lanzar menu rofi
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Abrir menu"),
    
    #teclas para lanzar firefox
    Key([mod], "d", lazy.spawn("firefox"), desc="Abrir Firefox"),
  

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    #Control volumen
    #key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    #key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    #key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    #Brillo de pantalla
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +2%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 2%-")),

    #Capturar Pantalla
    Key([mod], "s", lazy.spawn("scrot")),
    Key([mod, "shift"], "s", lazy.spawn("scrot -s")),


     
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


#Listado de iconos de Nerd Fonts
#1 : nf-linux-archlinux
#2 : nf-md-firefox
#3 : nf-md-git
#4 : nf-oct-file_directory_open_fill
#5 : nf-linux-kali_linux
#6 : nf-seti-hacklang
#7 : nf-oct-file_symlink_file
#8 : nf-md-image_filter_black_white
#9 : nf-md-resistor_nodes

groups = [Group(i) for i in[
    "  ","  "," 󰊢 ","  ","  ", "  ","  "," 󰋰 ","󰭅 ",
]]

for i, group in enumerate(groups):
    numeroEscritorio = str(i+1)
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                numeroEscritorio,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                numeroEscritorio,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    
    layout.Columns(
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=3,
        margin=4,
        border_focus="#bd93f9" #Color del texto purpura
    ),
    layout.Max(),
    # Otros layouts aquí
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


widget_defaults = dict(
    font=fuente_predetermindada,
    fontsize=tamaño_fuente,
    padding=1,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [                
                widget.GroupBox(
                    active=color_activo,
                    border_width = 1,
                    disable_drag = True,
                    fontsize = tamaño_icono,
                    foreground = color_fg,
                    highlight_method = "block",
                    inactive = color_inactivo,
                    margin_x = 0,
                    margin_y = 5,
                    other_current_screen_border = color_oscuro,
                    other_screen_border = color_oscuro,
                    padding_x = 0,
                    padding_y = 10,
                    this_current_screen_border = color_claro,
                    this_screen_border = color_claro,
                    urgent_alert_method = "block",
                    urgent_border = color_urgent,
                ),
                fc_separador (),
                widget.Prompt(),
                widget.WindowName(
                    foreground = color_texto1,
                    background = color_bg,
                ),

                #widget.Chord(
                #    chords_colors={
                #        "launch": ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                #),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),

                

                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),

                widget.Systray(
                    icon_size = tamaño_icono,
                    background = color_bg,
                ),
                fc_separador(),

                #Inicio grupo 1
                fc_rectangulo(color_grupo1,0,color_bg),
                fc_icono(" ", color_grupo1,color_ico), #nf-fa-thermometer
                widget.ThermalSensor(
                    foreground = color_fg,
                    background = color_grupo1,
                    threshold = 50,
                    tag_sensor = "Core 0",
                    fmt = 'T1:{}',
                ),

                #widget.ThermalSensor(
                #    foreground = color_fg,
                #    background = color_grupo1,
                #    threshold = 50,
                #    tag_sensor = "Core 1",
                #    fmt = 'T1:{}',
                #),

                fc_icono("  ", color_grupo1,color_ico),
                widget.Memory(
                    foreground = color_fg,
                    background = color_grupo1,
                ),
                #fc_rectangulo(color_grupo1, 1),
                #fc_separador(),
                #Fin grupo 1

                #Grupo 2
                fc_rectangulo(color_grupo2, 0,color_grupo1),
                fc_icono("󰁪 ", color_grupo2,"ffffff"), #nf-md-autorenew
                
                widget.CheckUpdates(
                    background = color_grupo2,
                    colour_have_update = color_actualizaciones,
                    colour_no_updates = "ffffff",#color_fg,
                    no_update_string = '0',
                    dispay_format = '{updates}',
                    update_interval = 1800,
                    distro='Arch_checkupdates',
                ),
                fc_icono(" 󰓅 ",color_grupo2,"ffffff"), #nf-md-speedometer
                widget.Net(
                    foreground = "ffffff", #color_fg,
                    background = color_grupo2,
                    format='{down:.0f}{down_suffix} 󰁅 󰁝 {up:.0f}{up_suffix}', #nf-md-arrow_down | nf-md-arrow_up
                    interface = dispositivo_red,
                    use_bits = 'true'
                ),

                #fc_rectangulo(color_grupo2, 1),
                #fc_separador(),
                #Fin Grupo 2

                #Inicio grupo 3
                fc_rectangulo(color_grupo3,0,color_grupo2),
                widget.Clock(
                    background = color_grupo3,
                    foreground = color_fg,
                    format="%d-%m-%Y %a %I:%M %p"
                ),
                #fc_icono(" ",color_grupo3), #nf-fa-volume_up
                #widget.PulseVolume(
                #    foreground = color_fg,
                #    background = color_grupo3,
                #    limit_max_volume = True,
                #    fontsize = tamaño_fuente,
                #),
                #fc_rectangulo(color_grupo3,1),
                #fc_separador(),
                #Fin grupo 3


                #Inicio grupo 4
                fc_rectangulo(color_grupo4,0,color_grupo3),
                widget.CurrentLayoutIcon(
                    background = color_grupo4,
                    scale = 0.6
                ),
                #widget.CurrentLayout(
                #    background = color_grupo4
                    
                #),

                #fc_rectangulo(color_grupo4,1),
                #fc_separador(),
                #Fin grupo 4

                
                #widget.QuickExit(),
                fc_separador(),
                
            ],
            tamaño_barra,
	        background=color_barra,
            
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,



        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([script])
    
widget.Battery(charge_char='⚡', discharge_char='', empty_char='❌', full_char='✔', format='{char} {percent:2.0%}', update_interval=5),
widget.Battery(charge_char='⚡', discharge_char='', empty_char='❌', full_char='✔', format='{char} {percent:2.0%}', update_interval=5),
widget.Battery(charge_char='⚡', discharge_char='', empty_char='❌', full_char='✔', format='{char} {percent:2.0%}', update_interval=5),
widget.Battery(charge_char='⚡', discharge_char='', empty_char='❌', full_char='✔', format='{char} {percent:2.0%}', update_interval=5),

fonts = [
    "sans",
    "monospace",
    "FontAwesome",
    "MaterialIcons-Regular"
    "Noto Color Emoji"
]

