# -*- coding: utf-8 -*-
# Copyright: (C) 2018 Lovac42
# Support: https://github.com/lovac42/LifeDrain_EndGames
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.4


import random
from aqt import mw
from anki.hooks import addHook, runHook, wrap
from anki import version
ANKI21 = version.startswith("2.1.")


MESSAGES=(
    "The Egg Is Done!",
    "Go Take A Break!",
    "Another Tomato Picked!"
)

TOMATO_ASCII="""<center><h1>%s</h1>
<pre id="teaPic">
  ,d                                               ,d                
  88                                               88                
MM88MMM ,adPPYba,  88,dPYba,,adPYba,  ,adPPYYba, MM88MMM ,adPPYba,   
  88   a8"     "8a 88P'   "88"    "8a ""     `Y8   88   a8"     "8a  
  88   8b       d8 88      88      88 ,adPPPPP88   88   8b       d8  
  88,  "8a,   ,a8" 88      88      88 88,    ,88   88,  "8a,   ,a8"  
  "Y888 `"YbbdP"'  88      88      88 `"8bbdP"Y8   "Y888 `"YbbdP"'   

                   ,               
                  /.\              
                 //_`\             
            _.-`| \ ``._           
        .-''`-.       _.'`.        
      .'      / /'\/`.\    `.      
     /   .    |/         `.  \     
    '   /                  \  ;    
   :   '            \       : :    
   ;  ;             ;      /  .    
    ' :             .     '  /     
     \ \           /       .'      
 LGB  `.`        .'      .'        
        `-..___....----`           
</pre><br><br>
<h1 id="teatime"></h1></center>
<script>
var tmCnt=%s
var e=document.getElementById("teatime");
window.setInterval(function(){
 e.innerText=tmCnt;
 tmCnt--
 if(tmCnt==0) alert('Break Over!');
},1000);
</script>"""


pomodoros=0
def pomodoroTimer():
    global pomodoros
    did=mw.col.decks.selected()
    conf=mw.col.decks.confForDid(did)

    pomodoros+=1
    if pomodoros==4:
        pomodoros=0
        time=conf.get("PomodoroLongBreak", 0)*60
        msg="You've Got Ketchup!"
    else:
        time=conf.get("PomodoroShortBreak", 0)*60
        msg=random.choice(MESSAGES)

    #Off mode
    if not time: return

    #Display
    mw.requireReset(True)
    mw.bottomWeb.hide()
    mw.web.stdHtml(TOMATO_ASCII%(msg,time),
            css='' if ANKI21 else mw.sharedCSS)

    runHook('LifeDrain.recovery',9999)

addHook('LifeDrain.gameOver',pomodoroTimer)


########################################################
#  GUI stuff, adds deck menu options to enable/disable
########################################################

import aqt
import aqt.deckconf
from aqt.qt import *

from anki import version
ANKI21 = version.startswith("2.1.")
if ANKI21:
    from PyQt5 import QtCore, QtGui, QtWidgets
else:
    from PyQt4 import QtCore, QtGui as QtWidgets


def dconfsetupUi(self, Dialog):
    r=self.lifeDrainLayout.rowCount()

    #Short Breaks
    self.lblPomodoroSB = QtWidgets.QLabel(self.tab_3)
    self.lblPomodoroSB.setText(_("Pomodoro Short Break:"))
    self.lifeDrainLayout.addWidget(self.lblPomodoroSB, r, 0, 1, 1)
    self.valPomodoroSB = QtWidgets.QSpinBox(self.tab_3)
    self.valPomodoroSB.setMinimum(0)
    self.valPomodoroSB.setMaximum(30)
    self.valPomodoroSB.setSingleStep(1)
    self.lifeDrainLayout.addWidget(self.valPomodoroSB, r, 1, 1, 1)
    r+=1

    #Long Breaks
    self.lblPomodoroLB = QtWidgets.QLabel(self.tab_3)
    self.lblPomodoroLB.setText(_("Pomodoro Long Break:"))
    self.lifeDrainLayout.addWidget(self.lblPomodoroLB, r, 0, 1, 1)
    self.valPomodoroLB = QtWidgets.QSpinBox(self.tab_3)
    self.valPomodoroLB.setMinimum(0)
    self.valPomodoroLB.setMaximum(60)
    self.valPomodoroLB.setSingleStep(5)
    self.lifeDrainLayout.addWidget(self.valPomodoroLB, r, 1, 1, 1)


def loadConf(self):
    i=self.conf.get("PomodoroShortBreak", 0)
    self.form.valPomodoroSB.setValue(i)
    i=self.conf.get("PomodoroLongBreak", 0)
    self.form.valPomodoroLB.setValue(i)

def saveConf(self):
    self.conf['PomodoroShortBreak']=self.form.valPomodoroSB.value()
    self.conf['PomodoroLongBreak']=self.form.valPomodoroLB.value()


def ui_wrap():
    aqt.forms.dconf.Ui_Dialog.setupUi = wrap(aqt.forms.dconf.Ui_Dialog.setupUi, dconfsetupUi, pos="after")
    aqt.deckconf.DeckConf.loadConf = wrap(aqt.deckconf.DeckConf.loadConf, loadConf, pos="after")
    aqt.deckconf.DeckConf.saveConf = wrap(aqt.deckconf.DeckConf.saveConf, saveConf, pos="before")
addHook('profileLoaded', ui_wrap)

