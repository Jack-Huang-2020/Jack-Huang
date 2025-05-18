import os
import random
import uuid

def shuffle_png_files(folder_path):
    # 获取所有PNG文件（不区分大小写）
    original_files = [f for f in os.listdir(folder_path)
                     if f.lower().endswith('.png') and os.path.isfile(os.path.join(folder_path, f))]

    if not original_files:
        print("未找到PNG文件。")
        return

    # 生成打乱后的文件名列表
    shuffled_files = original_files.copy()
    random.shuffle(shuffled_files)

    # 生成临时文件名列表（使用UUID保证唯一性）
    temp_files = [str(uuid.uuid4()) + ".png" for _ in original_files]

    # 第一次重命名：原文件 → 临时文件
    for orig, temp in zip(original_files, temp_files):
        orig_path = os.path.join(folder_path, orig)
        temp_path = os.path.join(folder_path, temp)
        try:
            os.rename(orig_path, temp_path)
        except Exception as e:
            print(f"错误：无法重命名 {orig} → {temp} ({e})")
            return

    # 第二次重命名：临时文件 → 打乱后的文件名
    for temp, new_name in zip(temp_files, shuffled_files):
        temp_path = os.path.join(folder_path, temp)
        new_path = os.path.join(folder_path, new_name)
        try:
            os.rename(temp_path, new_path)
        except Exception as e:
            print(f"错误：无法重命名 {temp} → {new_name} ({e})")
            return

    print(f"操作成功完成！共处理了 {len(original_files)} 个文件。")

if __name__ == "__main__":
    folder = input("请输入目标文件夹路径：")
    if not os.path.isdir(folder):
        print("错误：指定的路径不是有效文件夹。")
    else:
        shuffle_png_files(folder)