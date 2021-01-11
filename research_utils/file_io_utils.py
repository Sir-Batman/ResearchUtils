from pathlib import Path
from warnings import warn
from os import makedirs
from uuid import uuid1


def safe_write(filename):
    """
    Converts a string filename into a Path object, and checks that a filename is safe to write to.
    If not, it returns a modified version of the filename with a UUID inserted before the file extension.
    If the parent directory path does not exist, it is created.
    Warnings, not exceptions are raised upon either case.

    :param filename: string, path to the file. Can be relative or absolute
    :return: Path: path to a file that does not exist (and thus is safe to write to without overwriting)
    """
    file = Path(filename)
    if not file.parent.exists():
        warn(f"[safe_write] Path to directory {file.parent} does not exist. Creating {file.parent}...")
        makedirs(file.parent)
    if file.exists():
        new_name = file.stem + "_" + str(uuid1())
        warn(f"[safe_write] Filename {file.name} already exists. Changing filename to {new_name + str(file.suffix)}.")
        file = Path(file.parent, new_name+str(file.suffix))
    return file
