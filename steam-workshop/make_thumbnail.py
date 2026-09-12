#!/usr/bin/env python3
"""Rebuilds thumbnail.png (Workshop preview) and steam-workshop/thumbnail-200px.png (a
legibility check at Steam's listing size, not uploaded). Layout lives in thumbnail_layout.py.

Two F12 screenshots of the pause menu (Esc) at 5120x1440: vanilla, where the menu column is
scaled to the screen width and its top and bottom fall off the screen, and the same with
this mod. The crop is a tall window around the menu column; the halves sit side by side."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from thumbnail_layout import make_columns

OLD = "/home/nikita/Pictures/Screenshots/BEFORE_pause_menu.png"   # TODO: vanilla, menu cut off
NEW = "/home/nikita/Pictures/Screenshots/AFTER_pause_menu.png"    # TODO: with this mod
# 880x1440 windows centred on the menu column (x 2120..3000 of a 5120 wide screen)
CROP_OLD = (2120, 0, 3000, 1440)
CROP_NEW = (2120, 0, 3000, 1440)
OUT = os.path.join(os.path.dirname(__file__), "..", "thumbnail.png")
make_columns(OUT, "PAUSE MENU FIX", OLD, NEW, CROP_OLD, CROP_NEW, sub="ULTRAWIDE 32:9")
