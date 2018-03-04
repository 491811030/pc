import random
x = random.random()##省略random.seed()系统时间为种子
x =[random.random() for _ in range(1000)]
print(x)