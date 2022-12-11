import time

def calProd():
    # calculate product od first 1,000,000 numbers.

    product = 1
    for i in range(1, 1000000):
        product = product * i
        print(f"this is the{i}th calculation")
    return product

start_time = time.time()

prod = calProd()

end_time = time.time()

print(f"the result is {len(str(prod))} digits long\n")
print(f"the process took ({end_time - start_time}) seconds")
