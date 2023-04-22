import Dog as animal 
from car import car  , tesla  
# import carton as box 
dog = animal.Dog('Willie' , 7)

car =  car('TOYOTA' , 2021 , 'C-130' )
tesla = tesla('TESLA' , 2022 , 'leaf')

# print(dog.name)
# print(dog.age)
# dog.run()
# dog.roll_over()
# car.describe_car()
# car.set_odometer(22)
# car.describe_car()

# carton = box.carton('001' , 'khandan Chips' , '100x100x100' , 14.22 , 12000 , 10001 ,'WTL FLUTE FLUTE FLUTE WTK')
# carton.create_quotation()
# carton.print_paper()
# carton.update_quantity(23_200)
# carton.increment_quantity(176)
# carton.create_quotation()

tesla.describe_car()
tesla.name = 'Benz'

tesla.describe_car()
tesla.describe_battery()
tesla.fill_gas_tank()

