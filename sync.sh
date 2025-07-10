#!/bin/bash
IP=$(cat sync.txt )
rsync -av /Users/feng/Documents/Notes/open-c3-book/docs/open-c3.github.io/ root@$IP:/data/app/nginx/html/open-c3-docs/
ssh root@$IP  "cd /data/app/nginx/html/open-c3-docs/; bash fix-assets.sh"
