def find_in(data, words):
    IfThereIsNumbers = 0
    for a in data:
        for b in a :
            try :
                int(b)
            except ValueError :
                continue
            else:
                IfThereIsNumbers += 1
    if IfThereIsNumbers > 1:
        print("You have number in text :( ")
    num = 0
    countVowel = 0
    count = 0
    for each in data:
        num += 1
        number = 0
        for i in words:
            print(num,"winadadebashi aris :",each.count(i),words[number])
            number +=1
    for one in data:
        for letter in one:
            print(letter)
            if letter in "a,e,i,o,u":
                countVowel += 1
            elif letter in "b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z":
                count += 1
    print("am winadadebebshi aris : ",countVowel,"xmovani da : ",count,"tanxmovani")




def main():
    data = input("shemoiyvanet sami winadadeba mdzimit gamoyofili").lower().split(",")
    words = ["moon", "sun"]
    find_in(data,words)
if __name__ == '__main__':
    main()
