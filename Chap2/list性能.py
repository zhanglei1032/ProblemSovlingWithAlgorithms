#列表的4种扩充方式
def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))


import timeit
from timeit import Timer


#from __main__ import test1 这个语句将来自 __main__命名空间的函数test1
#调用到为进行时间测量而建立的timeit命名空间中去
#timeit默认运行一百万次，也可用number指定次数
t1 = Timer("test1()", "from __main__ import test1")
t2 = Timer("test2()", "from __main__ import test2")
t3 = Timer("test3()", "from __main__ import test3")
t4 = Timer("test4()", "from __main__ import test4")

print("concat: ", t1.timeit(number=1000), "ms")
print("append: ", t2.timeit(number=1000), "ms")
print("comprehension: ", t3.timeit(number=1000), "ms")
print("list function: ", t4.timeit(number=1000), "ms")


#运行结果
#concat:  1.3814115093601913 ms
#append:  0.07480978478253064 ms
#comprehension:  0.0306077076217548 ms
#list function:  0.012014990815657711 ms


#操作              Big-O
#index[x]           O(1)
#index[x] = y       O(1)
#append             O(1)
#pop()              O(1)
#pop(i)             O(n)        删除第i个元素后，后续元素都前移一位
#insert(i, item)    O(n)        元素i以后的元素都需要后移一位
#del operator       O(n)
#iteration          O(n)
#contains(i)        O(n)
#get slice[x:y]     O(k)
#del slice          O(n)
#set slice          O(n + k)
#reverse            O(n)
#concatenate        O(k)        两个列表相加取决于第二个列表的长度（把第二个列表的元素逐个添加都第一个列表）
#sort               O(nlogn)
#multiply           O(nk)
