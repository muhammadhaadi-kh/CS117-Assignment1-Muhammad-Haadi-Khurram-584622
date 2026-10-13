
voltage_volts = float(input("Enter the value:"))#initializing values
resistance_ohms = float(input("Enter the value:"))
if resistance_ohms<=0:    # resistance cant be zero for current
    print("Not possible")
else:
    current_Amp=(voltage_volts/resistance_ohms)
    print("current is",current_Amp)
    if current_Amp>2:
            print("Fuse will blow")
    else:
              print("Fuse will not Blow")


