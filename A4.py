x=float(input("Enter your resistor:"))
y=float(input("Enter your resistor:"))
z=float(input("Enter your resistor:"))
if x<=y and x<=z:
    print("x resistor is smallest")
elif y<=x and y<=z:
   print("y is smallest")
else:
    print("z is smallest")
if x>=y and x>=z:
  print("x is largest")
elif y>=x and y>=z:
  print("y is largest")
else:
    print("z is largest")
  
    
