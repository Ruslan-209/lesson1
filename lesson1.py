# 1st program
print((9*5)**0,5)

# 2st program
print(9.99 > 9.98 and 1000!=1000.1)

# 3rd program
x = 1234
y = 5678
print(((x%1000)//10)+((y%1000)//10))

# 4th program

z = 13.42
v = 42.13

print(int(z//1) == round((v-int(v))*100) or round(z-int(z))*100 == int(v//1))

z1 = int(z)
v1 = int(v)

z2 = int(z1-z)*100
v2 = int(v1-v)*100

print(z2==v2)