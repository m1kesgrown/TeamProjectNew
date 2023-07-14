import os
import shutil
import zipfile
import sys
from pathlib import Path


img_files = []
vid_files = []
doc_files = []
mus_files = []
arc_files = []
know_files = [img_files, vid_files, doc_files, mus_files, arc_files]
know_ext = []
unknow_ext = []


def sorter(path):
    dest_fold_im = os.path.join(path, 'Images')
    os.makedirs(dest_fold_im, exist_ok=True)
    dest_fold_vid = os.path.join(path, 'Video')
    os.makedirs(dest_fold_vid, exist_ok=True)
    dest_fold_mus = os.path.join(path, 'Music')
    os.makedirs(dest_fold_mus, exist_ok=True)
    dest_fold_doc = os.path.join(path, 'Documents')
    os.makedirs(dest_fold_doc, exist_ok=True)
    dest_fold_arc = os.path.join(path, 'Archieve')
    os.makedirs(dest_fold_arc, exist_ok=True)

    def sort(path):
        for obj in os.listdir(path):
            obj_path = os.path.join(path, obj)
            if os.path.isdir(obj_path):
                if os.listdir(obj_path):
                    sort(obj_path)
                else:
                    if os.path.basename(obj_path) not in ['Music', 'Video', 'Documents', 'Archieve', 'Images']:
                        os.rmdir(obj_path)
            elif os.path.isfile(obj_path):
                normalize(obj_path)

    def normalize(obj_path):
        img_ext = ('jpeg', 'jpg', 'png', 'svg')
        vid_ext = ('avi', 'mp4', 'mov', 'mkv')
        doc_ext = ('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx')
        mus_ext = ('mp3', 'ogg', 'wav', 'amr')
        arc_ext = ('zip', 'gz', 'tar')

        dir_path, name = os.path.split(obj_path)
        CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
        TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                       "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
        TRANS = {}
        for c, t in zip(CYRILLIC_SYMBOLS, TRANSLATION):
            TRANS[ord(c.lower())] = t.lower()
            TRANS[ord(c.upper())] = t.upper()

        new_name = name.translate(TRANS)
        parts = new_name.split('.')

        symbol_for_change = ['!', '@', '#', '$', '%', '^', '&', '*', "'", '.',
                             '(', ')', '-', '+', '{', '}', '`', '|', '"', '№', ';', '%', ':', '?', '*', '/', '', ' ']
        file_name = '.'.join(parts[:-1])
        ext = parts[-1].lower()

        norm_name = ''
        for char in file_name:
            if char in symbol_for_change:
                norm_name += '_'
            else:
                norm_name += char
        file_name = f'{norm_name}.{ext}'
        ren_f = os.path.join(dir_path, file_name)

        if ext in img_ext:
            count = 1
            final_path = os.path.join(dest_fold_im, file_name)
            while os.path.exists(final_path):
                file_name = f'{norm_name}_{count}.{ext}'
                os.rename(obj_path, ren_f)
                final_path = os.path.join(dest_fold_im, file_name)
                count += 1
            shutil.move(obj_path, final_path)
            img_files.append(file_name)
            know_ext.append(ext)

        elif ext in vid_ext:
            count = 1
            final_path = os.path.join(dest_fold_vid, file_name)
            while os.path.exists(final_path):
                file_name = f'{norm_name}_{count}.{ext}'
                os.rename(obj_path, ren_f)
                final_path = os.path.join(dest_fold_vid, file_name)
                count += 1
            shutil.move(obj_path, final_path)
            img_files.append(file_name)
            know_ext.append(ext)
        elif ext in doc_ext:
            count = 1
            final_path = os.path.join(dest_fold_doc, file_name)
            while os.path.exists(final_path):
                file_name = f'{norm_name}_{count}.{ext}'
                os.rename(obj_path, ren_f)
                final_path = os.path.join(dest_fold_doc, file_name)
                count += 1
            shutil.move(obj_path, final_path)
            img_files.append(file_name)
            know_ext.append(ext)

        elif ext in mus_ext:
            count = 1
            final_path = os.path.join(dest_fold_mus, file_name)
            while os.path.exists(final_path):
                file_name = f'{norm_name}_{count}.{ext}'
                os.rename(obj_path, ren_f)
                final_path = os.path.join(dest_fold_mus, file_name)
                count += 1
            shutil.move(obj_path, final_path)
            img_files.append(file_name)
            know_ext.append(ext)
        elif ext in arc_ext:
            with zipfile.ZipFile(obj_path, 'r') as zip_ref:
                archive_name = os.path.splitext(obj_path)[0]
                archive_dir = os.path.join(
                    obj_path, 'archives', archive_name)
                os.makedirs(archive_dir, exist_ok=True)
                zip_ref.extractall(archive_dir)
                os.remove(obj_path)
            count = 1
            final_path = os.path.join(dest_fold_arc, file_name)
            while os.path.exists(final_path):
                file_name = f'{norm_name}_{count}.{ext}'
                os.rename(obj_path, ren_f)
                final_path = os.path.join(dest_fold_arc, file_name)
                count += 1
            shutil.move(obj_path, final_path)
            img_files.append(file_name)
            know_ext.append(ext)
        else:
            unknow_ext.append(ext)
    path = input("Please provide the directory path: ")
    sort(path)


if __name__ == '__main__':
    sorter()
