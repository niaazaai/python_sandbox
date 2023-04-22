
class carton: 
    def __init__ (self , id , product_name , size , price , order_quantity , job_no , used_paper ):
        self.id = id 
        self.product_name = product_name 
        self.size = size 
        self.price = price 
        self.order_quantity = order_quantity 
        self.job_no = job_no 
        self.used_paper = used_paper 

    def create_quotation(self): 
        print(f"ID {self.id} | Job No {self.job_no} | {self.product_name} | {self.order_quantity} QTY | {self.size} CM  | {self.price} USD  =>> {round(self.price * self.order_quantity , 2 ) } Total Price")

    def print_paper(self): 
        print(f"USED PAPER IN JOB NO : {self.job_no}  IS ::==> {self.used_paper}")

    def update_quantity(self , qty):
        self.order_quantity = qty 
        print(f"Quantity Updated to {self.order_quantity}")
    
    def increment_quantity(self , qty):
        self.order_quantity += qty 
        print(f"Quantity Incremented to {self.order_quantity}")

    

