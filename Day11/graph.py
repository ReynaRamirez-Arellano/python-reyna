import matplotlib.pyplot as plt
# plt.figure()
# plt.plot([1,2,3],[1,2,3],[1,2,3],[2,4,6],[1,2,3],[0.5,1,1.5])
# plt.show()

# plt.figure()
# xl=[1,2,3]
# yl=[1,2,3]
# plt.plot(xl,yl,'YS')
# plt.show()

# plt.figure()
# xl=[1,2,3]
# yl=[3,5,7]
# x2=[1,2,3]
# y2=[0.25,0.5,0.75]
# plt.plot(xl,yl,'r',x2,y2,'ko')
# plt.show()

# plt.figure()
# xl=[]
# yl=[]
# for i in range(-10,11):
#     xl.append(i)
#     yl.append(i**3+i*4+2)
# plt.plot(xl,yl,'b')
# plt.show()

plt.figure()
xl=[]
yl=[]
x2=[]
y2=[]
x3=[]
y3=[]
for i in range(-10,11):
    xl.append(i)
    yl.append(i)
    x2.append(i)
    y2.append(i**2)
    x3.append(i)
    y3.append(i**3)
plt.plot(xl,yl,'b',x2,y2,'b',x3,y3,'b')
plt.show()