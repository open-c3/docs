#!/usr/bin/env bash
set -e

# 设置图片目录
IMG_DIR="docs/attachments"

# 查找所有 Markdown 文件
find . -type f -name "*.md" | while read -r file; do
  # 提取 Markdown 中包含 Pasted image 的图片名
  grep -oE 'Pasted image [0-9]{14}\.png' "$file" | while read -r oldname; do
    newname=$(echo "$oldname" | sed 's/ /_/g')

    # 如果文件存在并未重命名过
    if [ "$oldname" != "$newname" ] && [ -f "$IMG_DIR/$oldname" ]; then
      echo "[INFO] Rename: $IMG_DIR/$oldname → $IMG_DIR/$newname"
      mv "$IMG_DIR/$oldname" "$IMG_DIR/$newname"
    fi

    # 替换 Markdown 中的引用
    sed -i '' "s/$oldname/$newname/g" "$file"
  done
done

echo "[DONE] 所有粘贴图像名称已修复。"

