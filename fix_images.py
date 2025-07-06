import os
import re
import shutil
from pathlib import Path

docs_dir = "docs"  # Obsidian 目录
assets_dir = os.path.join(docs_dir, "attachments")
os.makedirs(assets_dir, exist_ok=True)

# 正则：Obsidian图片语法 ![[xxx.png]]
obsidian_img_pattern = re.compile(r'!\[\[(.+?\.(?:png|jpg|jpeg|gif))\]\]')

# 正则：WPS粘贴路径 file://...
wps_img_pattern = re.compile(r'!\[\]\(file://(.*?/wps\d+\.(?:png|jpg|jpeg))\)')

def fix_md_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # 修复 Obsidian 图片语法
    content = obsidian_img_pattern.sub(r'![](attachments/\1)', content)

    # 修复 WPS 图片引用
    matches = wps_img_pattern.findall(content)
    for img_path in matches:
        img_path = img_path.strip()
        src = Path(img_path)
        if not src.exists():
            print(f"[WARN] 找不到图片：{img_path}")
            continue

        dest = Path(assets_dir) / src.name
        shutil.copy2(src, dest)
        new_md_path = f'attachments/{src.name}'
        content = content.replace(f"file://{img_path}", new_md_path)

    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[OK] 修复: {path}")

def scan_all_md_files():
    for root, _, files in os.walk(docs_dir):
        for name in files:
            if name.endswith(".md"):
                fix_md_file(os.path.join(root, name))

if __name__ == "__main__":
    scan_all_md_files()

