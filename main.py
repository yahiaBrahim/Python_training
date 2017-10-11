import sys, getopt
import rdbt
import Glob





def main(argv):

    try:
        #print ("Hey" + sys.argv[1])
        with open(sys.argv[1], "rb") as rdbt.f:
            cat = rdbt.readbyte()
            print cat
            print Glob.index

    except EnvironmentError:
        print("<"+sys.argv[1]+">" + " file Does not exist")                             

if __name__ == "__main__":
   main(sys.argv[1:])                                