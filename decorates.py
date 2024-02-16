# this is with out args
# def Greet(fx):
#     def mfx():
#         print("hello , monirul ")
#         fx()
#         print("thanks for use our website")
#     return mfx
# @Greet
# def hello():
#     print("your function")
#
# hello()

# this is with args
def say_hello(fx):
    def mfx(*args, **kwargs):
        print("this is the beggining")
        fx(*args, **kwargs)
        print("this is the end")
    return mfx
@say_hello
def add(a,b):
    print (a+b)


add(2,3)