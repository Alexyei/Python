import pathlib
import datetime

FILE_PATTERN = "*.txt"
ARCHIVE = "archive"

print(pathlib.Path().cwd())


def copyfiles(dirpath, newdirpath):
    allsize = 0
    count = 0
    cur_path = pathlib.Path(dirpath)

    if not pathlib.Path.exists(newdirpath):
        pathlib.Path.mkdir(newdirpath)

    for file in cur_path.glob(FILE_PATTERN):
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


def main():
    today_dir_string = datetime.date.today().strftime("%Y-%m-%d")
    copyfiles(pathlib.Path(), pathlib.Path() / ARCHIVE / today_dir_string)


if __name__ == "__main__":
    main()
