
class Patient:
    def __init__(self, name, bill_amount):
        # the getter and setter methods used to access and modify the private attributes of the class
        self.__name = name
        self.set_bill_amount(bill_amount)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        try:
            bill_amount = float(bill_amount)
        except (ValueError, TypeError):
            raise ValueError("Bill amount must be a valid number.")

        if bill_amount < 0:
            raise ValueError("Bill amount cannot be negative.")

        self.__bill_amount = bill_amount

    def calculate_bill(self):
        # base bill calculation for regular patients (no discount) 
        return self.get_bill_amount()

    def calculate_savings(self): # method that calculates the savings for the patient. - (bonus feature)
        return self.get_bill_amount() - self.calculate_bill()

class SeniorPatient(Patient):

    def calculate_bill(self):
        # 20% discount for senior citizens
        base_bill = super().calculate_bill()
        return base_bill * 0.80

class PhilHealthPatient(Patient):

    def calculate_bill(self):
        # applying 15% discount for PhilHealth members
        base_bill = super().calculate_bill()
        return base_bill * 0.85

# sample patients
regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)

patients = [regular_patient, senior_patient, philhealth_patient]

# printing the billing information for each patient
print("Hospital Billing System")
print("-----------------------")

total_savings = 0

for i in patients:
    orig = i.get_bill_amount()
    final = i.calculate_bill()
    savings = i.calculate_savings()
    total_savings += savings

    print(f"Patient Name:  {i.get_name()}")
    print(f"Original Bill: ₱{orig:,.2f}")
    print(f"Final Bill: ₱{final:,.2f}")
    print(f"Discount Saved: ₱{savings:,.2f}\n")

print("-----------------------")
print(f"Total Hospital Discounts: ₱{total_savings:,.2f}")
