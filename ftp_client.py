from glob import glob
from ftpretty import ftpretty
import os
import env_var

f = ftpretty(
    env_var.FTP_SERVER_IP,
    *env_var.FTP_SERVER_USER_CREDENTIALS,
    port=env_var.FTP_SERVER_PORT,
)
