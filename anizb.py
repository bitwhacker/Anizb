""" Main routine - just tests for libraries at this point"""
from flask import Flask
from lib.py3utils import Config
from lib.py3anidb import *

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':    
#    app.run()
    config = Config()
    anizb = config.get_section('anizb', {
        'dbtype' : 'sqlite',
        'port' : '3306',
        'hostname' : 'localhost',
        'user' : 'anizb',
        'password' : 'none',
        'dbname' : 'anizb'})
    anidb = config.get_section('anidb', {
        'dbtype' : 'sqlite',
        'port' : '3306',
        'hostname' : 'localhost',
        'user' : 'anidb',
        'password' : 'none',
        'dbname' : 'anidb'})
    model = AnidbModel()

    ts = TitleSearch()
#    ts.load_titles()
#    for title in m.get_titles():
#        print (title.anidbid, title.title, title.language, title.type)
    ts.search('One Piece')
