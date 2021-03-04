from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("mat", "123", "simulations/")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(('127.0.0.1', 21211), handler)
server.serve_forever()
