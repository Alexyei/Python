import sys
import string


def fk10(str_val, j):
    for h in range(j-1, -1, -1):
        str_val = str_val.replace(string.ascii_lowercase[h] + string.ascii_lowercase[h], "")
        return fk10(str_val, h)
    return str_val


# line = sys.stdin.readline()
line = "GgiyYtTIEeLltSsuizZIgGkVUuUzZuJyYbUucUuCBjSkHhKAasNKknm"
line = line.lower()

min_gen1 = len(line)
for char in string.ascii_lowercase:
    temp_line = line.replace(char, "")
    for k in range(0, len(string.ascii_lowercase)):
        temp_line = temp_line.replace(string.ascii_lowercase[k] + string.ascii_lowercase[k], "")
        temp_line = fk10(temp_line, k)
    min_gen1 = min(min_gen1, len(temp_line))
print(min_gen1)

# import sys
# import string
#
#
# def fk10(temp_str, min_gen11, char1):
#     for k in range(0, len(string.ascii_lowercase)):
#         if string.ascii_lowercase[k] == char1:
#             break
#         temp_str = temp_str.replace(string.ascii_lowercase[k] + string.ascii_lowercase[k], "")
#         if k:
#             temp_str = fk10(temp_str, min_gen11, string.ascii_lowercase[k - 1])[0]
#         else:
#             min_gen11 = min(min_gen11, len(temp_str))
#             return temp_str, min_gen11
#
#
# # line = sys.stdin.readline()
# line = "CdabAcCaCBAcCcaDA"
# # print("aabcddddada".replace('dd', ""))
# min_gen1 = len(line)
# min_gen2 = len(line) - 1
# # temp_line = ""
# # while min_gen1 != min_gen2:
# for char in string.ascii_lowercase:
#     temp_line = line.lower().replace(char, "")
#     for double_char in string.ascii_lowercase:
#         temp_line = temp_line.replace(double_char + double_char, "")
#         min_gen1 = min(min_gen1, len(temp_line))
#         temp_line, min_gen1 = fk10(temp_line, min_gen1, double_char)
#     # for char in string.ascii_lowercase:
#     # temp_line = line.lower().replace(char, "")
#     # for i in range(0, len(string.ascii_lowercase)):
#     #     if string.ascii_lowercase[i] == char:
#     #         break
#     #     temp_line = temp_line.replace(double_char + double_char, "")
#     #     min_gen1 = min(min_gen1, len(temp_line))
# sys.stdout.write(str(min_gen1))
