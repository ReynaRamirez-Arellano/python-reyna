'''
리스트(aka.array)
-데이터를 저장하는 방식 중 하나
-규칙은 대괄호와 쉼표로 구분
-출력시 모두 나타남
-특징1:순서로 안에있는 내용을 선택할 수 있음
    :순서는 0부터 시작(항상)
    :마지막 순서는 -1해도 무방
-특징2:append를 이용해 추가할 수 있음
(메소드 이용)
-특징3:pop을 이용해 삭제할 수 있음
*맨 마지막께 사라짐
-특징4:선택한 값을 지우고 싶을떈 remove 사용
-특징5:정렬(오른차순)할떄 sort 사용
-특징6:정렬(내림차순)할때 reverse 사용
'''
# a=10
# b="하율"
# c=["사과","배","바나나"]
# d=[10,20,30]
# e=["축구",2,"야구",3]
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

출력할꺼=[]
for i in range(1,20):
    if i%2==1:
        출력할꺼.append(i)
출력할꺼.reverse()
print(출력할꺼)

출력할것=[]
for i in range(50,100):
    if i%3==0:
        if i%4==0:
            출력할것.append(i)
출력할것.reverse()
print(출력할것)

print(출력할꺼[0]*출력할것[-1])

