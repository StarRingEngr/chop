# build-wiki-index.py
import os
import json

WIKI_FOLDER = "wiki"
OUTPUT = "json/search-index.json"

files = []
for root, _, filenames in os.walk(WIKI_FOLDER):
    for f in filenames:
        if f.lower().endswith(".md"):
            rel_path = os.path.relpath(os.path.join(root, f), WIKI_FOLDER)
            rel_path = rel_path.replace("\\", "/").replace(".md", "")
            files.append(rel_path)

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(files, f, ensure_ascii=False, indent=2)

print(f"✅ 生成完成，共 {len(files)} 个文档")