import os
import random
import uuid
import sys

def shuffle_png_in_directory(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        # 筛选出所有.png文件，不区分大小写
        png_files = [f for f in filenames if f.lower().endswith('.png')]
        if len(png_files) < 2:
            continue  # 不足两个文件无需处理

        # 生成随机顺序的文件名列表
        shuffled_files = png_files.copy()
        random.shuffle(shuffled_files)

        # 生成临时文件名列表（使用UUID确保唯一性）
        temp_files = [os.path.join(dirpath, uuid.uuid4().hex + '.tmp') for _ in png_files]

        # 第一步：将所有PNG文件重命名为临时文件
        for i in range(len(png_files)):
            src = os.path.join(dirpath, png_files[i])
            dst = temp_files[i]
            try:
                os.rename(src, dst)
            except Exception as e:
                print(f"错误：无法重命名 {src} 到 {dst}，原因：{e}")
                return

        # 第二步：将临时文件按随机顺序重命名为原文件名
        for i in range(len(png_files)):
            src = temp_files[i]
            dst = os.path.join(dirpath, shuffled_files[i])
            try:
                os.rename(src, dst)
            except Exception as e:
                print(f"错误：无法重命名 {src} 到 {dst}，原因：{e}")
                return

if __name__ == "__main__":

#    if len(sys.argv) != 2:
#        print("使用方法：python 打乱材质包图片顺序.py <目录路径>")
#        sys.exit(1)

    target_dir = input("PATH:")
    target_dir = target_dir.replace("\\","//")
    DEMO_PATH = "D://Jack Huang//Repo//Jack-Huang - Github//Demo//Demo - 1"

    if target_dir == "DEMO_PATH" or "PATH" or "path":
        if not os.path.isdir(DEMO_PATH):
            print(f"错误：{DEMO_PATH} 不是有效目录")
            sys.exit(1)
        shuffle_png_in_directory(DEMO_PATH)
        print("文件名打乱完成！")
    else:
        if not os.path.isdir(target_dir):
            print(f"错误：{target_dir} 不是有效目录")
            sys.exit(1)
        shuffle_png_in_directory(target_dir)
        print("文件名打乱完成！")