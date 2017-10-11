import Glob
import sys

global f
def readbyte():
 
    one_byte = f.read(1)
    if (one_byte == ""):
        print("\n\n==========================(END)=======================")
        print("====================Thanks For Using Our App====================")
        sys.exit()
    
    number = ord(one_byte)
    Glob.index = Glob.index + 1
    return number
