from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import logging

authorizer = DummyAuthorizer()
authorizer.add_user("client",
                    "client",
                    ".",
                    perm='elradfmwMT')

handler = FTPHandler
handler.banner = "pyftpdlib based ftpd ready."
handler.masquerade_address = '150.254.111.83'
handler.passive_ports = range(60000, 65535)
handler.use_sendfile = False
handler.authorizer = authorizer

logging.basicConfig(filename='/docker/ftp/pyftpd.log', level=logging.DEBUG)

# server = FTPServer(('172.24.0.1', 21211), handler)
server = FTPServer(('0.0.0.0', 21211), handler)
server.max_cons = 256
server.max_cons_per_ip = 5
server.serve_forever()
