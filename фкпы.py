def testy(arg1,arg2,arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

args = ("two", 3,5)
kwargs = {"args3": 3 , "args2":"two" , "arg1":5 }
testy(*args)
testy(*kwargs)
