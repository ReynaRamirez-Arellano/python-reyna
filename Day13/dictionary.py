'''
딕셔너리(dictionarty)
-파이썬에서 사용하는 자료구조 중 하나
-key와 value 쌍으로 이루어져 있음
-중괄호를 이용함{}
indexing 가능함 key 값을 이용해서
indexing method 이용가능
# '''
# height={'서현':160,'하율':140,'유래':153}
# print(height)

# print(height.get("하율"))
# print(height.keys())
# height.update({"하율":165})
# height["하율"]=130
# print(height)
# height.update({"선생님":180})
# print(height)
# height["아인"]=170
# del height["선생님"]
# del height["아인"]
# print(height)
# print("선생님" in height)
# print("하율" in height)
for i in range(11):
    fruits={"오랜지":30,"바나나":20,"사과":50}
    fruit=input("과일 상점 입니당. 어떤 과일을 드릴까여??@^@:")
    if fruit in fruits:
        print(f"{fruit}는 {fruits[fruit]}개 있습니당!!")
else:
    print(f"죄송하지만 저희 상점에는 {fruit}이 없어용ㅠ")
    