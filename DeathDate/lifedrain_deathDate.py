# -*- coding: utf-8 -*-
# Copyright: (C) 2018 Lovac42
# Support: https://github.com/lovac42/LifeDrain_EndGames
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.1


# == User Config =========================================

BIRTH_YEAR  = 2000
BIRTH_MONTH = 1
BIRTH_DATE  = 1

AVERAGE_LIFE_EXPECTANCY = 80 * 365

#Don't show gameover screen util after the user grades the card.
WAIT_FOR_GRADE = True

# == End Config ==========================================
##########################################################

from aqt import mw
from anki.hooks import addHook, runHook, remHook
from datetime import date, datetime
from anki import version
ANKI21=version.startswith("2.1.")


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
    mw.web.stdHtml(getCal(),
        css='' if ANKI21 else mw.sharedCSS)
    reset()


def reset():
    global gameover
    gameover=False
    remHook('showQuestion',showMsg)
    runHook('LifeDrain.recover',True,9999)


def getCal():
    birth = date(BIRTH_YEAR, BIRTH_MONTH, BIRTH_DATE)
    today = datetime.now().date()
    age = (today - birth).days//30
    life=AVERAGE_LIFE_EXPECTANCY//30 - age
    cal="* "*age + "- "*(life)
    return """<center><h1>Life Graph</h1><br><br>
<div style="width:300px;">%s</div><br>
<i>The Clocks Are Ticking...</i></center>"""%cal


def onAfterStateChange(newS,oldS,*args):
    if gameover: reset()


addHook('LifeDrain.gameOver',checkState)
addHook('afterStateChange',onAfterStateChange)
