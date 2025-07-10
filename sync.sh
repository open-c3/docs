#!/bin/bash
cp fix-assets.sh open-c3.github.io/
cp fix-assets-book.sh open-c3.github.io/

IP=$(cat sync.txt )
rsync -av /Users/feng/Documents/Notes/open-c3-book/docs/open-c3.github.io/ root@$IP:/data/app/nginx/html/open-c3-docs/
ssh root@$IP  "cd /data/app/nginx/html/open-c3-docs/; bash fix-assets.sh"
