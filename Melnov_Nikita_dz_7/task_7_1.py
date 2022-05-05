import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def make_my_dir(base_dir, my_starter):
    for key, val in my_starter.items():
        folder = os.path.join(base_dir, key)
        if not os.path.exists(folder):
            os.mkdir(folder)
        for el in val:
            folder = os.path.join(base_dir, key, el)
            if not os.path.exists(folder):
                os.mkdir(folder)

starter = {'my_project': ['settings', 'mainapp', 'adminapp', 'autohapp']}

if __name__ == '__main__':
    make_my_dir(BASE_DIR, starter)