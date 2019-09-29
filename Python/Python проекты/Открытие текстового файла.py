def main():
    try:
        myfile = open("textfile", "w")
        try:
            myfile.write("hello world")
        except Exception as e:
            print("open", e)
        finally:
            myfile.close()
    except Exception as ex:
        print("not open", ex)
    '''try:
        with open("textfile", "w") as myfile:
            try:
                myfile.write("hello world")
            except Exception as e:
                print("open", e)
    except Exception as ex:
        print("not open", ex)'''
    print("text")


if __name__ == "__main__":
    main()
