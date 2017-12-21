# #创建字典
# items=[('name','earth'),('port','80')]
# dict2 = dict(items)
# print(dict2)
#
# dict1 = dict((['name','earth'],['port','80']))
# print(dict1)

#合并两个有序列表
'''
def _recursion_merge_sort2(l1, l2, tmp):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return _recursion_merge_sort2(l1, l2, tmp)


def recursion_merge_sort2(l1, l2):
    return _recursion_merge_sort2(l1, l2, [])

'''
'''
假设有2个有序列表l1、l2，如何效率比较高的将2个list合并并保持有序状态，这里默认排序是正序。
思路是比较简单的，无非是依次比较l1和l2头部第一个元素，将比较小的放在一个新的列表中，以此类推，直到所有的元素都被放到新的列表中。

'''
l1 = [1,3,5,8,4,2]
l2 = [2,4,5,3,6,9,6]
list=[]



