#!/bin/sh
# fullbackup.sh script
tar cf /storage/backup/$(date +%Y%m%d%H%M%S).tar \
  --exclude=Thumbnails --exclude=.thumbnails \
  /storage/.kodi /storage/.cache /storage/.config
find /storage/backup -name "*.tar" -type f -mtime +15 -exec rm -f {} \;