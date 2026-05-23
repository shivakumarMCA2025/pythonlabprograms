
"""WAPP to read patient_name,  room_charges, medicine_cost, lab_test_cost and display hospital patient details along with the Total bill"""

patient_name=input("enter patient name: ")
room_charges=int(input("enter room charges: ")) 
medicine_cost=int(input("enter medicine cost: "))
lab_test_cost=int(input("enter lab test cost: "))
total_bill=room_charges+medicine_cost+lab_test_cost
print("Patient Name:", patient_name)
print("Total bill:", total_bill)
