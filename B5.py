def ohms_current(v,r):
    """Calculate current using Ohm's Law:I=V/R"""
    return v/r
def power_dissipated(i,r):
    """Calculate power dissipated P=(I^2)*R"""
    return(i**2)*r
v_test =12
r_test = 6
current_result = ohms_current(v_test,r_test)
power_result= power_dissipated(current_result,r_test)
print("Current = ",current_result,"A")
print("Power=",power_result,"W")
