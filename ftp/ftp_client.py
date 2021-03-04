from ftpretty import ftpretty
import env_var

f = ftpretty(
    env_var.FTP_SERVER_IP,
    *env_var.FTP_SERVER_USER_CREDENTIALS,
    port=env_var.FTP_SERVER_PORT,
)
