import base64
import json
import os

def images_to_json():
    # 支持的图片格式
    img_exts = ('.png', '.jpg', '.jpeg', '.gif', '.webp')
    result = {}

    # 遍历当前文件夹
    for filename in os.listdir('.'):
        # 只处理图片
        if filename.lower().endswith(img_exts):
            name_without_ext = os.path.splitext(filename)[0]  # 去掉后缀作为 key
            print(f"正在处理：{filename}")

            # 读取图片并转 base64
            with open(filename, 'rb') as f:
                data = f.read()
                base64_str = base64.b64encode(data).decode('utf-8')

            # 判断图片类型
            ext = filename.split('.')[-1].lower()
            mime = {
                'png': 'image/png',
                'jpg': 'image/jpeg',
                'jpeg': 'image/jpeg',
                'gif': 'image/gif',
                'webp': 'image/webp'
            }.get(ext, 'image/png')

            # 拼接最终 base64
            result[name_without_ext] = f"data:{mime};base64,{base64_str}"

    # 写入 json
    with open('images.png.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 生成完成！共 {len(result)} 张图片 → images.png.json")

if __name__ == '__main__':
    images_to_json()