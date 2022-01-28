fileread=open("/home/luser/programming/python/reading.txt","r")
for line in fileread.readlines():
    print(line)

fileread.close()
