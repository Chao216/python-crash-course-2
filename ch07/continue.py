# continue 会忽略余下代码，重新回头开始。

current = 0

while current < 1000:
    current += 1

    if current % 2 == 0:# 如果能被2整除，下面的代码就不执行，继续 +1
        continue
    print(current)
