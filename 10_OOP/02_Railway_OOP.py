import pandas as pd
pd.DataFrame()


class RailwayForm:
    def printData(self):
        print("Name is " , self.name)
        print("Train is " , self.train)
       
    
myApplication = RailwayForm()
myApplication.name= "Nemo"
myApplication.train = "Express"
myApplication.printData()