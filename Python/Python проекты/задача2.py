import sys
log = sys.stdin.readlines()
# log = ['[2019-08-29 13:00:13] 10.64.64.8',
#        '[2019-08-29 13:15:35] 95.213.255.16',
#        '[2019-08-29 14:14:33] 10.64.64.8',
#        '[2019-09-01 14:14:35] 35.228.158.140',
#        '[2019-09-01 14:14:35] 35.228.158.140',
#        '[2019-09-01 15:29:01] 35.228.158.140']

log_count = {}
for line in log:
    ip = line.split(' ')[2]
    log_count[ip] = log_count.get(ip, 0) + 1

sorted_log_count = dict(sorted(log_count.items(), key=lambda item: item[1], reverse=True))
for key in sorted_log_count.keys():
    sys.stdout.write(key+'\n')
