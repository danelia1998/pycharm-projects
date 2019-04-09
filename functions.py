import main

def askingMarkets(markets,answerMarket):
    print("there are next markets in our service : ", markets," enter which one is better for you !")
    answerMarket.append(input("Write name of market : ").lower())
    if str(answerMarket[0]) in markets:
        return answerMarket
    else:
        print("write it again ! ")
        return askingMarkets(markets, answerMarket)
def askingProducts(Products,answerMarket):
    nikora = ["cheese","bread","salad","xachapuri","cake","fish","egg"]
    goodwill = ["cheese","bread","salad","xachapuri","cake","fish","egg"]
    zghapari = ["cheese","bread","salad","xachapuri","cake","fish","egg"]
    carefour = ["cheese","bread","salad","xachapuri","cake","fish","egg"]
    answerProducts = []
    textFile = open("SaveData.txt","w")
    PlaceOfBuying = []
    if answerMarket[0] == "nikora":
        print("magaziashi aris es produqtebi : ",nikora,)
        answerProducts.append(input("daweret im produqtis saxelwodeba romelic gnebavt sheidzinot :").lower())
        PlaceOfBuying.append("nikora")

        if answerProducts[0] not in nikora:
            print(answerProducts[0],nikora)
            return askingProducts(Products , answerMarket)
        else:
            Products.append(answerProducts[0])
            print(Products)
            print("kidev gnebavt rame? y/n ")
            ask = input(" : ").lower()
            if ask == "y":
                return Products,askingProducts(Products,answerMarket)

    elif answerMarket[0] == "goodwill":
        print("magaziashi aris es produqtebi : ", goodwill, )
        answerProducts.append(input("daweret im produqtis saxelwodeba romelic gnebavt sheidzinot :").lower())
        PlaceOfBuying.append("goodwill")

        if answerProducts[0] not in goodwill:
            return askingProducts(Products, answerMarket)
        else:
            Products.append(answerProducts[0])
            print("kidev gnebavt rame? y/n ")
            ask = input(" : ").lower()
            if ask == "y":
                return Products, askingProducts(Products, answerMarket)
    elif answerMarket[0] == "zghapari":
        print("magaziashi aris es produqtebi : ", zghapari, )
        answerProducts.append(input("daweret im produqtis saxelwodeba romelic gnebavt sheidzinot :").lower())
        PlaceOfBuying.append("zghapari")

        if answerProducts[0] not in zghapari:
            return askingProducts(Products, answerMarket)
        else:
            Products.append(answerProducts[0])
            print("kidev gnebavt rame? y/n ")
            ask = input(" : ").lower()
            if ask == "y":
                return Products, askingProducts(Products, answerMarket)

    else:
        print("magaziashi aris es produqtebi : ", carefour, )
        answerProducts.append(input("daweret im produqtis saxelwodeba romelic gnebavt sheidzinot :").lower())
        PlaceOfBuying.append("carefour")

        if answerProducts[0] not in carefour:
            return askingProducts(Products, answerMarket)
        else:
            Products.append(answerProducts[0])
            print("kidev gnebavt rame? y/n ")
            ask = input(" : ").lower()
            if ask == "y":
                return Products, askingProducts(Products, answerMarket)

    print("Your cart : ",Products)
    askingForSave = input("Do you wanna save your cart in TxT file? y/n").lower()

    if askingForSave == "y":
        textFile.write(PlaceOfBuying[0])
        textFile.write(str(Products))

    textFile.close()



