# file = open("order.txt", "w")
# try:
#     file.write("Masala Chai - 2 cups")
# finally:
#     file.close()

with open("order.txt", "w") as file: # if autmatically provides the try-except block
    file.write("ginger tea - 4 cups")