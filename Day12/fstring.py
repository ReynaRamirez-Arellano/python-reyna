'''
f-string 사용법
-python 표현방식 중 하나
str="오늘은 금요일"
fstr=f"내일은 토요일"
print(fstr)
print(str)
--------------------------
입력(input)<->출력(print)
'''
# age=19
# name="뉴진스"
# print(str)
# fstr2=f"내 나이는 {age}이고, 이름은 {name}입니다"
# print(fstr2)

# animal="고양이"
# school="초등학생"
# print(str)
# fstr2=f"내 나이는 {animal}이고, 이름은 {school}입니다"
# print(fstr2)
# for i in range(3){
# 입력한거=input("나이를 입력하세요:")
# print(f"당신의 나이는 {입력한거}이군요")}
# for i in range(3):
#     gender=input("성별을 알려주세요(남/여):")
#     name=input("이름을 알려주세요:")
#     print(f"당신은 {gender}이고, 이름은 {name}이네요. 반가워요!")
for i in range(5):
    num1=input("첫 번쨰 숫자를 넣어주세요:")
    num2=input("두 번째 숫자를 넣으세요:")
    print(f"두 수의 합은{int(num1)+int(num2)}입니다")