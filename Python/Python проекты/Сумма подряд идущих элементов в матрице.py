data_text = open("kaspersky_sum_in_matrix.txt")
data = [item.split() for item in data_text]
for i in range(0, len(data)):
    for j in range(0, len(data[i])):
        data[i][j] = int(data[i][j])
# print(data)
max_sum = sum(data[0][:5])

# sum in rows top to bottom left to right
for row in data:
    for i in range(0, len(row) - 4):
        max_sum = max(max_sum, sum(row[i:i + 5]))
print(max_sum)
# sum in columns top to bottom left to right
for i in range(0, len(data)):
    column = [row[i] for row in data]
    for j in range(0, len(column) - 4):
        max_sum = max(max_sum, sum(column[i:i + 5]))
print(max_sum)
# sum in diagonal left top corner to right bottom corner bottom to top
# for i in range(4, len(data) - 4):
#     diagonal = []
#     for j in range(0, i + 1):
#         diagonal.append(data[i - j][j])
for k in range(0, len(data) - 4):
    two_diag = [[], []]
    for i in range(0, len(data) - k):
        two_diag[0].append(data[i][len(data) - i - 1 - k])
        two_diag[1].append(data[i + k][len(data) - i - 1])
    for diagonal in two_diag:
        for j in range(0, len(diagonal) - 4, 5):
            max_sum = max(max_sum, sum(diagonal[j:j + 5]))
print(max_sum)
# sum in diagonal left bottom corner to right to corner top to bottom
# for i in range(len(data) - 4, 4, -1):
#     diagonal = []
#     for j in range(0, len(data) - i + 1):
#         diagonal.append(data[i + j - 1][j])
#         print(i + j, j)
for k in range(0, len(data) - 4):
    two_diag = [[], []]
    for i in range(0, len(data) - k):
        two_diag[0].append(data[i][i + k])
        two_diag[1].append(data[i + k][i])
    for diagonal in two_diag:
        for j in range(0, len(diagonal) - 4, 5):
            max_sum = max(max_sum, sum(diagonal[j:j + 5]))

print(max_sum)
