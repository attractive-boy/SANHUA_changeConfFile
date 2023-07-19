import os
import shutil
import ctypes
import msvcrt


def copy_files_by_input(destination_folder):
    # 输入要复制的文件夹名称
    delete_all_files(destination_folder)
    try:
        # 构建源文件夹的完整路径
        source_path = destination_folder + search_term

        if os.path.exists(source_path) and os.path.isdir(source_path):
            # 获取源文件夹中的所有文件
            files = os.listdir(source_path)

            for file in files:
                # 构建源文件的完整路径和目标文件的完整路径
                source_file_path = os.path.join(source_path, file)
                destination_file_path = os.path.join(destination_folder, file)

                try:
                    # 复制文件到目标文件夹
                    shutil.copy2(source_file_path, destination_file_path)
                    print(f"已复制文件: {file}")
                except Exception as e:
                    print(f"复制文件时出错: {e}")
        else:
            print("指定的文件夹不存在或不是文件夹类型")
    except Exception as e:
        print(f"删除文件时出错: {e}")

    print("复制完成")


def delete_all_files(folder_path):
    # 获取目标文件夹中的所有文件
    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path, file)

        try:
            # 删除文件
            ctypes.windll.kernel32.DeleteFileW(file_path)
            print(f"已删除文件: {file}")
        except Exception as e:
            print(f"删除文件时出错: {e}")

    print("删除完成")


search_term = input("请输入要复制的文件夹名称: ")
copy_files_by_input(r"C:\Addins\SystemSettingAddins")
copy_files_by_input(r"C:\swwin_newent\server_cns\DLLs")
print("脚本执行完毕，请按任意键关闭窗口.")
msvcrt.getch()
