#先转成一个字符串的形式
def decTohex(decValue):
    hex = ""
    while decValue !=0:#直到他的商为0
        hexValue = decValue%16#一个十进制数除以16的余数
        hex = toHexChar(hexValue) + hex #再把余数转成十六进制的字符串
        decValue = decValue //16
    return hex
#再把字符串转成十六进制
def toHexChar(hexValue):
    if 0 <=hexValue <=9:
        return chr(hexValue+ord('0'))
    else:
        return chr(hexValue - 10 +ord('A'))

def main():
  decValue = eval(input("请输入一个十进制数:"))
  print("这个十六进制是:",decTohex(decValue))

main()