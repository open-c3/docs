import os
import re
import shutil
from pathlib import Path
from datetime import datetime

# === 配置 ===
docs_dir = "docs"  # Obsidian 内容根目录
assets_dir = os.path.join(docs_dir, "attachments")
os.makedirs(assets_dir, exist_ok=True)

# Obsidian 图片语法 ![[image.png]]
obsidian_img_pattern = re.compile(r'!\[\[(.+?\.(?:png|jpg|jpeg|gif))\]\]')

# WPS 粘贴路径 file://...
wps_img_pattern = re.compile(r'!\[\]\(file://(.*?/wps\d+\.(?:png|jpg|jpeg))\)')

def gen_new_filename(original_name):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{timestamp}_{original_name}"

def fix_md_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    updated_files = {}

    # === 修复 Obsidian 图片语法 ===
    def replace_obsidian(match):
        filename = match.group(1)
        new_path = f"/attachments/{filename}"
        return f"![]({new_path})"

    content = obsidian_img_pattern.sub(replace_obsidian, content)

    # === 修复 WPS 粘贴路径 ===
    matches = wps_img_pattern.findall(content)
    for img_path in matches:
        img_path = img_path.strip()
        src = Path(img_path)
        if not src.exists():
            print(f"[WARN] 找不到图片：{img_path}")
            continue

        # 避免重复处理
        if img_path in updated_files:
            new_filename = updated_files[img_path]
        else:
            new_filename = gen_new_filename(src.name)
            dest = Path(assets_dir) / new_filename
            shutil.copy2(src, dest)
            updated_files[img_path] = new_filename

        content = content.replace(f"file://{img_path}", f"/attachments/{new_filename}")

    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[OK] 修复完成: {path}")

def scan_all_md_files():
    for root, _, files in os.walk(docs_dir):
        for name in files:
            if name.endswith(".md"):
                fix_md_file(os.path.join(root, name))

if __name__ == "__main__":
    scan_all_md_files()

