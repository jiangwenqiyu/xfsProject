str = input('输入城市:')
total = str.split(';')


city = ['北京', '上海', '天津']
to = list()
for i in total:
    temp = dict()
    i = i.split(',')
    temp[i[0]] = int(i[1])
    to.append(temp)


beijing  = 0
shanghai = 0
tianjin = 0

for obj in to:
    for key in obj:
        if key == '北京':
            beijing += obj[key]
        elif key == '天津':
            tianjin += obj[key]
        else:
            shanghai += obj[key]

print('北京:{}'.format(beijing))
print('天津:{}'.format(tianjin))
print('上海:{}'.format(shanghai))










