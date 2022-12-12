import timeit


res = timeit.timeit(stmt="[i for i in range(100000000)]", number=100)
print(res)

