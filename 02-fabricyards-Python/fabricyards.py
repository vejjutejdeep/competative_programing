# fabricyards(inches)
# Fabric must be purchased in whole yards, so purchasing just 1 inch
# of fabric requires purchasing 1 entire yard. With this in mind,
# write the function fabricYards(inches) that takes the number of
# inches of fabric desired, and returns the smallest number of whole
# yards of fabric that must be purchased.

# fabricexcess(inches)
# Write the function fabricExcess(inches) that takes the number of
# inches of fabric desired and returns the number of inches of excess
# fabric that must be purchased (as purchases must be in whole yards)
# . Hint: you may want to use fabricYards, which you just wrote!
import math


def fun_fabricyards(inches):
    # your code goes here
    yards = inches / 36
    print(math.ceil(yards))
    return (math.ceil(yards))


def fun_fabricexcess(inches):
    # your code goes here
    yards = math.ceil(inches / 36)
    excess = (yards * 36) - inches
    print(excess)
    return(excess)


fun_fabricyards(0)
fun_fabricexcess(37)
