import os


def main():
    path_dir = input("Type a full path of dir: ")
    os.chdir(path_dir)
    files = filter(os.path.isfile, os.listdir(path_dir))
    files = [os.path.join(path_dir, f) for f in files]
    files.sort(key=lambda x: os.path.getmtime(x))

    i = 1

    for filename in files:
        extension = os.path.splitext(filename)[1]
        dst = str(i) + extension
        dst = os.path.join(path_dir, dst)  # path_dir + dst
        os.rename(filename, dst)
        i += 1


if __name__ == '__main__':
    main()
