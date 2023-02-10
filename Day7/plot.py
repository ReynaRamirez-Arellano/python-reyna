'''
막대그래프 그리기
-모듈설치 필요함
-python에서 모듈을 설치할 떄는 pip명령어를 쓴다
-터미널 창에서"pip install matplotlib"을 입력
'''
import matplotlib.pyplot as plt
fruits=["apple","bluebarry","cherry","orange"]
counts=[5,10,7,12]
barcolor=["#FF0202","#7764CF","#FF2168","#FFBC1E"]
창,내용=plt.subplots(1,3)
내용[0].bar(fruits,counts,color=barcolor)
내용[1].barh(fruits,counts,color=barcolor)
내용[2].barh(fruits,counts,color=barcolor)
plt.show()
