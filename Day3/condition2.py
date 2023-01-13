'''
조건문2(while)
while 조건:
    실행할 코드 작성
1.조건이 참이면, 아래 코드가 실행됨
2.조건이 거짓이면, while이 끝남
3.for 조건문은 while 조건문으로 바꿀 수 있다
'''
# for i in range(3):
#     print("Hi")

# i=0
# while i<3:
#     print("hi")


# while True:
#     print("왜이래")

# while False:
#     print("엥?")

#Q1
# i=1
# while i<11:
#     print(i)
#     i+=1
#Q2
# i=1
# while i<11:
#     if i%2==0:
#         print(i)
#     i+=1
#Q3
# i=1
# sum=0
# while i<11:
#     if i%3==0:
#         sum+=i
#         print(sum)
#     i+=1
#Q4
# i=50
# while i<100:
#     if i%3==0:
#         if i%7==0:
#             print(i)
#     i+=1
#Q5
i=1
sum=1
while i<20:
    if i%2==0:
        sum*=i
    i+=1
print(sum)