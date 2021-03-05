from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("mat", "123", "simulations/", perm='elradfmwM')
authorizer.add_user("mat2", "123", "simulations/", perm='elradfmwM')

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(('127.0.0.1', 21211), handler)
server.max_cons = 256
server.max_cons_per_ip = 5
server.serve_forever()
