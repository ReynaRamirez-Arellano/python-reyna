
# a=[1,2,3]
# a.insert(1,100)
# print(a)
# a=[]
# print(a.index(2))
# print(a.index(3))
# b=["가","나","다","나"]
# print(b.index("나"))
# a=["가","나","다","나"]
# print(a.count("나"))
# ***
# a=10
# b="하율"
# c=["사과","배","바나나"]
# d=[10,20,30]
# e=["축구",2,"야구",3]
# ***
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# print(d[0]+d[1])
# print(d[2]//d[0])
# print(d[-1]-d[1])

# 요일=["일요일","월요일"]
# print(요일)
# 요일.append("화요일")
# print(요일)
# 요일.pop()
# print(요일)
# 요일.remove("일요일")
# print(요일)

# fruit=["orange","watermelon","banana","apple"]
# fruit.sort()
# print(fruit)
# fruit.reverse()
# print(fruit)

# 출력할꺼=[]
# for i in range(10,21):
#     if i%3==0:
#         출력할꺼.append(i)
# 출력할꺼.reverse()
# print(출력할꺼)

# 출력할꺼=[]
# for i in range(1,20):
#     if i%3==0:
#         출력할꺼.append(i)
# 출력할꺼.reverse()
# print(출력할꺼)

# 출력할것=[]
# for i in range(50,100):
#     if i%3==0:
#         if i%4==0:
#             출력할것.append(i)
# 출력할것.reverse()
# print(출력할것)

# print(출력할꺼[0]*출력할것[-1])
def 구구단(입력):
    출력할것=[]
    for i in range(1,10):
        출력할것.append(i*입력)
    print(출력할것)
구구단(3)
구구단(8)
