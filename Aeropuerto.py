import random as rn

class FlightInterface:
    
    def __init__(self):
        self.__active= False
    
    def activate_interface(self):
        self.__active= True
    
    def desactivate_interface(self):
        self.__active= False
    
    def is_activate(self):
        return self.__active
    
    def check_interface(self):
        if self.__active == True:
            return 'Activa'
        else:
            return 'Inactiva'
    
    def __str__(self):
        return f'La interfaz de vuelos está en este momento: {self.check_interface()}'
    
    def __repr__(self):
        return f'FlightInterface({self.__active})'
    
class Date:
          
    def __init__(self, day=1, month=1, year=2020):
        self.__day= day
        self.__month= month
        self.__year= year
    
    @property
    def day(self):
        return self.__day
    @day.setter
    def day(self, day):
        self.__day= day
    
    @property
    def month(self):
        return self.__month
    @month.setter
    def month(self, month):
        self.__month= month
    
    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, year):
        self.__year= year
    
    def __repr__(self):
        return f'Date({self.__day}, {self.__month}, {self.__year})'
    
    def __str__(self):
        return f'La fecha de su vuelo es: {self.__day}/{self.__month}/{self.__year}'

class Passenger:
    
    def __init__(self, passname, gender, age):
        self.__passname= passname
        self.__gender= gender
        self.__age= age
        
    @property
    def passname(self):
        return self.__passname
    
    @property
    def gender(self):
        return self.__gender
    
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age= age
    
    def __repr__(self):
        return f'Passenger({self.__passname}, {self.__gender}, {self.__age})'
    
    def __str__(self):
        return f'Pasajero de nombre: {self.__passname}, de edad: {self.__age} y género: {self.__gender}'

class Flight:
    
    __adultsPrice= 1500
    __childsPrice= 750
    __olderPrice= 500
    
    def __init__(self, ownername, passengers, origin, destination):
        self.__ownername= ownername
        self.__passengers= passengers
        self.__origin= origin
        self.__destination= destination
        self.__date= Date()
        self.__interface= FlightInterface()
        self.__codes= []
    
    def turn_on_interface(self):
        self.__interface.activate_interface()
        return 'Puede realizar su registro de vuelo ahora'
    
    def turn_off_interface(self):
        self.__interface.desactivate_interface()
        return '¡Que tenga un gran día!'
    
    def is_active(self):
        return self.__interface.is_activate()
    
    def generate_code(self):
        letters= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        passLength= len(self.__passengers)
        while passLength !=0:
            code= ''
            for i in range(5):
                code+= letters[rn.randint(0,8)]+str(rn.randint(0,9))
            passLength-=1
            self.__codes.append(code)
        return self.__codes
    
    def assign_code(self):
        for i in range(len(self.__passengers)):
            if i == 0:
                print('El pasajero número 1 posee el código: ' + self.__codes[i])
            else:
                print('El pasajero número ' + str(i+1) + ' posee el código: ' +self.__codes[i])
    
    def calculate_price(self):
        total= 0
        for i in self.__passengers:
            if i.age < 20:
                 total+= Flight.__childsPrice
            elif 20 <= i.age < 60:
                total+= Flight.__adultsPrice
            else:
                total+= Flight.__olderPrice
        return f'El total de los boletos sería de: ${total}'
        
    def change_date(self, day, month, year):
        self.__date= Date(day, month, year)
        return self.__date.day, self.__date.month, self.__date.year
    
    def date_data(self):
        return self.__date.day, self.__date.month, self.__date.year
    
    def change_destination(self, newdestination):
        self.__destination= newdestination
        return f'Se cambió el destino a {self.__destination}'
            
    def __repr__(self):
        return f'Flight({self.__ownername}, {self.__passengers}, {self.__origin}, {self.__destination}, {repr(self.__date)}, {repr(self.__interface)}'
    
    def __str__(self):
        return f'Su vuelo de: {self.__origin} --- {self.__destination}, se ha registrado a nombre de: {self.__ownername}. {self.__date}'
    
    
if __name__ == '__main__':
    p1= Passenger('Nicolás Macías', 'M', 20)
    print(p1)
    p2= Passenger('Lancelot Micelas', 'M', 32)
    print(p2)
    p3= Passenger('Joshua Hernández', 'M', 17)
    print(p3)
    print(repr(p3))
    p4= Passenger('Michelle Serret', 'F', 83)
    print(repr(p4))
    v1= Flight('Lancelot Micelas', [p1, p2], 'Montevideo, Uruguay', 'Ciudad de México, México')
    print(v1.calculate_price())
    print(v1.generate_code())
    v1.assign_code()
    print(v1)
    v1.change_date(23, 4, 2020)
    print(v1)
    v2= Flight('Michelle Serret', [p1, p2, p4], 'Chicago, EUA', 'Madrid, España')
    print(v2.turn_on_interface())
    print(v2.generate_code())
    v2.assign_code()
    print(v2.calculate_price())
    print(repr(v2))
    print(v2.change_date(4, 10, 2020))
    print(v2.date_data())
    print(v2.change_destination('Nueva Delhi, India'))
    print(v2)
    print(v2.turn_off_interface())