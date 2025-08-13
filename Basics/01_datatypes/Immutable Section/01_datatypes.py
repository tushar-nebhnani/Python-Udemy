"""
    Mutable: this thing can be changed
    Immutable: this thing cannot be changed
    ->* identity helps to figure out it is changeable or not, only check it with identiy. With value you should never check mutability or immutability. If the identity is same it is mutable but if the identity changes it is not mutable.
    -> What values i can change and what values i cannot change in the memory.

    Immutable: Numbers(but we can change the reference of it),
    Mutable: Sets, 

    Types Of Datatypes:
        1. Objects:-  Everything is object in python. 
            Properties: * Every single obj has a unique identity
                        * It's own unique type
                        * Have a value assign to it, it can have an empty value also

        2. Numbers:- 
            Types:-     1. Integers 
                        2. Boolean -> logical operations: AND, OR, NOT
                        3. Real Number(floating point numbers)
                        4. Complex Numbers(2+3j, j is the iota of python)

                    sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)   
            
"""
# checking mutability for numbers

# you never check mutability using value as it will just reassign the reference of the value, we are just changing the reference but the actual value.
sugar_amount = 2
print(f"Intial Number of spoons: {sugar_amount}")

sugar_amount = 12
print(f"Number of spoons: {sugar_amount}")

# checking through the identity of the number(value assigned to it)
print(f"Identity of intial variable 2: {id(2)}")
print(f"Identity of variable 12: {id(12)}")

# checking mutability for sets
# This is the mutable part
spice_mix = set()
print(f"Intial spice mix id: {id(spice_mix)}")
print(spice_mix)

spice_mix.add("Ginger")
spice_mix.add("Cardamon")

print(spice_mix)
spice_mix.add("Salt")
print(f"After spice mix id: {id(spice_mix)}")
print(spice_mix)

# Numbers start here
black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of tea is: {total_grams}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Total grams of remainig tea is: {remaining_tea}")

# "/" -> you care what comes after decimals
milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is: {milk_per_serving}")

# "//" -> you don't care what comes after decimals
total_tea_bags = 7
pots = 4
bag_per_pots = total_tea_bags // pots
print(f"Bags per pot: {bag_per_pots}")

# "%" -> you care about how much is left
total_cadmon_pods = 10
pods_per_cup = 3
leftover_pods = total_cadmon_pods % pods_per_cup
print(f"Lectover cadmon pod: {leftover_pods}")

base_flavour_stength = 2
scale_factor = 3
powerful_flavour = base_flavour_stength ** scale_factor
print(f"The power of our flavour is: {powerful_flavour}")

# improving the readability 
total_tea_leaves_harvested = 1_000_000_000
print(f"tea leaves: {total_tea_leaves_harvested}")

# boolean starts here, True = 1, False = 0
is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling # upcasting of the number
print(f"Upcasting of number: {total_actions}")

milk_present = 0 # no milk
print(f"is there milk? {bool(milk_present)}")

water_hot = True
tea_added = False

can_serve = water_hot and tea_added
print(f"Can serve char? {can_serve}")

import sys
# real number simply means precision in our program
ideal_temp = 95.5
real_temp = 95.49
print(f"ideal temp: {ideal_temp}")
print(f"Real temp: {real_temp}")
print(f"difference in precision: {ideal_temp - real_temp}")
print(sys.float_info) # gives the precision of the float number

# swapping without using temp
a, b = 4, 5
a, b = b , a
print(f"{a}, {b}")