# -*- coding: utf-8 -*-
# Copyright: (C) 2018 Lovac42
# Support: https://github.com/lovac42/LifeDrain_EndGames
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.4


# == User Config =========================================

#Don't show gameover screen util after the user grades the card.
WAIT_FOR_GRADE = True

# == End Config ==========================================
##########################################################

import os
from aqt import mw
from anki.hooks import addHook, runHook, remHook
from anki.sound import clearAudioQueue, play
from anki import version
ANKI21=version.startswith("2.1.")

MOD_ABS,_ = os.path.split(__file__)
ENDING_MELODY=os.path.join(MOD_ABS,'135831__davidbain__end-game-fail.mp3')


ASCII_ART="""<center><h1>GAME OVER</h1><br><br><pre>
, ,    ,      ,    ,     ,     ,   ,      ,     ,     ,      ,      ,    
,       ,     ,    ,       ,   .____. ,   ,     ,      ,       ,      ,  
 ,    ,   ,    ,     ,   ,   , |   :|         ,   , ,   ,   ,       ,    
   ,        ,    ,     ,     __|====|__ ||||||  ,        ,      ,      , 
 ,   ,    ,   ,     ,    , *  / o  o \  ||||||,   ,  ,        ,    ,     
          .      ,    ,     * | -=   |  \====/ ,       ,   ,    ,     ,  
   ,     -|-     ,   ,     , U==\__//__. \\//    ,  ,        ,    ,      
          |  ,        ,  ,   / \\==// \ \ ||  ,   ,      ,          ,    
   ,  .-'~~~`-. ,  ,       ,|    o ||  | \||   ,      ,     ,   ,     ,  
 ,  .'   ,     `.  ,    ,   |    o ""  |\_|B),    ,  ,    ,       ,      
    |  R  I  P  | ,   ,    , \__  --__/   ||  ,        ,      ,     ,    
 ,  |   ,    ,  |  ,     ,  /          \  ||,   ,   ,      ,    ,    ,   
    |      ,    |    ,     |            | ||      ,  ,   ,    ,   ,      
  \\|  ,      , |//   ,   ,|            | || ,  ,  ,   ,   ,     ,  ,    
 ------_____---------____---\__ --_  __/__LJ__---------________-----___  
</pre></center>"""


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
    clearAudioQueue()
    mw.requireReset(True)
    play(ENDING_MELODY)
    mw.bottomWeb.hide()
    mw.web.stdHtml(ASCII_ART,
        css='' if ANKI21 else mw.sharedCSS)
    reset()


def reset():
    global gameover
    gameover=False
    remHook('showQuestion',showMsg)
    runHook('LifeDrain.recover',True,9999)


def onAfterStateChange(newS,oldS,*args):
    if gameover: reset()


addHook('LifeDrain.gameOver',checkState)
addHook('afterStateChange',onAfterStateChange)
