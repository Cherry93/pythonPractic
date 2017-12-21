# 正则表达式的元字符
import  re


# 匹配单个字符与数字
'''
.  表示匹配任意字符,  但是除了换行符以外
[34578]   表达匹配 3或者4或5或7或8
[abc]     表示匹配 a或者b 或者c
[a-z]     表示匹配所有的小写字母 a - z
[A-Z]     匹配大写的字母
[0-9a-zA-Z]  表示所有的数字或字母
[0-9a-zA-Z_]  表示所有的数字或字母或者下划线

[^345]   ^ 表示取反,  此处表示除了3,4,5以外的所有字符
[^a-z]  除了所有的小写字母以外

\d    注意是反斜杠, 表示所有的数字,  相当于[0-9]
\D    表示多有的非数字    相当于 [^0-9]
\w    表示所有的数字字母下划线   相当于 [0-9a-zA-Z_]
\W    表示除 数字字母下划线 以外的所有字符, 相当于[^0-9a-zA-Z_]
\s    表示匹配 空格,换行,回车,制表,换页 符     相当于 [ \n\r\t\f]
\S    表示除 空格,换行,回车,制表,换页 符  之外的符号 相当于 [^ \n\r\t\f]


'''
# res = re.match(".","abc")
# res = re.match(".","*bc")
# res = re.match(".","\nbc")
# res = re.match(".",".bc")
# res = re.match("1[34578]","13")
# res = re.match("1[34578]","23")
# res = re.match("1[34578]","18")
# res = re.match("[a-z]","Abc")
# res = re.match("[a-z]","Abc",re.I)
# res = re.match("[^345]","1bc")
# res = re.match("\d","9bc")
# res = re.match("\W","$bc")
# print(res)

# 正则表达式的边界字符
'''
 以什么开始,以什么结尾, 判断单词是否以什么结尾
^  注意 ^ 在[^ ]表示取反, 单独使用时表示以 ^ 后的字符开始,
    在re.M模式下,如果换行,则会从换行开始处再一次匹配
$  表示以 $ 前的字符结束, re.M模式会影响
\A  表示以 \A 后的字符开始   re.M不会受影响
\Z  表示以 \Z 前的字符结束   re.M 不会受影响
\b  表示是否是单词的结尾,  如: er\\b 表示会匹配nerver 中末尾的er,不会匹配中间的er字符,当nerver在字符串的末尾时也可以匹配
\B  表示非单词的结尾      如:er\\B 表示会匹配nerver中间的er字符,不会匹配单词末尾的er
'''

# res = re.findall("^123.","123rer123e")
# res = re.findall("123$","123rer123")
# res = re.findall("^123$","123")
# res = re.findall("\A123","12rer123e")
# res = re.findall("123\Z","12rer123")

# res = re.findall("^wen","wen is a good man\nwen is a nice man")
# res = re.findall("\Awen","wen is a good man\nwen is a nice man")

# res = re.findall("^wen","wen is a good man\nwen is a nice man",re.M)
# res = re.findall("\Awen","wen is a good man\nwen is a nice man",re.M)

# re.findall("\A")
# res = re.findall("er\\b","i nerver like girl")
# res = re.findall("er\\b","i nerve like girl nerver")
# print(res)
#

'''
# 匹配字符的数量设置
说明:  x,y,z 表示的是任意的字符,  m,n  表示数量,m,n都是正整数

x?  表示匹配0个或者1个x
x*  表示0个或者任意多个x
x+  表示的1个或者多个

x{n} 表示匹配n个x
x{n,m}  表示可以匹配至少n个最多m个x
x{n,}   表示匹配至少n个x
'''

res = re.findall("a?","wen is a good man")  #--- 非贪婪
# res = re.findall("a*","wen is aa good maaan")  #尽可能多的去匹配, --- 贪婪模式
# res = re.findall("a+","wen is aa good maaan")  # 贪婪模式
# res = re.findall("a{2}","wen is a good maaaan")
res = re.findall("a{2,}","wen is a good maaaan")  # 贪婪
res = re.findall("a{2,3}","wen is a good maaaan")
print(res)

'''
cn  或者 com
mail163Pattern = "\w+@163\.((com)|(cn))"


(xyz)  表示把xyz看作一个整体
x|y    表示x或者y

'''













