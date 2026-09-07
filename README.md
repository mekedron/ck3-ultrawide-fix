# Ultrawide Pause Menu Fix (CK3)

Fixes the in-game pause menu (Escape) being cut off vertically on ultrawide /
super-ultrawide displays such as 5120x1440.

## Where to get

[Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3797535808)
[Paradox](https://mods.paradoxplaza.com/mods/158317/Any)

## Cause

`game/gui/frontend_ingame_menu.gui` scales its content with

    scale = "[ScaleToFitElementOutside('(int32)1920', '(int32)1080')]"

`ScaleToFitElementOutside` is a "cover" fit: `max(width/1920, height/1080)`.
On 5120x1440 that is `max(2.67, 1.33) = 2.67`, so the ~830px tall menu column is
blown up to ~2200px and does not fit into 1440px of screen height.

Every other full-screen frontend layout (`frontend_main.gui`,
`frontend_bookmarks.gui`, `window_barbershop.gui`) uses `ScaleToFitElementInside`
instead - which is why the main menu looks fine and only the pause menu breaks.

## Fix

`gui/frontend_ingame_menu.gui` overrides the vanilla file with three changes to
the single outer widget:

* `ScaleToFitElementOutside` -> `ScaleToFitElementInside` (`min(w/1920, h/1080)` = 1.33x)
* `size = { 100% 100% }` -> `size = { 1920 1080 }`
* `parentanchor = left|vcenter` -> `parentanchor = center`

The last two mirror `frontend_main.gui`, so the menu column lands at the same
horizontal position as in the main menu instead of hugging the left screen edge.
The background art is a `background` block on the window itself and still covers
the whole screen.

## Layout

    descriptor.mod                    mod metadata (read from inside the mod dir)
    thumbnail.png                     Workshop preview image, must sit in the mod root
    gui/frontend_ingame_menu.gui      overrides game/gui/frontend_ingame_menu.gui
    install.sh                        copies the mod into the Proton prefix
    steam-workshop/                   Workshop listing texts and preview image

## Installing

Run `./install.sh`. It copies the mod into the CK3 mod directory **inside the Proton
prefix**:

    ~/.local/share/Steam/steamapps/compatdata/1158310/pfx/drive_c/users/steamuser/
      Documents/Paradox Interactive/Crusader Kings III/mod/

That is the path the game and the Paradox launcher actually use under Proton.
`~/.local/share/Paradox Interactive/Crusader Kings III` is the native-Linux
location and is *not* read by the Proton build - a mod placed there is invisible
to the launcher.

Close the launcher before installing, then start it and enable
"Ultrawide Pause Menu Fix" in the playset.

## Game version

Built against 1.19.0.6 (Scribe). GUI overrides fully replace the vanilla file, so
after a game patch re-diff `gui/frontend_ingame_menu.gui` against
`<steam>/Crusader Kings III/game/gui/frontend_ingame_menu.gui`.
