



def func(functions):
    def something(**kwargs):
        list = [value for value in kwargs['user_input'] if value in "1234567890"]
        return print(list)





@func
def takeMe(**kwargs):
    print()


takeMe(user_input=input("...."))



