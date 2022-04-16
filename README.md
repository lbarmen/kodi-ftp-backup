# kodi-ftp-backup
python 3 matrix kodi backup ftp

add to cron 
ssh: crontab -e
add
00 5 * * * /storage/ftp-backup/backup_kodi.sh > /dev/null 2>&1
05 5 * * * /usr/bin/python3 /storage/ftp-backup/upload_backup_ftp.py > /dev/null 2>&1
10 5 * * * /usr/bin/python3 clean_old_file_ftp.py > /dev/null 2>&1