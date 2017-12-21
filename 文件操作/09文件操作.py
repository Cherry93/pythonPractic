'''

  (1) 在任意位置创建一个.py文件，如'D:/编程练习/python练习/Week2_02.py'
     (2) 在D盘下创建一个文件Blowing in the wind.txt，即‘D:\Blowing in the wind.txt’
     其内容是：
How many roads must a man walk down
Before they call him a man
How many seas must a white dove sail
Before she sleeps in the sand
How many times must the cannon balls fly
Before they're forever banned
The answer my friend is blowing in the wind
The answer is blowing in the wind
     (3) 在文件头部插入歌名“Blowin’ in the wind”
     (4) 在歌名后插入歌手名“Bob Dylan”
     (5) 在文件末尾加上字符串“1962 by Warner Bros. Inc.”
     (6) 在屏幕上打印文件内容，最好加上自己的设计
     (7) 以上每一个要求均作为一个独立的步骤进行，即每次都重新打开并操作文件
'''
f= open("Blowing in the wind.txt",mode="w",encoding="utf-8")
f.write("How many roads must a man walk down\n")
f.write("Before they call him a man\n")
f.write("How many seas must a white dove sail\n")
f.write("Before she sleeps in the sand\n")
f.write("How many times must the cannon balls fly\n")
f.write("Before they're forever banned\n")
f.write("The answer my friend is blowing in the wind\n")
f.write("The answer is blowing in the wind\n")
f.close()

with open("Blowing in the wind.txt",mode="r+",encoding="utf-8") as rf:
    srt = rf.readlines()
    srt.insert(0,"Blowin’ in the wind\n")
    rf.seek(0,0)
    rf.writelines(srt)


