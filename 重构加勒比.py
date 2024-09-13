import os
import re


def rename_files(directory):
    # 遍历指定目录及其子目录
    for root, dirs, files in os.walk(directory):
        # 忽略名为"#整理完成"的子目录
        if '#整理完成' in root:
            print(f"忽略目录{root}")
            continue
        for file in files:
            # 处理满足条件的文件名
            new_name = process_filename(file)
            if new_name and new_name.lower() != file.lower():
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)  # 实际运行时去掉注释
                print(f"文件名从{file}更改为{new_name}")
            elif new_name:
                # print(f"文件名{file}已经符合要求，无需更改。")
                pass


def process_filename(filename):
    # 匹配包括 "Carib-XXXXXX-XXX-FHD ..." 的文件名模式
    # pattern = r'(?i)carib[-_](\d{6})[-_](\d{3}).*\.mkv'
    pattern = r'(?i)carib[-_](\d{6})[-_](\d{3}).*(\.mkv|\.mp4)$'
    match = re.match(pattern, filename)
    if match:
        # 格式化新文件名为 "carib-XXXXXX-XXX.mkv"
        # new_filename = f'carib-{match.group(1)}-{match.group(2)}.mkv'.lower()
        new_filename = f'carib-{match.group(1)}-{match.group(2)}{match.group(3)}'.lower()
        return new_filename
    else:
        # 匹配包括 "Carib-XXXXXX-XXX ..." 的文件名模式
        # match = re.match(r'(?i)carib-(\d{6})-(\d{3})[^\.]*\.mkv', filename)
        match = re.match(r'(?i)carib-(\d{6})-(\d{3})[^\.]*(\.mkv|\.mp4)$', filename)

        if match:
            # 格式化新文件名为 "carib-XXXXXX-XXX.mkv"
            print("matched rule 2")
            # new_filename = f'carib-{match.group(1)}-{match.group(2)}.mkv'.lower()
            new_filename = f'carib-{match.group(1)}-{match.group(2)}{match.group(3)}'.lower()
            return new_filename
        match2 = re.match(r'(\d{6})-(\d{3})-carib.*\.mkv', filename, re.IGNORECASE)
        # match2 = re.match(r'(\d{6})-(\d{3})-carib.*(\.mkv|\.mp4)$', filename, re.IGNORECASE)

        if match2:
            # print("xxxx-xxx-carbxxx.mkv")
            new_filename2 = f'carib-{match2.group(1)}-{match2.group(2)}.mkv'.lower()
            # new_filename2 = f'carib-{match2.group(1)}-{match2.group(2)}{match.group(3)}'.lower()

            return new_filename2
    return None


# 指定需要遍历的目录
# directory = '/Volumes/个人收藏/加勒比老'
# directory = '/Volumes/个人收藏/加勒比老/未命名文件夹'
directory = '/Volumes/个人收藏/加勒比'
rename_files(directory)
