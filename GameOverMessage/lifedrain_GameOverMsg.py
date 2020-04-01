# -*- coding: utf-8 -*-
# Copyright: (C) 2018 Lovac42
# Support: https://github.com/lovac42/LifeDrain_EndGames
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.6


# == User Config =========================================

#Don't show gameover screen util after the user grades the card.
WAIT_FOR_GRADE = True

# == End Config ==========================================
##########################################################

import os, re, random
from aqt import mw
from anki.hooks import addHook, runHook, remHook
from anki.sound import clearAudioQueue, play
from anki import version
ANKI21=version.startswith("2.1.")
CSS = None if ANKI21 else mw.sharedCSS

SND_EXT=re.compile(r'\.(?:mp[3a]|Flac|Ape|Ogg|Aac|Wma|Aiff?|au|wav)$', re.I)

RES_DIR = 'game_over_melody'
SND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), RES_DIR))
MELODY_LIST=[i for i in os.listdir(SND_DIR) if SND_EXT.search(i)]


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
    m=random.choice(MELODY_LIST)
    m=os.path.join(SND_DIR,m)
    play(m)

    mw.requireReset(True)
    mw.bottomWeb.hide()
    mw.web.stdHtml(ASCII_ART, css=CSS)
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
