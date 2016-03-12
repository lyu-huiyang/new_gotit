from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from toranado.ioloop import IOLoop
from config import app

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5000)
IOLoop.instance().start()
