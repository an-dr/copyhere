import sys
import easygui

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")


# def __openfile():

def start(name: str = None):
    import os
    import zipfile
    import pathlib
    from shutil import copy
    here_dir = pathlib.Path.cwd()
    is_zip = False

    # source processing:
    gui_path2open = os.environ.get("COPYHERE_SOURCEDIR", default=None)
    if gui_path2open is None:
        gui_path2open = '*'
    else:
        gui_path2open = os.path.join(gui_path2open, '*')
    src_str = easygui.fileopenbox(default=gui_path2open)
    if src_str is None:
        print("No selection")
        return None  # close if no selection
    src = pathlib.Path(src_str)
    if src.suffix == ".zip":
        is_zip = True
    src_dir, src_name = src.parent, src.name

    # destination processing:
    if name is None:
        here_name = src_name
    elif name == "":
        here_name = easygui.enterbox(msg="Enter the name", title=" ", default="")
    else:
        here_name = name + src.suffix
    here = here_dir.joinpath(here_name)

    if is_zip:
        zip_ref = zipfile.ZipFile(src, 'r')
        zip_ref.extractall(here.parent)
        zip_ref.close()
    else:
        copy(str(src), str(here))


if __name__ == '__main__':
    try:
        start()
    except Exception as e:
        print(e)
        easygui.msgbox(e, "Error")
