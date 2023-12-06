from filezilla import download_files
from filezilla_writer import upload_files
from modifier import modify_files

server="server"
username="username"
pasword="user_password"


domain_old="talismanmd.site"
domain_new="talismanmd.site"

replace_from="talismanmd.ru"
replace_to="talismanmd.site"

download_files(domain_old)
modify_files(replace_from,replace_to)
upload_files(domain_new)