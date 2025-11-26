import os
from pathlib import Path
import shutil
import sys


def read_directory(folder: Path, indent: str = " ") -> None:
    print(indent + str(folder.name))
    if folder.is_dir():
        for child in folder.iterdir():
            read_directory(child, indent + "    ")


def copy_file(source: Path, destination: Path) -> None:
    destination_name = str(destination.name)

    if source.is_file():
        extension = source.suffix
        extension_path = os.path.join(destination_name, extension)
        os.makedirs(extension_path, exist_ok=True) 
        shutil.copy2(source, extension_path)
        return

    if source.is_dir():
        for child in source.iterdir():
            copy_file(child, destination)


if __name__ == "__main__":
    initial_folder = sys.argv[1]
    if len(sys.argv) < 3:
        destination = "dist"
    else:    
        destination = sys.argv[2]

    read_directory(Path(initial_folder))
    copy_file(Path(initial_folder), Path(destination))
    read_directory(Path(destination))
