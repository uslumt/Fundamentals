def salting(obj):
    def _salt(f:str, t:int):
        print(f + " salted " + str(t) + " times")
    return _salt

@salting
def my_menu (fd , tm):
    return fd , tm

steak_menu = my_menu("steak", 2)
