import random
rand_num = random.random()
rand_num = 10000*rand_num

n = random.randint(0,int(rand_num))

random_number_list = list()
var = list()

i = 1
while i<rand_num:
    random_number_list.append(i)
    i +=1

random.shuffle(random_number_list)

print(random_number_list)
print(rand_num)
print(n)

i = 0
while i<n:
    var.append(random_number_list[i])
    i += 1

print(var)

m = max(var)
#formül
N = m+int(m/n)-1

print("toplam = {} \ntahmin = {}".format(rand_num,N))


