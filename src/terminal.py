import subprocess
import os
import requests
from typing import List


def sh(
        command: List[str],
        dry_run: bool = False) -> None:
    """
    Execute a shell command.
    :param command: command line split as a list of strings.
    :param dry_run: if true, simulate command execution.
    :return: None
    """
    if dry_run:
        print(f'\t> {" ".join(command)}')
        return

    o, e = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    ).communicate()

    o, e = o.decode("utf-8").strip(), e.decode("utf-8").strip()
    if e:
        raise AttributeError(e)
    if o.startswith("RuntimeError"):
        raise AttributeError(o)
    if o:
        print(o)


def cd(
        path: str) -> None:
    """
    Change dir.
    :param path: folder to move to.
    :return: None
    """
    os.chdir(path)


def mv(
        old_path: str,
        new_path: str) -> None:
    """
    Rename an existing file.
    :param old_path: old file name.
    :param new_path: new file name.
    :return: None
    """
    os.rename(old_path, new_path)


def mkdir(
        folder: str) -> None:
    """
    Create a new folder.
    :param folder: new folder name.
    :return: None
    """
    os.makedirs(folder)


def touch(
        path: str,
        makedirs: bool = False) -> None:
    """
    Create a new file.
    :param path: new file path, including name.
    :param makedirs: if true, creates non-existing folders in path.
    :return: None
    """
    if makedirs:
        basedir = os.path.dirname(path)
        if not os.path.exists(basedir):
            mkdir(basedir)
    with open(path, 'a'):
        os.utime(path, None)


def curl(
        url: str,
        path: str,
        makedirs: bool = False) -> None:
    """
    Download a file from the Internet.
    :param url: url where the file is located.
    :param path: local path where to store the downloaded content, including file name.
    :param makedirs: if true, creates non-existing folders in path.
    :return: None
    """
    r = requests.get(url)
    touch(path, makedirs=makedirs)
    with open(path, "w") as tf:
        tf.write(r.content.decode("utf-8"))
