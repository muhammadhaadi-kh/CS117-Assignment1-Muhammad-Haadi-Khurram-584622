num_resistors = int(input("How many resistors?"))
total_resistance=0
for i in range(1,num_resistors+1):
   resistor_value=float(input("Enter value of R:"))
   total_resistance+=resistor_value
   print("Total resistance=",(total_resistance))
