'''
집합의 특징
1.순서가 없음
2.중복이 없음
3.연산 가능{교집합(intersection),합집합(union),차집합(difference)}
집합-
'''
# a={1}
# print(a)
# print(type(a))
# b=[2]
# print(b)
# print(type(b))
# c=(3,4)
# print(c)
# print(type(c))
# d={4:"a",5:"b"}
# print(d)
# print(type(d))
# e=[100,200,300]
# f=(500,600,700)
# print(e[2])
# print(f[1])
# print(e[1:3])
# print(f[:1])

# A={1,2,3}
# B={3,3,4,4,4,5,5}
# print(A)
# print(B)
# print(A-B)
# print(B-A)
# print(A&B)
# print(A|B)

# fruit={"lemon","banana","apple","cherry"}
# red={"fire","tomato","apple","cherry"}
# print(fruit|red)
# print(fruit&red)
# print(fruit-red)
# print(red-fruit)

A={1,2,3,4,6,12}
B={1,2,3,4,6,9,12,18,36}
CD=A&B
GCD=max(CD)
LCM=GCD*(24/GCD)*(36/GCD)
print(LCM)
print(GCD)

A={1,2,4,7,14,28}
B={1,2,3,6,7,14,42}
CD=A&B
GCD=max(CD)
LCM=GCD*(28/GCD)*(42/GCD)
print(LCM)
print(GCD)
print(CD)

A={1,2,4.6,8,12,24,48}
B={1,2,5,10,50}
C={1,2,13,26}
CD=A&B&C
GCD=max(CD)
print(GCD)
print(CD)