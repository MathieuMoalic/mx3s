from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import env_var

authorizer = DummyAuthorizer()
authorizer.add_user(
    *env_var.FTP_SERVER_USER_CREDENTIALS, env_var.FTP_HOME_DIR, perm="elradfmwMT"
)

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", env_var.FTP_SERVER_PORT), handler)
server.serve_forever()