import os
import random
import re

def select_files():
    # 获取当前运行目录
    current_dir = os.getcwd()

    # 获取目录下所有文件，不包括脚本自身
    all_files = [f for f in os.listdir(current_dir) if os.path.isfile(f) and f != os.path.basename(__file__)]

    # 初始化分类列表
    simple_files = []
    medium_files = []
    hard_files = []

    # 分类文件：按内容检查
    for file in all_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                if "简单" in content:
                    simple_files.append(file)
                if "中等" in content:
                    medium_files.append(file)
                if "困难" in content:
                    hard_files.append(file)
        except (UnicodeDecodeError, IOError):
            # 跳过无法读取的文件
            continue

    # 检查是否有足够的文件满足条件
    if len(simple_files) < 5 or len(medium_files) < 5 or len(hard_files) < 2:
        print("文件内容不足以满足选择条件，请检查目录中的文件。")
        return

    # 定义函数：检查文件名的中文字符是否重复
    def has_unique_chinese_chars(files):
        seen_chars = set()
        for file in files:
            filename = os.path.splitext(file)[0]  # 去掉扩展名
            chinese_chars = re.findall(r'[\u4e00-\u9fa5]', filename)
            for char in chinese_chars:
                if char in seen_chars:
                    return False
                seen_chars.add(char)
        return True

    # 随机选择文件，确保中文字符不重复
    while True:
        selected_simple = random.sample(simple_files, 3)
        selected_medium = random.sample(medium_files, 3)
        selected_hard = random.sample(hard_files, 2)
        selected_files = selected_simple + selected_medium + selected_hard

        if has_unique_chinese_chars(selected_files):
            break

    # 合并选取的文件并去掉扩展名
    selected_files_no_ext = [f"[[{os.path.splitext(f)[0]}]]" for f in selected_files]

    # 打印结果
    print("\n".join(selected_files_no_ext))

if __name__ == "__main__":
    select_files()
