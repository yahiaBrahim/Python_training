'''
   The License:
   
   Asterix-dz is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
 
   Asterix-dz is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
 
   You should have received a copy of the GNU General Public License
   along with Asterix-dz.  If not, see <http://www.gnu.org/licenses/>.

   Q29kZWQgQnkgIk9TZHogRHpheWVyIgpXaXRoIHRoZSBoZWxwIE9mIFJhb3VmCkZhY2Vib29rOiBPU2RldmR6Cg==

'''

from __future__ import division
from aircodes import airline_code
import sys, getopt
import rdbt 
import Glob
import Func

# ------------------ MAIN ENTRY ---------------------------------------#

def main(argv):
   
    Hello = """ 

     .oo .oPYo. ooooo .oPYo.  .oPYo. o  o    o        ooo.   oooooo 
    .P 8 8        8   8.      8   `8 8  `b  d'        8  `8.     d' 
   .P  8 `Yooo.   8   `boo   o8YooP' 8   `bd'         8   `8    d'  
  oPooo8     `8   8   .P      8   `b 8   .PY.   ooooo 8    8   d'   
 .P    8      8   8   8       8    8 8  .P  Y.        8   .P  d'    
.P     8 `YooP'   8   `YooP'  8    8 8 .P    Y.       8ooo'  dooooo 
..:::::..:.....:::..:::.....::..:::......::::..:::::::.....::.......
:Q29kZWQgQnkgIk9TZHogRHpheWVyIgpXaXRoIHRoZSBoZWxwIE9mIFJhb3VmCkZhY2:
::::::::::::Vib29rOiBPU2RldmR6Cg==::::::::::::::::::::::::::::::::::
    """
    print(Hello)
    
    i = 1


    try:
        #print ("Hey" + sys.argv[1])
        with open(sys.argv[1], "rb") as rdbt.f:

            
            #index = 0
            while(1):
                Glob.cat = rdbt.readbyte()
                
                
                if (Glob.cat == 1 or Glob.cat == 48):
                    
                    print("\n------------------------------------------------")
                    print("------------------CAT: %d-----------------------"% Glob.cat)
                    print("------------------------------------------------")
                    
                        
                else:
                    
                    while ((Glob.cat != 1) and (Glob.cat != 48)):
                        print("\n\n##########################################")
                        print Glob .index
                        print("Don't Support Cat %d" % Glob.cat)
                        print("Block Data Skipped N= %d" % i)
                        
                        leng1 = rdbt.readbyte()
                        leng2 = rdbt.readbyte()
                    
                        leng = (leng1 << 8) | leng2
                        print ("+---CAT: %d" % Glob.cat) 
                        print ("len is %d " % leng)
                        print("##########################################\n\n")
                        # Just Skip This Category Block
                        leng = leng - 3 # 3 bytes of CAT and Length 
                        rdbt.f.seek(leng, 1)
                        
                        Glob.cat = rdbt.readbyte()

                        
                        Glob.index = Glob.index - 3
                        i = i + 1
                
                    print("------------------------------------------------")
                    print("------------------CAT: %d-----------------------"% Glob.cat)
                    print("------------------------------------------------")
        

                    
                    Glob.index = Glob.index + 1

                    
                
                length1 = rdbt.readbyte()
                length2 = rdbt.readbyte()
                
                
                BlockData_length = (length1 << 8) | length2
                
                Glob.total_len = Glob.total_len + BlockData_length

                print ("+--- Block Len : %d" % BlockData_length)

                

                while (Glob.index < Glob.total_len):
                    print Glob .index
                    
                    print("--------------(New Data Record)---------------")
                    
                    Func.READ_FSPEC()

                    #-------------------------------- Decode Categorie 48 ----------------------------- 
                    if(Glob.cat == 48):
                        Func.Decode_48()
                    # Decode CAT 001                                

                    elif (Glob.cat == 1):

                        #Glob.FSPEC1

                        Func.Decode_01()
    
    except EnvironmentError:
        print("<"+sys.argv[1]+">" + " file Does not exist")                             

if __name__ == "__main__":
   main(sys.argv[1:])                           
