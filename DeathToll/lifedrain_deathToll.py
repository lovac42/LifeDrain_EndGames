# -*- coding: utf-8 -*-
# Copyright: (C) 2018 Lovac42
# Support: https://github.com/lovac42/LifeDrain_EndGames
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.2


import sys, random
from anki.hooks import addHook, runHook


death_toll=random.randint(3,5)

def timesUp():
    global death_toll
    death_toll-=1
    if not death_toll:
        sys.exit()
    runHook('LifeDrain.recovery', 100)

addHook('LifeDrain.gameOver',timesUp)
