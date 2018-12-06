# -*- coding: utf-8 -*-
# Copyright: (C) 2018 Lovac42
# Support: https://github.com/lovac42/LifeDrain_EndGames
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.2


# == User Config =========================================

BREAK_TIME=5*60

TEA_TIME=30*60

# == End Config ==========================================
##########################################################


import random
from aqt import mw
from anki.hooks import addHook, runHook
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
    pomodoros+=1
    if pomodoros==4:
        pomodoros=0
        time=TEA_TIME
        msg="You Got Ketchup!"
    else:
        time=BREAK_TIME
        msg=random.choice(MESSAGES)

    mw.moveToState("overview")
    mw.web.stdHtml(TOMATO_ASCII%(msg,time),
            css='' if ANKI21 else mw.sharedCSS)
    runHook('LifeDrain.recovery',9999)

addHook('LifeDrain.gameOver',pomodoroTimer)
