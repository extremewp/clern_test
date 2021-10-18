import yaml


# def test_demo():
#     for i in range(5):
#
#         yield i
# a = test_demo()
# print(next(a))
# print(next(a))
# print(next(a))
with open("../datas/step_add.yml") as f:
   assss= yaml.safe_load(f)
   print(assss)