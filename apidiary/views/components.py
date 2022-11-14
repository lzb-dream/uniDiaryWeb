import time
def conversionTime(timespec):
    add_time = time.localtime(int(timespec) / 1000)
    writeTime = time.strftime('%Y-%m-%d %H:%M:%S', add_time)
    return writeTime
