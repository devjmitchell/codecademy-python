# File I/O - check if a file is closed and close it if not

with open("text.txt", "w") as my_file:
    my_file.write("This is my test of automagically closing the file using 'with' and 'as'!")

if my_file.closed == False:
    my_file.close()

print my_file.closed
