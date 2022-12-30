'''
조건문 
1.If/Else
if 조건:
참일 때 작성
else:
거짓일 때 작성
2.For
for i in range(숫자):
작성
for i in range(시작.끝):
작성
for i in range(시작,끝,중간):
작성
'''
# apple =10
# orange =20
# if apple>orange:
#     print("사과가 큼")
# else:
#     print("오렌지 큼")

# for i in range(1,10):
#     print(i+1)

# for i in range(1,11,2):
#     print(i)

# for i in range(1,11):
#     if i%2==1:
#         print(i)

# for i in range(1,11):
#     if i%2==0:
#         print(i)

# for i in range(20,41):
#     if i%3==0:
#         print(i)

# for i in range(50,100):
#     if i%3==0:
#         if i%4==0:
#             print(i)

# sum=0
# minus=0
# for i in range(1,101):
#     if i%2==0:
#         sum+=i
#     if i%2==1:
#         minus+=i
# print(sum-minus)

sum=1
for i in range(1,21):
    if i%7==0:
        sum*=i
print(sum)
