import os
import re

# 根据记忆定义LeetCode Hot100的题号列表
hot100_numbers = [
    1, 49, 128,  # 哈希
    283, 11, 15, 42,  # 双指针
    3, 438,  # 滑动窗口
    560, 239, 76,  # 子串
    53, 56, 189, 238, 41,  # 普通数组
    73, 54, 48, 240,  # 矩阵
    160, 206, 234, 141, 142, 21, 2, 19, 24, 25, 138, 148, 23, 146,  # 链表
    94, 104, 226, 101, 543, 102, 108, 98, 230, 199, 114, 105, 437, 236, 124,  # 二叉树
    200, 994, 207, 208,  # 图论
    46, 78, 17, 39, 22, 79, 131, 51,  # 回溯
    35, 74, 34, 33, 153, 4,  # 二分查找
    20, 155, 394, 739, 84,  # 栈
    215, 347, 295,  # 堆
    121, 55, 45, 763,  # 贪心算法
    70, 118, 198, 279, 322, 139, 300, 152, 416, 32,  # 动态规划
    62, 64, 5, 1143, 72,  # 多维动态规划
    136, 169, 75, 31, 287  # 技巧
]

def process_files(directory='.'):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            # 使用正则表达式匹配以序号+点开头的文件名
            print(filename)
            match = re.match(r'^(\d+)\.', filename)
            if match:
                problem_number = int(match.group(1))
                if problem_number in hot100_numbers:
                    add_hot100_tag(os.path.join(directory, filename))

def add_hot100_tag(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # 查找标签行（以井号开头的行）
    tag_line_index = None
    for i, line in enumerate(lines):
        if re.match(r'^\s*#\w+', line):
            tag_line_index = i
            break
    
    # 如果找到标签行
    if tag_line_index is not None:
        # 检查是否已经包含hot100标签
        if '#hot100' not in lines[tag_line_index]:
            # 在行尾添加hot100标签（确保有空格分隔）
            lines[tag_line_index] = lines[tag_line_index].rstrip() + ' #hot100\n'
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(lines)
            print(f"Added #hot100 tag to existing tags in {file_path}")
        else:
            print(f"File {file_path} already has #hot100 tag")
    else:
        # 如果没有找到标签行，则在文件末尾添加
        if lines and lines[-1].strip() != '':
            lines.append('\n')  # 确保有空行分隔
        lines.append('#hot100\n')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)
        print(f"Added #hot100 tag to {file_path}")

if __name__ == "__main__":
    process_files()
    print("Processing completed!")
