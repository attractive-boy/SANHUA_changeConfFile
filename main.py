import os
import shutil
import msvcrt
import psutil


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


def is_file_in_use(file_path):
    try:
        # 使用 psutil 检查是否有进程正在使用指定文件
        for process in psutil.process_iter(["pid", "open_files"]):
            open_files = process.info.get("open_files")
            if open_files:
                for file in open_files:
                    if file.path == file_path:
                        return True
    except psutil.AccessDenied:
        # 如果没有足够权限获取进程信息，假设文件已被使用
        return True

    return False


def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"已删除文件: {file_path}")
    except Exception as e:
        print(f"删除文件时出错: {e}")

        # 尝试停用使用该文件的进程
        terminate_processes_using_file(file_path)

        try:
            # 再次尝试删除文件
            os.remove(file_path)
            print(f"已删除文件: {file_path}")
        except Exception as e:
            print(f"再次删除文件时出错: {e}")


def delete_all_files(folder_path):
    # 获取目标文件夹中的所有文件
    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):  # 只删除文件，不处理目录
            delete_file(file_path)

    print("删除完成")


def terminate_processes_using_file(file_path):
    try:
        # 使用 psutil 停用使用指定文件的进程
        for process in psutil.process_iter(["pid", "open_files"]):
            for file in process.info["open_files"]:
                if file.path == file_path:
                    os.kill(process.pid, 9)
                    print(f"停用进程 {process.pid} 使用了文件 {file_path}")
    except psutil.AccessDenied:
        # 如果没有足够权限停用进程，打印提示信息
        print("无法停用进程：没有足够的权限。")


search_term = input("请输入要复制的文件夹名称: ")
copy_files_by_input(r"C:\Addins\SystemSettingAddins")
copy_files_by_input(r"C:\swwin_newent\server_cns\DLLs")
print("脚本执行完毕，请按任意键关闭窗口.")
msvcrt.getch()
