import os
import shutil
from pathlib import Path

from parse import parse
from normalize import normalize

ext = {
    "images": ["JPEG", "PNG", "JPG", "SVG"],
    "video": ["AVI", "MP4", "MOV", "MKV"],
    "documents": ["DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX"],
    "audio": ["MP3", "OGG", "WAV", "AMR"],
    "archives": ["ZIP", "GZ", "TAR"],
    "other": [],
}

output = input('Please enter output folder name: ')


def rename(file, path):
    if os.path.exists(file):
        norm_name = normalize(file.stem) + file.suffix
        new_name = os.path.join(path, norm_name)
        os.rename(file, new_name)


def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def sort_known(sfx, path, file):
    for key, value in ext.items():
        directory = key
        parent_dir = path.parent
        dest = os.path.join(parent_dir, output, directory)

        for item in value:
            if sfx.casefold() == item.casefold():
                make_dir(dest)
                rename(file, dest)


def sort_unknown(sfx, path, file):
    for value in ext.values():
        directory = "other"
        parent_dir = path.parent
        dest = os.path.join(parent_dir, output, directory)

        for item in value:
            if not sfx.casefold() == item.casefold():
                make_dir(dest)
                rename(file, dest)


def handle_archives(path):
    parent_dir = path.parent
    norm_sfx = []
    for sfx in ext["archives"]:
        norm_sfx.append(sfx.casefold())
    dest = os.path.join(parent_dir, output, "archives")
    if os.path.exists(dest):
        os.chdir(dest)
    for item in Path(os.getcwd()).iterdir():
        arch_dest = os.path.join(os.getcwd(), item.stem)
        if item.is_file():
            shutil.unpack_archive(item, arch_dest)
    for root, _, f_names in os.walk(dest):
        for f in f_names:
            if Path(os.path.join(root, f)).suffix[1:] in norm_sfx:
                os.remove(Path(os.path.join(root, f)))


def handle_output(output):
    ext_list = []
    output_ext = []
    alien_ext = []
    for _, value in ext.items():
        for item in value:
            ext_list.append(item.casefold())

    parent_dir = os.getcwd()
    dest = Path(os.path.join(parent_dir, output))
    output_dict = {}
    for item in dest.iterdir():
        output_dict.update({item.name: []})
        output_list = []
        for file in item.iterdir():
            output_list.append(file.name)
            if file.suffix[1:] in ext_list:
                output_ext.append(file.suffix)
            else:
                if file.suffix:
                    alien_ext.append(file.suffix)
        output_dict.update({item.name: output_list})


def sort(path):
    if os.path.exists(path):
        dest = os.path.join(path.parent, output)
        make_dir(dest)
        for item in parse(path):
            file = Path(item).absolute()
            sfx = "".join(file.suffix[1:])

            sort_known(sfx, path, file)
            sort_unknown(sfx, path, file)

        if not parse(path):
            shutil.rmtree(path)
        else:
            sort(path)
        handle_output(dest)


if __name__ == "__main__":
    path = Path(input('Enter path to folder to be sorted: '))
    sort(path)
