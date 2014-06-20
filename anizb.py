""" Main routine - just tests for libraries at this point"""
from flask import Flask
from lib.py3utils import Config
from lib.py3anidb import Anidb

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':    
#    app.run()
    config = Config()
    anizb = config.set_default('anizb', {
        'dbtype' : 'sqlite',
        'port' : '3306',
        'hostname' : 'localhost',
        'user' : 'anizb',
        'password' : 'none',
        'dbname' : 'anizb'})

    anidb = Anidb()
    titles = anidb.get_anime_titles_by_substring('One Piece')
    for title in titles:
        print(title.anidbid, title.title)
