import sys

# logs = sys.stdin.readlines()

logs = ['letrhjuttsrydckpksafswnefddbus',
        'lstshjutteradcqakwlfsgazfueius',
        'ldtshjutciradcrakwvfswazfbeyus',
        'lstshjutteradcqaiwlfswazfuebus',
        'lstshjutteredcqarslfswazuuebfs',
        'lstshuxtteradeqafwlfszanfuebus',
        'lbtshiutnsvaootakalmpdwzfuemus',
        'lhtshjnttlradcqaiwlfswazfuebus',
        'lsurtjumteradcawawmfswhzfkezus',
        'lsumajustgrkucqajkxbswaziusbzs',
        'lstsojjttebayjqafwlfsaazfuebvx',
        'rstshjutteradmrakwlfsvazkunbus',
        'csdshjuuteradcuarmlfswgjftnbus',
        'lstshjuttehadcbakwlfswazfuebus',
        'lstdhrutteradvyjkwlfswwzouxpgm',
        'lstscjufldradmjskwtfswazfuebus',
        'ustszjutteradcqakwrfswjzfuewus',
        'ystxhjutteysxkqakylxawazfuzbgs',
        'lstshjutteradcqakwlfswazfuebus',
        'lgtnhgutterpdcqakglfgwtzpumbug']
set_value = []
# print(logs)
for str_val in logs:
    set_value.append(str_val)

exit_f = 0
# print(set_value)
# print(len(set_value))
for i in range(0, len(set_value) - 1):
    for j in range(i + 1, len(set_value)):
        # temp_set = set(set_value[i]).intersection(set(set_value[j]))
        # if len(temp_set) == (len(set(set_value[i])) - 1):
        # print(1111)
        # sys.stdout.write(str(set_value[i]))
        count_t = 0
        position = 0
        for t in range(0, len(set_value[i])):
            if set_value[i][t] != set_value[j][t]:
                count_t += 1
                position = t
        if count_t == 1:
            # print(set_value[i])
            # print(set_value[j])
            # print("1111111")
            # for k in range(0, len(set_value[i])):
            #   if set_value[i][k] != set_value[j][k]:
            sys.stdout.write(str(set_value[i][:position]))
            sys.stdout.write(str(set_value[i][position + 1:]))

            # print()
            # print('lstshjutteradcqawlfswazfuebus')
            exit_f = 1
            break
        #exit_f = 1
        #break
    # else:
#          print(len(temp_set), len(set_value[i]))

    if exit_f:
        break
