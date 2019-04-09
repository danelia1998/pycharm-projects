class Subject:

    def __init__(self, name, credits, averageMark):
        self.name = name
        self.credits = credits
        self.averageMark = averageMark
        print("{} faculty costs {} credits".format(self.name, self.credits))

    def Checker(self):
        if self.averageMark > 51:
            print("Your M.average is higher than 51 ({}), you can choose {} faculty!".format(self.averageMark,self.name))
        else:
            print("You cant join this {} faculty coz your aver.mark is lower than minimum {}! ".format(self.name,self.averageMark))


subject = Subject("chemistry",38,44)
subject2 = Subject("dentist",38,53)
subject3 = Subject("computer science",20,52)
subject.Checker()
subject2.Checker()
subject3.Checker()


