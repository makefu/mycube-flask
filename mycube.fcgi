from flup.server.fcgi import WSGIServer
from mycube import app

if __name__ == '__main__':
    WSGIServer(app).run()
