import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")


def start():
    import os
    import easygui
    import zipfile
    import pathlib
    from shutil import copy

    cwd_path = pathlib.Path.cwd()
    # cd_cmd = "cd " + str(cwd_path)
    # os.system(cd_cmd)
    path_str = easygui.fileopenbox()
    if path_str is None:
        return None
    else:
        path = pathlib.Path(path_str)
        if path.suffix == ".zip":
            zip_ref = zipfile.ZipFile(path, 'r')
            zip_ref.extractall(cwd_path)
            zip_ref.close()
            return ""
        else:
            copy(str(path), str(cwd_path))


if __name__ == '__main__':
    start()
