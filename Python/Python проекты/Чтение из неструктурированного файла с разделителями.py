import datetime

data_text = open("temp_data_pipes_00a.txt")
header = data_text.readline()
# state, month_day_year,avg_daily , record_count\
data = [[record[0], datetime.datetime.strptime(record[1], '%Y/%m/%d'), float(record[2]), int(record[3])] for record in
        (item.split('|') for item in data_text)]
print(data)
