#pip install -r requirements.txt --user
import app
import gevent
from gevent import monkey
monkey.patch_all()
web_scannerApp = app.software()

#Site web pour les tests :
"""crawler : https://qwant.com , xss : https://xss-game.appspot.com/level2/frame, sql :  http://challenge01.root-me.org/web-serveur/ch19/?action=recherche"""
 