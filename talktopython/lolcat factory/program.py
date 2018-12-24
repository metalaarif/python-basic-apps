#!/usr/bin/python3
import os


def main():
    header()
    create_folder()


def header():
    print("-" * 50)
    print("\t\t\t LoL Cat Factory")
    print("-" * 50)

def create_folder():
    current_path = os.path.dirname(__file__)
    folder_name = "cat_pics"
    photo_path = os.path.join(current_path, folder_name)

    if not os.path.exists(photo_path) or not os.path.isdir(photo_path):
        print("Creating a folder.....{}".format(photo_path))
        os.mkdir(photo_path)

    return photo_path

if __name__ == '__main__':
    main()