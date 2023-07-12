import os


def parse(path):
    f_name = []
    for root, _, f_names in os.walk(path):
        for f in f_names:
            f_name.append(os.path.join(root, f))
    return f_name
