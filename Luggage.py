import random as rn
class Luggage:
    
    __price= 250
    
    def __init__(self, owner, weight=0, length= 0, large=0, width=0):
        self.__owner= owner
        self.__weight= weight
        self.__length= length
        self.__large= large
        self.__width= width
        self.__luggcode= []
        self.__register= True
    
    def remove_luggage(self):
        self.__register= False

    def luggage_data(self):
        return self.__owner, self.__weight, self.__large, self.__length, self.__width, self.__register
    
    def luggage_code(self):
        letters= ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R']
        lugg=1
        while lugg !=0:
            code= ''
            for i in range(5):
                code+= letters[rn.randint(0,8)]+str(rn.randint(0,9))
            lugg-=1
            self.__luggcode.append(code)
        return self.__luggcode
    
    def luggage_price(self):
        total= Luggage.__price
        if self.__register == True:
            if 20 >= self.__width and 20 >= self.__large and 20 >= self.__length and 20 >= self.__weight:
                total+=1500
                return f'El precio del registro de la maleta (pequeña) sería de: ${total}'
            elif 40 >= self.__width and 40 >= self.__large and 40 >= self.__length and 40 >= self.__weight:
                total+=2000
                return f'El precio del registro de la maleta (mediana) sería de: ${total}'
            elif self.__width > 40 and self.__large > 40 and self.__length > 60 and self.__weight > 60:
                total+=2700
                return f'El precio del registro de la maleta (grande) sería de: ${total}'
        else:
            return 'No tiene maletas registradas'

    def __repr__(self):
        if self.__register == False:
            return f'{self.__owner} no tiene maletas registradas'
        else:
            return f'Luggage({self.__owner}, {self.__weight}, {self.__length}, {self.__large}, {self.__width})'
    
    def __str__(self):
        if self.__register == False:
            return f'{self.__owner} no tiene maletas registradas'
        else:
            return f'Se tiene registrada la maleta de {self.__owner}. Con un peso de: {self.__weight}, una altura de: {self.__length}, un largo de: {self.__large} y un ancho de: {self.__width}'

if __name__ == '__main__':
    l1= Luggage('MakiMan', 15, 13, 16, 20)
    l2= Luggage('Doctor García', 40, 35, 30, 25)
    l3= Luggage('Baby Boop', 63, 68, 75, 80)
    print(l2.luggage_code())
    l1.remove_luggage()
    print(l1.luggage_price())
    print(l2.luggage_price())
    print(l3.luggage_price())
    print(l3.luggage_data())
    print(repr(l2))
    print(l3)
    print(l1)