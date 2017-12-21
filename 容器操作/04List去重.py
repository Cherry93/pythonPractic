'''

去掉list中重复元素
'''


# a=[1,2,4,2,4,5,6,5,7,8,9,0]
# b = list(set(a))
# print(b)
# c = dict.fromkeys(a,None)
# print(c)
# d = list(c.keys())
# print(d)

mdict = {"name": "zhangsan", "age": 20}
print(type(mdict.items()))#<class 'dict_items'>
for k, v in mdict.items():
 print(k, v)
 '''
 一行代码实现对列表a中的偶数位置的元素进行加3后求和？
 '''
 a = [1, 2, 3, 4, 5]

# print(a[1::2])
# for x in a[1::2]:
list = [-2, 1, 3, -6]
list1 =sorted(list,key = abs)
print(list1)

'''
假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
1、请用sorted()对上述列表分别按名字排序：

2、再按成绩从高到低排序：
'''

L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
#按名字排序
def by_name(t):
    print(t[0])
by_name(L)

# print('sorted by name: ')
# print(sorted(L,key=by_name))


def d(fp):
    def _d(*arg, **karg):
        print("do sth before fp..")
        r = fp(*arg, **karg)
        print("do sth after fp..")
        return r

    return _d
@d
def f(name):
    print("call f:%s"%name)
f("hah")

