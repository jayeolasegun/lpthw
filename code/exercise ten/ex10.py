tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# Escape Sequences

#Escape       What it does
#\\           Backslash(\)
#\'           Single-quote(')
#\"           Double-quote(")
#\a           ASCII bell (BEL)
#\b           ASCII backspace (BS)
#\f           ASCII formfeed (FF)
#\n           ASCII linefeed (LF)
#\N{Name}     Character named name in the unicode database (Unicode only)
#\r           ASCII carriage return
#\t           ASCII horizontal tab
#\uxxxx       Character with 16-bit hex value xxxxx (Unicode only)
#\Uxxxx       Character with 32-bit hex value xxxxx (Unicode only)
#\v           ASCII vertical tab (VT)
#\ooooo       Character eith Octal value oo
#\xhh         Character with hex value hh    

# an infinite loop
#while True:
#    for i in ["/","-","|","\\","|"]:
#        print("%s\r" % i)      

