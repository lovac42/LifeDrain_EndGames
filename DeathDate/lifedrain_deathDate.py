# -*- coding: utf-8 -*-
# Copyright: (C) 2018 Lovac42
# Support: https://github.com/lovac42/LifeDrain_EndGames
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.3


# == User Config =========================================

BIRTH_YEAR  = 2000
BIRTH_MONTH = 1
BIRTH_DATE  = 1

AVERAGE_LIFE_EXPECTANCY = 80 * 365

#Don't show gameover screen util after the user grades the card.
WAIT_FOR_GRADE = True

RESOLUTION = 30  #days per character

WIDTH = 300

# == End Config ==========================================
##########################################################

from aqt import mw
from anki.hooks import addHook, runHook, remHook
from datetime import date, datetime
from anki import version
ANKI21=version.startswith("2.1.")
CSS = None if ANKI21 else mw.sharedCSS

gameover=False
def checkState():
    global gameover
    if WAIT_FOR_GRADE and \
    mw.reviewer.state=='answer':
        gameover=True
        addHook('showQuestion',showMsg)
    else:
        showMsg()


def showMsg():
    mw.requireReset(True)
    mw.bottomWeb.hide()
    mw.web.stdHtml(getCal(), css=CSS)
    reset()


def reset():
    global gameover
    gameover=False
    remHook('showQuestion',showMsg)
    runHook('LifeDrain.recover',True,9999)


def getCal():
    birth = date(BIRTH_YEAR, BIRTH_MONTH, BIRTH_DATE)
    today = datetime.now().date()
    age = (today - birth).days//RESOLUTION
    life=AVERAGE_LIFE_EXPECTANCY//RESOLUTION - age
    cal="* "*age + "- "*(life)
    return """<center><h1>Life Graph</h1><br><br>
<div style="width:%dpx;">%s</div><br>
<i>The Clock Is Ticking...</i></center>"""%(WIDTH,cal)


def onAfterStateChange(newS,oldS,*args):
    if gameover: reset()


addHook('LifeDrain.gameOver',checkState)
addHook('afterStateChange',onAfterStateChange)
