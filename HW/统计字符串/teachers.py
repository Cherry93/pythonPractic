'''
定义教师类，属性包括姓名、职称、工资，创建1000个实例，使用pickle写入teachers.dat并再次读出；

'''
import pickle
from tkinter import filedialog
class Teachers:

    def __init__(self,name,call,rmb):
        self.name =name
        self.call = call
        self.rmb = rmb
    def __str__(self):
        return "name:"+str(self.name)+"call:"+str(self.call)+"rmb:"+str(self.rmb)
c = Teachers("王小星","高级",1000)
#print(c)


def writeDemo():
    global file

        #print(c)
    savePath = filedialog.asksaveasfilename()
    file = open(savePath, mode="ab")
    for i in range(10):
        data = c
    pickle.dump(data, file)
    file.close()

writeDemo()

def readMode():
    global file
    print(data)
with open(filedialog.askopenfilename(), mode="rb") as file:
    for i in range(10):
     data = pickle.load(file)
     print(data)
readMode()

