class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        
    def getStatus(self):
        print("*********************************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are: {self.seats}")
        print("*********************************")
   
    def getFare(self):
        print(f"The price of the ticket is: Rs.{self.fare}")
        print("*********************************")
   
    def bookTicket(self):
        if (self.seats>0):
            print(f"Your seat has been booked, your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry, we have no more seats!")
        
    def cancelTicket(self):
        self.seats = self.seats + 1
        print(f"Your ticket has been cancelled!")
        
        
intercity = Train("Karchi Express", 90, 100)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
#intercity.bookTicket()
intercity.cancelTicket()
intercity.getStatus()
intercity.getFare()
