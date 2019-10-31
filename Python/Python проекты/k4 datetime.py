import sys
from datetime import datetime

format_time = '%H:%M:%S'
# datetime.strptime(time2, format)

# logs = sys.stdin.readlines()
values = {}
count = 1
with open("dataset_267210_1.txt", "r", encoding="utf-8") as infile:
    for log in infile:
        # print(log.split(' ')[0])
        values[log.split(' ')[1]] = values.get(log.split(' ')[1], [])
        values[log.split(' ')[1]].append((datetime.strptime(log.split(' ')[0], format_time), count))
        count += 1
# print(values)
id_values = []
# print(values[99], values[100])
for item in values.items():
    # print(item)
    for i in range(1, len(values[item[0]]) - 1):
        # print((values[i] - values[i - 1]).total_seconds())
        if (values[item[0]][i][0] - values[item[0]][i - 1][0]).total_seconds() > 3:
            # print("1000000000000")
            id_values.append(values[item[0]][i - 1][1])

# sys.stdout.write(" ".join(id_values))
for id_val in id_values:
    sys.stdout.write(str(id_val) + " ")
# sys.stdout.write(str(sorted(id_values))[1:-1])
