import os
from datetime import datetime

def generate_comparison_md():
    # 获取当前目录
    current_dir = os.getcwd()
    
    # 设置comparisons和questions目录的路径
    comparisons_dir = os.path.join(current_dir, '..', 'comparisons')
    questions_dir = os.path.join(current_dir, '..', 'questions')
    
    # 获取questions目录下所有的.md文件
    question_files = [f for f in os.listdir(questions_dir) if f.endswith('.md')]
    
    # 遍历questions目录中的每个文件
    for question_file in question_files:
        # 获取前缀aaa.bbb（去掉md后缀）
        prefix = '.'.join(question_file.split('.')[:2])  # 获取aaa.bbb部分
        
        # 创建新文件名: aaa.bbb.cpp.evo.md
        new_filename = f"{prefix}.cpp.evo.md"
        new_file_path = os.path.join(current_dir, new_filename)
        
        # 读取comparisons目录下以aaa.bbb为前缀的所有文件
        comparison_files = [
            f for f in os.listdir(comparisons_dir) if f.startswith(prefix)
        ]

        
        # 按照倒序排列文件名
        comparison_files.sort(reverse=True)
        
        # 生成预期的内容
        expected_content = generate_expected_content(question_file, comparison_files, comparisons_dir, questions_dir)

        # 检查文件是否已存在
        if os.path.exists(new_file_path):
            # 如果文件已存在，读取内容并验证
            with open(new_file_path, 'r', encoding='utf-8') as existing_file:
                existing_content = existing_file.read()
                
                expected_count = expected_content.count("![[")
                actual_count = existing_content.count("![[")
                
                # 比较出现次数
                if expected_count == actual_count:
                    print(f"文件 {new_filename} 已存在，内容符合预期。")
                else:
                    print(f"文件 {new_filename} 已存在，但内容不符合预期。")
                    
                    # 调试输出，查看comparisons目录中的所有文件
                    print(f"Comparisons Directory: {comparisons_dir}")
                    print("Comparison Files:", comparison_files)

                    print("\n---- 预期内容 ----")
                    print(expected_content)
                    print("---- 当前内容 ----")
                    print(existing_content)
                    
                    # 提示用户是否覆盖
                    user_input = input("内容不匹配。是否覆盖该文件？(y/N): ").strip().lower()
                    
                    if user_input == 'y':
                        with open(new_file_path, 'w', encoding='utf-8') as new_file:
                            new_file.write(expected_content)
                        print(f"文件 {new_filename} 已被覆盖。")
                    else:
                        print(f"文件 {new_filename} 保持不变。")
        else:
            # 文件不存在，创建新文件
            with open(new_file_path, 'w', encoding='utf-8') as new_file:
                new_file.write(expected_content)
            print(f"生成文件: {new_filename}")


def generate_expected_content(question_file, comparison_files, comparisons_dir, questions_dir):
    """根据题目文件和比较文件生成预期的内容"""
    # 获取当前日期并格式化为 YYYY/MM/DD
    current_date = datetime.now().strftime("%Y/%m/%d")
    
    # 去除.md后缀，只保留文件名
    question_filename_without_md = os.path.splitext(question_file)[0]
    
    # 写入标签
    content = f"#{current_date} #迭代/\n\n"
    
    # 写入题目部分
    content += f"# 题目\n\n"
    content += f"![[{question_filename_without_md}]]\n\n"
    
    # 写入comparisons部分
    # 使用倒叙遍历，即最新的比较文件在前
    for i in range(0, len(comparison_files), 1):  # 生成倒序的序列
        comparison_file = comparison_files[i]  # 获取对应的比较文件
        # 去除.cpp.cmp后缀
        comparison_filename_without_ext = os.path.splitext(comparison_file)[0]
        # 文件路径
        comparison_file_path = os.path.relpath(os.path.join(comparisons_dir, comparison_file), start=os.getcwd())
        # 写入每个比较的文件
        content += f"# 第 {len(comparison_files) - i} 次\n\n"  # 倒序编号
        content += f"![[{comparison_filename_without_ext}]]\n\n"
    
    return content

if __name__ == "__main__":
    generate_comparison_md()
