import weatherPortion as w

class main():
    def clothRec(rec):
        
        clothingOption =[['suit jacket', 'sweatshirt', 'sports coat', 'rain jacket'],
                     ['tank tops', 'T-shirts', 'polos', 'dress shirt'],
                     ['shorts', 'sweatpants', 'khakis', 'dress pants', 'jeans'],
                     ['sneakers', 'crocs', 'boat shoes', 'dress shoes']]


        coldClothes = [clothingOption[0][1],clothingOption[1][1], clothingOption[2][4], clothingOption[3][0]] 

        dressClothes = [clothingOption[0][0],clothingOption[1][3],clothingOption[2][3],clothingOption[3][3]]

        warmClothes = [clothingOption[1][0], clothingOption[2][0],clothingOption[3][0]]
        
    
        if rec == "warm":
            print(warmClothes)
        else:
            print(coldClothes)


    
