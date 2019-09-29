import shelve


def main():
    FILENAME = "states"
    with shelve.open(FILENAME) as states:
        states["London"] = "Great Britain"
        states["Paris"] = "France"
        states["Berlin"] = "Germany"
        states["Madrid"] = "Spain"

    with shelve.open(FILENAME) as states:
        print(type(states), type(states["London"]))
        print(states["London"])
        print(states["Madrid"])
        state = states.get("Brussels", "Undefined")
        print(state)
    print(type(states), end="\n\n")

    with shelve.open(FILENAME) as states:
        for key in states:
            print(key, " - ", states[key])
    print(end="\n\n")

    with shelve.open(FILENAME) as states:
        for state in states.items():
            print(state)
    # print(states["London"],type(states["London"])) #файл закрыт


if __name__ == "__main__":
    main()
