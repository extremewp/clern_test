import os

# os.mkdir("d")
# print(os.path.exists("d"))
# os.getcwd()
# os.removedirs("d")
if not os.path.exists("d"):
    os.mkdir("d")
if not os.path.exists("d/lala.txt"):
    y = open("d/lala.txt", "w")
    y.write("我日你妈卖批")
    y.close()
    os.path
