import parent as p
# class Female(p.person):
#     def greeting(self):
#         print(f"Hello,everyone^^")

# class Male(p.person):
#     def greeting(self):
#         print(f"Hi,guys!")


class pencil(p.상품):
    def 가격(self):
        print(f"{self.name}의 한다스의 가격은 {self.price}입니다")

class eraser(p.상품):
    def 지우개가격(self):
        print(f"{self.name}의 한팩의 가격은 {self.price}입니다")