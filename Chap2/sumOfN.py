import time
def sum_of_n_2(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i
    end = time.time()
    return the_sum, end - start

def sum_of_n_3(n):
    start = time.time()
    the_sum = (n * (n + 1)) / 2
    end = time.time()
    return the_sum, end - start

for i in range(5):
    #这里使用*解包返回的tuple
    #print("Sum is {} required {} seconds".format(*sum_of_n_2(10000)))
    print ("Sum is {} required {:.10f} seconds".format(*sum_of_n_3(1000000)))
