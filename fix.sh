#!/bin/bash

# 修复复制粘贴到Obsidian上的图片，图片名字有空格，有空格会有问题，当下一个脚本fix_images.py 脚本替换的时候，如果是有空格，在MKdocs显示正常，但是在Obsidian显示不正常
bash fix_pasted_image_name.sh

# 修复，从WPS的word文档复制过来的内容，图片是一个全路径，脚本会把它拷贝到本项目的附件路径中。同时如果复制粘贴进来的图片也会修改成统一的路径。
python3 fix_images.py

