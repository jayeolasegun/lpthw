# close -- closes the file
# read -- read the contents of the file
# readline -- reads just one line of a text file
# truncate -- empties the file . WATCH OUT IF YOU CARE ABOUT THE FILE
# write  ---  writes stuff to the file


from sys import argv

script, file_name = argv

print("We are going to erase %r" % file_name)
print("If you dont want that HIT CTRL-C(^C)")
print("If you want that, HIT return")

input("?")

print("Opening the file......")
target =  open(file_name, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now i am going to ask you for three lines.")

print("I am going to write these to the file.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I am going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, We close it.")
target.close()