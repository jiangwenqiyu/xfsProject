import datetime
import  time


current = datetime.datetime.now()
createTime = current.strftime("%Y-%m-%d %H:%M:%S")
backContent = current.strftime("%Y%m%d%H%M%S{}".format(str(int(time.time()*1000))[-3:]))

print(current)
print(createTime)
print(backContent)
print(str(int(time.time()*1000))[-4:])