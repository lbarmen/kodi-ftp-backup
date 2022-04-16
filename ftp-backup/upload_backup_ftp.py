from ftplib import FTP
from pathlib import Path
from datetime import date

today = date.today()
d1 = today.strftime("%Y%m%d")

file_path = Path('/storage/backup/'+d1+'050000.tar')

with FTP('192.168.1.1','login','pass') as ftp, open(file_path, 'rb') as file:
        ftp.storbinary(f'STOR /backup/rpi4/{file_path.name}', file)