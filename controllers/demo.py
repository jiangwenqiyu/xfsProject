import os
import psutil
import time
import wmi


def getcpu():
    # data = psutil.virtual_memory()
    # total = data.total
    # free = data.available
    #
    # totalStr = "总内存:{}G".format(round(total / 1024 / 1024 / 1024, 0))
    # freeStr = "可用内存:{}G".format(round(free / 1024 / 1024 / 1024, 0))
    # memUsage = "内存占用:{}".format(((total - free) / total) * 100)
    # cpu = " CPU:%.2f" % psutil.cpu_percent(interval=1)
    # cpuNum = 'CPU个数:{}'.format(psutil.cpu_count(logical=False))
    # print(totalStr)
    # print(memUsage)
    # print(cpu)
    # print(cpuNum)


    # cpuinfo = wmi.WMI()
    # for cpu in cpuinfo.Win32_Processor():
    #     print("您的CPU序列号为:" + cpu.ProcessorId.strip()) # BFEBFBFF0999906C1
    #     print("您的CPU名称为:" + cpu.Name) # 11th Gen Intel(R) Core(TM) i7-1165G7 @ 2.80GHz
    #     print("您的CPU已使用:%d%%" % cpu.LoadPercentage) # 17%
    #     print("您的CPU核心数为:%d" % cpu.NumberOfCores) # 4
    #     print("您的CPU时钟频率为:%d" % cpu.MaxClockSpeed) # 1690
    print(psutil.cpu_count())
    print(psutil.cpu_count(logical=False))

    p = psutil.Process()
    print(p.memory_full_info())


while True:
    getcpu()
    time.sleep(2)
    break




