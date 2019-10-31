import sys

logs = sys.stdin.readlines()

# logs = ['Total processor utilization across all cores: 46',
#         'Total processor utilization across all cores: 62',
#         'Total processor utilization across all cores: 53',
#         'Total processor utilization across all cores: 64',
#         'Total processor utilization across all cores: 73']

log_value = []
for log in logs:
    print(log)
    log_value.append(int(log.split(' ')[-1]))
# print(sum(log_value))
avg = sum(log_value) / len(log_value)
# print(avg)

max_value = avg + avg * 0.1
min_value = avg - avg * 0.1
count_error = 0
for log_val in log_value:
    if not((log_val <= max_value) and (log_val >= min_value)):
        # print(log_val)
        count_error += 1
sys.stdout.write(str(count_error))
