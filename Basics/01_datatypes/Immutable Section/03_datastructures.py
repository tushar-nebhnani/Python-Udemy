"""
    Tuples: ()
        We can't change them. IMMUTABLE.
        once it is defined we can't change it throughout the life of the program.
"""

masala_spices = ("cardamon", "cloves", "cinnamon")
# unpacking assigning name to the values
(spice1, spice2, spice3) = masala_spices 

print(f"Main masala spices: {masala_spices}")
print(f"Main masala spices: {spice1}, {spice2}, {spice3}") # unpack style

ginger_ratio, cardamon_ratio = 2, 1

print(f"Ratio for ginger is: {ginger_ratio} and cadmon: {cardamon_ratio}")
ginger_ratio, cardamon_ratio = cardamon_ratio, ginger_ratio
print(f"Ratio after swapping for ginger is: {ginger_ratio} and cadmon: {cardamon_ratio}")

# membership: in and not in

print(f"Is cloves present in masala spices? {"cloves" not in masala_spices}")
