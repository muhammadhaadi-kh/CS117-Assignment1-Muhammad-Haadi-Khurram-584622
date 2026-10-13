def loaded_divider(vs,r1,r2,rl):
    """
    Calculates the unloaded and loaded output volate of a voltage divider network.
    Retuns:(unloaded_voltage,loaded_voltage)
    """
    unloaded_voltage = vs*(r2/(r1 +r2))
    r2_paralell_rl = 1/((1/r2)+(1/rl))
    loaded_voltage = vs*(r2_paralell_rl/(r1+r2_paralell_rl))
    return round(unloaded_voltage,1),round(loaded_voltage,1)
print("loaded_divider(12,1000,1000,500)",loaded_divider(12,1000,1000,500))
    
