import numpy as np
# a=np.array([1,2,3])
# print(a)
# b=np.array([4,5,6])
# print(a+b)
# c=[1,2,3]
# d=[4,5,6]
# print(c+d)

# b=np.array([4,5,6])
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
# my_image=img.imread("./python-reyna/Day8/hy.png")
# plt.imshow(my_image)
# plt.show()

my_matrix=np.array([
[[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0]],
[[255,0,0],[255,0,0],[255,255,255],[255,0,0],[255,0,0]],
[[255,0,0],[255,255,255],[255,255,255],[255,255,255],[255,0,0]],
[[255,0,0],[255,0,0],[255,255,255],[255,0,0],[255,0,0]],
[[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0]],
])
plt.imshow(my_matrix)
plt.show()