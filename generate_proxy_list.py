#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json
from pathlib import Path

def extract_title_and_version(file_path):
    """
    从 HTML 文件中提取标题和版本号。
    优先从 <title> 标签获取标题，从 CONFIG.VERSION 获取版本号。
    如果找不到，则返回默认值。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"读取文件 {file_path} 失败: {e}")
        return None, None

    # 提取标题
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip() if title_match else None

    # 提取版本号（支持 CONFIG.VERSION = "xxx" 或 VERSION: "xxx"）
    version_match = re.search(r'CONFIG\.VERSION\s*=\s*["\']([^"\']+)["\']', content)
    if not version_match:
        version_match = re.search(r'VERSION\s*:\s*["\']([^"\']+)["\']', content)
    version = version_match.group(1).strip() if version_match else None

    # 如果没有标题，用文件名代替
    if not title:
        title = Path(file_path).stem

    return title, version

def scan_proxies(proxies_dir='proxies'):
    """
    扫描 proxies 目录下的所有 .html 文件，返回代理列表。
    """
    if not os.path.isdir(proxies_dir):
        print(f"目录 {proxies_dir} 不存在，跳过扫描。")
        return []

    proxies = []
    for filename in os.listdir(proxies_dir):
        if filename.endswith('.html'):
            file_path = os.path.join(proxies_dir, filename)
            title, version = extract_title_and_version(file_path)
            proxies.append({
                "name": title,
                "file": filename,          # 只存文件名，前端链接时拼接目录
                "description": "",
                "version": version or ""
            })
    return proxies

def write_jsonl(proxies, output_file='json/proxy-list.jsonl'):
    """
    将代理列表写入 JSONL 文件（每行一个 JSON 对象）。
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for proxy in proxies:
            f.write(json.dumps(proxy, ensure_ascii=False) + '\n')
    print(f"已生成 {output_file}，共 {len(proxies)} 条代理记录。")

if __name__ == '__main__':
    proxies = scan_proxies()
    write_jsonl(proxies)