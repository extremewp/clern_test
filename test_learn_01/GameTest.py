# class game:
#     gj = 200
#     xl = 1000
#     def fight(self,enemy_xl,enemy_gj):
#             final_gj = self.xl - enemy_gj
#             enemy_final_gj = enemy_xl - self.gj
#             if final_gj > enemy_final_gj:
#                 print("我赢了")
#             elif final_gj < enemy_final_gj:
#                 print("地方赢了")
#             else:
#                 print("平手")
#
# y = game()
# y.fight(enemy_xl=1000, enemy_gj=300)
import os


class Game:

     def __init__(self,name,student):
         self.name = name
         print(name)
         self.student = student
         print(student)
y = Game("wangwu", "wangwu")
