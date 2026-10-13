bit1=(input("Enter your number:"))
bit2=(input("Enter your number:"))
if bit1 not in["0","1"] or bit2 not in["0","1"]:
    print("Bits must be 0 or 1")
else:
    bit1=int(input("Enter your number:"))
    bit2=int(input("Enter your number:"))
    and_1=bit1&bit2
    or_1=bit1|bit2
    xor=bit1^bit2
    print("AND=",and_1)
    print("OR=",or_1)
    print("XOR=",xor)
