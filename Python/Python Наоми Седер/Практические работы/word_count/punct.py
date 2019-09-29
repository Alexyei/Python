def delpunct(line):
    line = line.lower()
    line = line.replace("--", " ")
    table = line.maketrans(",.;!?:", " " * 6)
    line = line.translate(table)
    return line
