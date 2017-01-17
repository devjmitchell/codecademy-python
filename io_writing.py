# File I/O - writing to a file

my_list = [i**2 for i in range(1,11)]

my_file = open("output.txt", "r+")	# r+ allow reading and writing (w is just writing)

# Add your code below!
for item in my_list:
    my_file.write(str(item) + "\n")

my_file.close()
