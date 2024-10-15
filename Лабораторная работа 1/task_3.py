#o+K3viTHHrAWerK0AJetF+gLV9ir4y9zQQAcKEGpIW4trfw5J+zIsrr6r4jOuSozvip/8u3fBOMR0Dfwt0HcWSYXBz12YqgU6T8RjgUgsdbAORLvu0Bnu5/bHXXMj9pCgl43sD9PDEZoyC8bNHU9J1wElBJE4QtbRd6DbNNGRRQzrXwOdSiFSAqTG539iWzEMlghxiWpPRXKUbRKVZo63rRB0OUIP/hWFnAHiyQet4SbH2ia80lk1Eu12rIxfp8pbMNHnqSoHYTERPqK/tytD2B1I1/pdVzUaXy3uOvzyRlYRfdrfAVZmLw76T2Qu3OTqWnrMI2KxAhOBidxjAc6/oAlJ/6dsfk6lkIGKOVB5TwGFaL/ZYg29FiNLKYn0WKr
def Comands(list_):

    #Finding a middle index of the list
    middle = (len(list_)-1)//2
    Comand_1 = list_[:middle]
    Comand_2 = list_[middle:]
    print("Comand #1: ",Comand_1,'\n')
    print("Comand #2: ", Comand_2)
    return [Comand_1, Comand_2]
#list of players
players=["kukaracha","gamegod","IHATEROBL0xxx","D4nG30Nmaster",
         "LadyWithBeard","KuchiKukan","Toshiba"]
#Print comands
Comands=Comands(players)
