voltages = [12.6,12.5,12.5,12.3,12.1,11.9,12.0,11.8,11.6,11.5,11.2]
max_length = 1
max_start_v = voltages[0]
max_end_v = voltages[0]
current_length=1
current_start_v = voltages[0]
for i in range(1,len(voltages)):
    if voltages[i]<voltages[i-1]:
        current_length +=1
    else:
        if current_length >max_length:
            max_length = current_length
            max_start_v = current_start_v
            max_end_v = voltages[i-1]
        current_length =1
        current_start_v = voltages[i]
if current_length > max_length:
     max_length = current_length
     max_start_v = current_start_v
     max_v = voltages[-1]
print("Longest continuous drop:",max_length,"minutes")
print("Started at:",max_start_v,"V")
print("Ended at",max_end_v,"V")
