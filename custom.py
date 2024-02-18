import time

def test():
    print("finally calling test")

def say_hello():
    test()
    time.sleep(2)
    print("update?!!")

