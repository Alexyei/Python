def main():
    text = "Hello, {first_name}.".format(first_name="Tom")
    print(text)  # Hello, Tom.

    info = "Name: {name}\t Age: {age}".format(name="Bob", age=23)
    print(info)  # Name: Bob  Age: 23

    info = "Name: {0}\t Age: {1}".format("Bob", 23)
    print(info)  # Name: Bob  Age: 23

    text = "Hello, {0} {0} {0}.".format("Tom")
    print(text)  # Hello, Tom Tom Tom

    welcome = "Hello {:s}"
    name = "Tom"
    formatted_welcome = welcome.format(name)
    print(formatted_welcome)  # Hello Tom

    source = "{:d} символов"
    print(source.format(5000))  # 5000 символов

    source = "{:,d} символов"
    print(source.format(5000))  # 5,000 символов

    number = 23.8589578
    print("{:.2f}".format(number))  # 23.86
    print("{:.3f}".format(number))  # 23.859
    print("{:.4f}".format(number))  # 23.8590
    print("{:,.2f}".format(10001.23554))  # 10,001.24
    print("{:10,.2f}".format(10001.23554))  #  10,001.24

    print("{:10.2f}".format(23.8589578))  # 23.86
    print("{:8d}".format(25))  # 25

    number = .12345
    print("{:%}".format(number))  # 12.345000%
    print("{:.0%}".format(number))  # 12%
    print("{:.1%}".format(number))  # 12.3%

    number = 12345.6789
    print("{:e}".format(number))  # 1.234568e+04
    print("{:.0e}".format(number))  # 1e+04
    print("{:.1e}".format(number))  # 1.2e+04

    info = "Имя: %s \t Возраст: %d" % ("Tom", 35)
    print(info)  # Имя: Tom     Возраст: 35

    number = 23.8589578
    print("%.2f  - %e" % (number, number))  # 23.86  - 2.385896e+01
    print("%10.2f  - %e" % (number, number))  #      23.86  - 2.385896e+01
    #print("%0,.2f  - %e" % (number, number))


if __name__ == "__main__":
    main()
