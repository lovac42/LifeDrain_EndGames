# -*- coding: utf-8 -*-
# Copyright: (C) 2018 Lovac42
# Support: https://github.com/lovac42/LifeDrain_EndGames
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.3b


HP_RECOVER = 100


import sys, random
from anki.hooks import addHook, runHook
from aqt.utils import showCritical


death_toll=random.randint(3,5)

def timesUp():
    global death_toll
    death_toll-=1
    if not death_toll:
        showCritical("Death Toll Was Immeasurable...",
                        title="Goodbye Cruel World!")
        sys.exit()
    runHook('LifeDrain.recover',True,HP_RECOVER)

addHook('LifeDrain.gameOver',timesUp)
