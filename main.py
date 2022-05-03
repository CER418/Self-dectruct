import os


def destruct():
    """Self destruct application"""
    os.system(f'rm -rf {os.getcwd()}')


if __name__ == '__main__':
    destruct()
