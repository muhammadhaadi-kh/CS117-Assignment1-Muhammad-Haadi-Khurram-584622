def paralell_resistance(resistors):
    """Calculates total equivalent resistancce for resistors in paralell"""
    reciprocal_sum = sum(1/r for r in resistors)
    return 1/reciprocal_sum
print("paralell_resistance[10,10]",paralell_resistance([10,10]))
print("paralell_resistance([100,200,300])",paralell_resistance([100,200,300]))
