class funcionary:
    def __init__(self, name, payment):
        self.name = name
        self.payment = payment
        
    def  up_payment(self, perc_up):
        perc_up = self.payment * (perc_up/100)
        new_pay = self.payment + perc_up
        return new_pay

name_func = input("put the funcionary name please: ")
payment_func = float(input("put the funcionary salary: "))
new_payment = float(input("put the funcionary percentage salary increase plz: "))

funcionary_payload = funcionary(name=name_func, payment=payment_func)
salary_payload = funcionary_payload.up_payment(new_payment)

print(f" o nome do funcionário é { funcionary_payload.name} ") 
print(f" o salario antigo é { funcionary_payload.payment} ") 
print(f" o novo salario é { salary_payload} ") 