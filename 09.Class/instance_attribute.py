
class car: 
    def __init__ (self , name , year , model): 
        self.name = name 
        self.year = year 
        self.model = model 
        self.odometer = 0  
    
    def describe_car(self): 
        print(f"The Veichle  {self.name} manufactured in {self.year} and the model is {self.model} / {self.odometer} KM ")

    def set_odometer(self , odometer ): 
        self.odometer = odometer

    def increment_odometer(self, miles):
            """Add the given amount to the odometer reading."""
            self.odometer += miles
    def fill_gas_tank(self):
        """Fills Gas into Car """
        print("Gas Tank is Filling")

class Electric_Car(car):
    def __init__(self , name, year, model ): 
        super().__init__(name , year, model)
        self.battery_size = Battery() 

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """The override method """
        print("Electric car does not require GAS ")
            

""" THIS CLASS IS SHOW US HOW WE CAN PUT INSTANCE OF A CLASS IN ANOTHER CLASS WITHOUT ANY INHERETANCE  """

class Battery : 
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        


elec_car  = Electric_Car('tesla' , 2023 , 'SDV-100')
elec_car.describe_car()
elec_car.fill_gas_tank()
elec_car.increment_odometer(100)
elec_car.describe_car()

elec_car.battery_size.describe_battery()
