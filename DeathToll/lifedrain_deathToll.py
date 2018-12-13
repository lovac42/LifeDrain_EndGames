# -*- coding: utf-8 -*-
# Copyright: (C) 2018 Lovac42
# Support: https://github.com/lovac42/LifeDrain_EndGames
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.4

# CONSTANTS:
BUTCHER=(1,1)
HARDCORE=(2,3)
NORMAL=(3,5)
WIMP=(5,9)

# == User Config =========================================

# LEVEL = BUTCHER
# LEVEL = HARDCORE
LEVEL = NORMAL
# LEVEL = WIMP

# == End Config ==========================================
##########################################################

import sys, random
from aqt import mw
from anki.hooks import addHook, runHook
from aqt.utils import showCritical
from anki import version
ANKI21 = version.startswith("2.1.")


death_toll=random.randint(LEVEL[0],LEVEL[1])
def timesUp():
    global death_toll
    death_toll-=1
    if not death_toll:
        showCritical("Death Toll Was Immeasurable...",
                        title="Goodbye Cruel World!")
        if ANKI21:
            mw.unloadProfileAndExit()
        else:
            sys.exit() #freezes on A21

    did=mw.col.decks.selected()
    conf=mw.col.decks.confForDid(did)
    hp_recover=conf.get('maxLife', 120)//2
    runHook('LifeDrain.recover',True,hp_recover)

addHook('LifeDrain.gameOver',timesUp)
