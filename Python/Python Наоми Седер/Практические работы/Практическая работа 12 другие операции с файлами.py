import os
import pathlib
import glob


def test():
    print(os.getcwd())
    print(os.curdir)
    print(os.pardir)
    print(type(os.getcwd()))
    print(type(os.curdir))
    print(type(os.pardir))

    cur_path = pathlib.Path()
    print(cur_path)
    print(cur_path.cwd())
    print(cur_path.parent)
    print(cur_path.parent.cwd())
    print(type(cur_path))
    print(type(cur_path.cwd()))
    print(type(cur_path.parent))
    print(type(cur_path.parent.cwd()))

    cur_path = pathlib.Path(os.pardir)
    print(cur_path.cwd())
    print(cur_path.parent)
    print("*" * 100)
    print()

    path1 = os.path.join(os.getcwd(), 'test_log.txt')
    print(path1)
    path1 = os.path.join(os.curdir, 'test_log.txt')
    print(path1)
    path1 = os.path.join(os.pardir, 'test_log.txt')
    print(path1)
    path1 = os.path.join(cur_path, 'test_log.txt')
    print(path1)
    path1 = os.path.join(cur_path.parent, 'test_log.txt')
    print(path1)
    path1 = os.path.join(cur_path.parent.cwd(), 'test_log.txt')
    print(path1)
    print("*" * 100)

    cur_path = pathlib.Path()
    path1 = cur_path.joinpath(cur_path.cwd(), 'test_log.txt')
    print(path1, type(path1))
    print(cur_path)
    path1 = cur_path.joinpath(os.getcwd(), 'test_log.txt')
    print(path1, type(path1))
    print(cur_path)
    path1 = cur_path.joinpath(os.curdir, 'test_log.txt')
    print(path1, type(path1))
    print(cur_path)
    path1 = cur_path.joinpath(os.pardir, 'test_log.txt')
    print(path1, type(path1))
    print(cur_path)
    path1 = cur_path.joinpath(cur_path.parent, 'test_log.txt')
    print(path1, type(path1))
    print(cur_path)
    path1 = cur_path.joinpath(cur_path.parent.cwd(), 'test_log.txt')
    print(path1, type(path1))
    print(cur_path)
    print("*" * 100)
    cur_path = pathlib.Path('test_log.txt')
    print(cur_path)
    path1 = cur_path.cwd()
    print(path1)
    print(cur_path.absolute())
    print("*" * 100)

    path1 = os.path.join(os.getcwd(), 'test_log.txt')
    path2 = os.path.join(os.path.dirname(path1), 'test_log.txt.old')
    print(path2)

    cur_path = pathlib.Path()
    path2 = cur_path.joinpath(cur_path.cwd(), 'test_log.txt.old')
    print(path2)
    path2 = pathlib.Path(cur_path.cwd(), 'test_log.txt.old')
    print(path2)


def filessize(dirpath):
    allsize = 0
    cur_path = pathlib.Path(dirpath)
    for file in cur_path.glob("*txt"):
        size = file.stat().st_size
        print(file.name, size)
        allsize += size
    print("Total file size:", allsize)


def filessizeos(dirpath):
    allsize = 0
    for file in glob.glob(os.path.join(dirpath, "*txt")):
        size = os.path.getsize(file)
        print(os.path.basename(file), size)
        allsize += size
    print("Total files size:", allsize)


def copyfiles(dirpath, newdirpath):
    allsize = 0
    count = 0
    cur_path = pathlib.Path(dirpath)

    if not pathlib.Path.exists(newdirpath):
        pathlib.Path.mkdir(newdirpath)

    for file in cur_path.glob("*txt"):
        size = file.stat().st_size
        print(file.name, size)

        newpath = pathlib.Path(newdirpath) / file.name
        if pathlib.Path.exists(newpath):
            pathlib.Path.unlink(newpath)
        file.rename(pathlib.Path(newpath))

        allsize += size
        count += 1

    print("Copy", count, "files")
    print("Total files size:", allsize)


def copyfilesos(dirpath, newdirpath):
    allsize = 0
    count = 0
    # cur_path = pathlib.Path(dirpath)

    if not os.path.exists(newdirpath):
        os.makedirs(newdirpath)

    for file in glob.glob(os.path.join(dirpath, "*txt")):
        size = os.path.getsize(file)
        name = os.path.basename(file)
        print(name, size)

        newpath = os.path.join(newdirpath, name)
        if os.path.exists(newdirpath):
            os.unlink(newdirpath)  # отказано в доступе
        # pathlib.Path.unlink(pathlib.Path().pnewpath)
        os.rename(dirpath, newdirpath)

        allsize += size
        count += 1

    print("Copy", count, "files")
    print("Total files size:", allsize)


def main():
    # test()
    filessize(pathlib.Path())
    print("*" * 100)
    filessizeos(pathlib.Path())
    print("*" * 100)
    filessize(os.getcwd())
    print("*" * 100)
    filessizeos(os.getcwd())
    print("*" * 100)

    copyfiles(pathlib.Path(), pathlib.Path().cwd() / "backup")
    copyfiles(pathlib.Path(), pathlib.Path() / "backup")
    # copyfiles(pathlib.Path(), os.path.join(os.getcwd(), "backup"))
    # copyfilesos(pathlib.Path(), pathlib.Path().cwd() / "backup")


if __name__ == "__main__":
    main()
