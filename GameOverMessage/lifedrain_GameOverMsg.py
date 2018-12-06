# -*- coding: utf-8 -*-
# Copyright: (C) 2018 Lovac42
# Support: https://github.com/lovac42/LifeDrain_EndGames
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Version: 0.0.2


from aqt import mw
from anki.hooks import addHook
from anki import version
ANKI21 = version.startswith("2.1.")


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


def msg():
    mw.requireReset(True)
    mw.bottomWeb.hide()
    mw.web.stdHtml(ASCII_ART,
        css='' if ANKI21 else mw.sharedCSS)

addHook('LifeDrain.gameOver',msg)
