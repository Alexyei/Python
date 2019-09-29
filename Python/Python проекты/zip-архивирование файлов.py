import pathlib
import datetime
import zipfile

FILE_PATTERN = "*.txt"
ARCHIVE = "archive"


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


def filestozip(dirpath, zipname):
    allsize = 0
    count = 0
    cur_path = pathlib.Path(dirpath)
    with zipfile.ZipFile(zipname, 'w') as ziparchive:
        for file in cur_path.glob(FILE_PATTERN):
            size = file.stat().st_size
            print(file.name, size)

            # newpath = pathlib.Path(newdirpath) / file.name
            # if pathlib.Path.exists(newpath):
            #     pathlib.Path.unlink(newpath)
            # file.rename(pathlib.Path(newpath))
            ziparchive.write(file)
            file.unlink()

            allsize += size
            count += 1

    print("Add to zip", count, "files")
    print("Total files size:", allsize)


def main():
    today_dir_string = datetime.date.today().strftime("%Y-%m-%d")
    filestozip(pathlib.Path(), today_dir_string + ".zip")
    # copyfiles(pathlib.Path(), pathlib.Path() / ARCHIVE)
    (pathlib.Path() / (today_dir_string + ".zip")).rename(pathlib.Path() / ARCHIVE / (today_dir_string + ".zip"))


if __name__ == "__main__":
    main()
