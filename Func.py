import Glob
import rdbt
from aircodes import *
import sys

def READ_FSPEC():
    Glob.FSPEC1= rdbt.readbyte()
    print("Glob.FSPEC1 : %s" % bin(Glob.FSPEC1) )
    fspec_len = 1
    if (Glob.FSPEC1 & 1):
        Glob.FSPEC2 = rdbt.readbyte()    
        print("Glob.FSPEC2 : %s" % bin(Glob.FSPEC2) )
        fspec_len = fspec_len + 1
        if (Glob.FSPEC2 & 1):
            Glob.FSPEC3 = rdbt.readbyte()
            print("Glob.FSPEC3 : %s" % bin(Glob.FSPEC3) )
            fspec_len = fspec_len + 1
            if (Glob.FSPEC3 & 1):
                Glob.FSPEC4 = rdbt.readbyte()
                print("Glob.FSPEC4 : %s" % bin(Glob.FSPEC4) )
                fspec_len = fspec_len + 1
            else:
                print(" |____No Other FSPEC Extension") 
        else:
            print(" |____No Other FSPEC Extension")     
    else:
        print(" |____No Other FSPEC Extension")         
    print("------------------------")           
    print("FSPEC Item Has %d bytes" % fspec_len)
    print("------------------------")

def SIX_BITS_CHAR(code):
    ind        = (code & 0x30) >> 4
    letter_num = (code & 0xF)

    if(letter_num == 0):
        if(ind == 0):
            return " "
        elif(ind == 1):
            return 'P'
        elif(ind == 2):
            return " "
        elif(ind == 3):
            return '0'      
    elif(letter_num == 1):
        if(ind == 0):
            return 'A'
        elif(ind == 1):
            return  'Q'
        elif(ind == 2):
            return " "
        elif(ind == 3):
            return '1'
    elif(letter_num == 2):
        if(ind == 0):
            return 'B'
        elif(ind == 1):
            return 'R'  
        elif(ind == 2):
            return " "
        elif(ind == 3):
            return '2'
    elif(letter_num == 3):
        if(ind == 0):
            return 'C'
        elif(ind == 1):
            return  'S'
        elif(ind == 2):
            return " "
        elif(ind == 3):
            return '3'
    elif(letter_num == 4):
        if(ind == 0):
            return 'D'
        elif(ind == 1):
            return  'T'
        elif(ind == 2):
            return " "
        elif(ind == 3):
            return '4'
    elif(letter_num == 5):
        if(ind == 0):
            return 'E'
        elif(ind == 1):
            return  'U'
        elif(ind == 2):
            return " "
        elif(ind == 3):
            return '5'
    elif(letter_num == 6):
        if(ind == 0):
            return 'F'
        elif(ind == 1):
            return 'V'  
        elif(ind == 2):
            return " "
        elif(ind == 3):
            return '6'
    elif(letter_num == 7):
        if(ind == 0):
            return 'G'
        elif(ind == 1):
            return  'W'
        elif(ind == 2):
            return " "
        elif(ind == 3):
            return '7'
    elif(letter_num == 8):
        if(ind == 0):
            return 'H'
        elif(ind == 1):
            return  'X'
        elif(ind == 2):
            return " "
        elif(ind == 3):
            return '8'
    elif(letter_num == 9):
        if(ind == 0):
            return 'I'
        elif(ind == 1):
            return  'Y'
        elif(ind == 2):
            return " "
        elif(ind == 3):
            return '9'
    elif(letter_num == 10):
        if(ind == 0):
            return 'J'
        elif(ind == 1):
            return  'Z'
        elif(ind == 2):
            return " "
        elif(ind == 3):
            return '10'
    elif(letter_num == 11):
        if(ind == 0):
            return 'K'
        elif(ind == 1):
            return  " "
        elif(ind == 2):
            return " "
        elif(ind == 3):
            return " "
    elif(letter_num == 12):
        if(ind == 0):
            return 'L'
        elif(ind == 1):
            return  " "
        elif(ind == 2):
            return " "
        elif(ind == 3):
            return " "
    elif(letter_num == 13):
        if(ind == 0):
            return 'M'
        elif(ind == 1):
            return " "
        elif(ind == 2):
            return " "
        elif(ind == 3):
            return " "
    elif(letter_num == 14):
        if(ind == 0):
            return 'N'
        elif(ind == 1):
            return " "   
        elif(ind == 2):
            return " "
        elif(ind == 3):
            return " "
    elif(letter_num == 15):
        if(ind == 0):
            return 'O'
        elif(ind == 1):
            return " "
        elif(ind == 2):
            return " "
        elif(ind == 3):
            return " "


def MODE3_A_REPLAY_OCTAL(cat):
    MODE3_A1 = rdbt.readbyte()
    MODE3_A2 = rdbt.readbyte()
    MODE3_A_REPLAY = ((MODE3_A1 << 8) | MODE3_A2) & 4095  # 4095 = 0b0000 1111 1111 1111

    MODE3_A_V = (MODE3_A1 & 128)
    MODE3_A_G = (MODE3_A1 & 64)
    MODE3_A_L = (MODE3_A1 & 32)

    if(cat == 1):
        print("+---I001/070 [Mode-3A Code in Octal Representation]")
    elif(cat == 48):
        print("+---I048/070 [Mode-3A Code in Octal Representation]")

    if(MODE3_A_V):
        print(" |____V : 1 :Code Not Validate")
    else:
        print(" |____V : 0 :Code Validate")
    if(MODE3_A_G):
        print(" |____G : 1 :Code Garbled")
    else:
        print(" |____G : 0 :Code Not Garbled")
    if(MODE3_A_L):
        if (cat == 1):
            print(" |____L : 1 :Smoothed Mode3_A Code Provided By Local Tracker")
        elif(cat == 48):
            print(" |____L : 1 :Mode3_A Code Not Extracted during the last scan")
    else:
        print(" |____L : 0 :Mode3_A Code As Derived From the Reply Of Transponder")

    print(" |____bit13: 0 : [Spare Bit Always Set to 0]")
        
    print(" |____Mode3_A reply In Octal : %o" % MODE3_A_REPLAY)
    print("     |____ Decimal : %d" % MODE3_A_REPLAY)

def MODE_C_BINARY():
    MOD_C_CODE1 = rdbt.readbyte()
    MOD_C_CODE2 = rdbt.readbyte()
    print MOD_C_CODE1
    print MOD_C_CODE2

    MOD_C_CODE  = ( MOD_C_CODE1 << 8) | MOD_C_CODE2
    MOD_C_CODE_HEIGHT = (MOD_C_CODE & 16383)
    MOD_C_CODE_V = (MOD_C_CODE1 & 128)
    MOD_C_CODE_G = (MOD_C_CODE1 & 64)
    print("+---I001/090 : [Mode C Code In Binary Representation]")
    if (MOD_C_CODE_V):
        print(" |____MODE_C_CODE_V : 1 : [Code Not Validated]")
    else:
        print(" |____MODE_C_CODE_V : 0 : [Code Validated]")
    if (MOD_C_CODE_G):
        print(" |____MODE_C_CODE_G : 1 : [Garbled Code]")
    else:
        print(" |____MODE_C_CODE_G : 0 : [Default (No Garbled)]")

    if (MOD_C_CODE_HEIGHT):
        print(" |____MODE_C_CODE_HEIGHT : %.2f FL (%d feets)" % ((MOD_C_CODE_HEIGHT * 1/4), MOD_C_CODE_HEIGHT * 25))
            # bit-1 (LSB) = 1/4 FL = 25 feet. (Radar Data Exchange Part-2a Document)

def TRUNCATED_TIME():
    TRUNCATED_TIME1 = rdbt.readbyte()
    TRUNCATED_TIME2 = rdbt.readbyte()
    TRUNCATED_TIME  = (TRUNCATED_TIME1 << 8) | TRUNCATED_TIME2  
    print("+---I001/141 [Truncated Time Of Day]: %.2f sec" % (TRUNCATED_TIME * 1/128))

def RADAR_PLOT_CHARAC(cat):
    if (cat == 1):

        RADAR_PLOT_CARAC = rdbt.readbyte()
        DATA = RADAR_PLOT_CARAC >> 1
        print("+---I001/130 : [Radar Plot Charac] : %d" % DATA)
        if(RADAR_PLOT_CARAC & 1):
            RADAR_PLOT_CARAC_EXT = rdbt.readbyte()
            print(" |____Extension Byte %d ]" % RADAR_PLOT_CARAC_EXT)
        else:
            print(" |____No Extension Byte")    
    elif(cat == 48):
        RADAR_PLOT_CARAC = rdbt.readbyte()
        print("+---I048/130 : [Radar Plot Charac] : %d" % RADAR_PLOT_CARAC) 
        SRL = (RADAR_PLOT_CARAC & 128)
        SRR = (RADAR_PLOT_CARAC & 64)
        SAM = (RADAR_PLOT_CARAC & 32)
        PRL = (RADAR_PLOT_CARAC & 16)
        PAM = (RADAR_PLOT_CARAC & 8)
        RPD = (RADAR_PLOT_CARAC & 4)
        APD = (RADAR_PLOT_CARAC & 2)
        FX  = (RADAR_PLOT_CARAC & 1)

        if(SRL):
            Subfield_1 = rdbt.readbyte()
            print(" |____SSR Plot Runlength : %.2f deg" % (Subfield_1 * 0.044))
        if(SRR):
            Subfield_2 = rdbt.readbyte()
            print(" |____Number Of Recieved Replies for M(SSR): %d " % Subfield_2)
        if(SAM):
            Subfield_3 = rdbt.readbyte()
            print(" |____Amplitude of M(SSR): %d dBm" % Subfield_3)
        if(PRL):
            Subfield_4 = rdbt.readbyte()
            print(" |____Primary Plot Runlength: %.2f deg" % (Subfield_4 * 0.044))
        if(PAM):
            Subfield_5 = rdbt.readbyte()
            print(" |____Amplitude of Primary Plot: %d dBm" % Subfield_5)
        if(RPD):
            Subfield_6 = rdbt.readbyte()
            if(Subfield_6 & 128):
                print(" |____Diffrence in Range between PSR & SSR plot: -%d" % (Subfield_6 & 0x7F))                         
            else:
                print(" |____Diffrence in Range between PSR & SSR plot: %d" % Subfield_6)                           
        if(APD):
            Subfield_7 = rdbt.readbyte()
            print(" |____Diffrence in Azimuth between PSR & SSR plot: %.2f deg" % (Subfield_7 * 0.044))
        if(FX):
            print(" |____ Extension Exists")
            Radar_Ext = rdbt.readbyte()
            print("     |____ %s" % bin(Radar_Ext))

            

def POLAR_CORD(cat):
    MSPOLAR_CORD1 = rdbt.readbyte()
    MSPOLAR_CORD2 = rdbt.readbyte()
    MSPOLAR_CORD3 = rdbt.readbyte()
    MSPOLAR_CORD4 = rdbt.readbyte()

    
    RHO_MSPOLAR_CORD  = (MSPOLAR_CORD1 << 8) | MSPOLAR_CORD2
    THETA_MSPOLAR_CORD  = (MSPOLAR_CORD3 << 8) | MSPOLAR_CORD4
    
    if(cat == 1):
        print("+---I001/040 [POSITION IN POLAR CORDINATES]:")
    elif(cat == 48):
        print("+---I048/040 [POSITION IN POLAR CORDINATES]:")

    print(" |____ RHO_MSPOLAR_CORD  : %d " % (RHO_MSPOLAR_CORD ))
    if(cat == 1):
        print(" |       |____%.4f NM" % (RHO_MSPOLAR_CORD * 1/128))
    elif(cat == 48):
        print(" |       |____%.4f NM" % (RHO_MSPOLAR_CORD * 1/256))
    print(" |____ THETA_MSPOLAR_CORD: %d " % (THETA_MSPOLAR_CORD))
    print("         |____%.4f deg" % (THETA_MSPOLAR_CORD * 0.0055))


def CARTESIAN_CORD(cat):

    CARTESIAN_CORD1 = rdbt.readbyte()
    CARTESIAN_CORD2 = rdbt.readbyte()
    CARTESIAN_CORD3 = rdbt.readbyte()
    CARTESIAN_CORD4 = rdbt.readbyte()

    X_CORD  = (CARTESIAN_CORD1 << 8) | CARTESIAN_CORD2
    Y_CORD  = (CARTESIAN_CORD3 << 8) | CARTESIAN_CORD4
    
    if(cat == 1):
        print("+---I001/042: [CARTESIAN CORD]")
    elif(cat == 48):
        print("+---I048/042: [CARTESIAN CORD]")
    print("X_CORD %s :" % bin(X_CORD))
    print("Y_CORD %s :" % bin(Y_CORD))
    
    if(CARTESIAN_CORD1 & 128):
        if(cat == 1):
            print(" |____ CARTESIAN_X_CORD : -%.2f NM" % ((X_CORD & 32767)) * 1/64)
            #just do not take the last bit in considiration bcz it is a Sign bit not included in the number.
        elif(cat == 48):
            print(" |____ CARTESIAN_X_CORD : -%.2f NM" % ((X_CORD & 32767)) * 1/128)

    else:
        if(cat == 1):
            print(" |____ CARTESIAN_X_CORD : -%.2f NM" % (X_CORD  * 1/64))
            #just do not take the last bit in considiration bcz it is a Sign bit not included in the number.
        elif(cat == 48):
            print(" |____ CARTESIAN_X_CORD : -%.2f NM" % (X_CORD  * 1/128))

    if(CARTESIAN_CORD3 & 128):
        if(cat == 1):
            print(" |____ CARTESIAN_Y_CORD : -%.2f NM" % ((Y_CORD & 32767)) * 1/64)
            #just do not take the last bit in considiration bcz it is a Sign bit not included in the number.
        elif(cat == 48):
            print(" |____ CARTESIAN_Y_CORD : -%.2f NM" % ((Y_CORD & 32767)) * 1/128)

    else:
        if(cat == 1):
            print(" |____ CARTESIAN_Y_CORD : -%.2f NM" % (Y_CORD  * 1/64))
            #just do not take the last bit in considiration bcz it is a Sign bit not included in the number.
        elif(cat == 48):
            print(" |____ CARTESIAN_Y_CORD : -%.2f NM" % (Y_CORD  * 1/128))




def TRACK_VELOCITY(cat):
    TRACK_VELOCITY1 = rdbt.readbyte()
    TRACK_VELOCITY2 = rdbt.readbyte()
    TRACK_VELOCITY3 = rdbt.readbyte()
    TRACK_VELOCITY4 = rdbt.readbyte()

    GROUND_SPEED        = (TRACK_VELOCITY1 << 8) | TRACK_VELOCITY2
    CALCULATED_HEADING  = (TRACK_VELOCITY3 << 8) | TRACK_VELOCITY4

    if(cat == 1):
        print("+---I001/200 : [TRACK VELOCITY IN POLAR CORD]:")
    elif(cat == 48):
        print("+---I048/200 : [TRACK VELOCITY IN POLAR CORD]:")

    print(" |____ GROUND_SPEED : %d : [Ground Speed]" % (GROUND_SPEED ))
    print(" |       |____%.2f kt" % (GROUND_SPEED * 0.22 ))
    print(" |____ HEADING      : %d : [Heading]" % (CALCULATED_HEADING ))
    print("         |____%.2f deg" % (CALCULATED_HEADING * 0.005 ))

def RECEIVED_POWER():
    RECEIVED_POWER = rdbt.readbyte()
    print("+---I001/131 [RECIEVED_POWER]: %d dBm" % RECIEVED_POWER)

def RADIAL_DOPPLER_SPEED(cat):
    if(cat == 1):
        RADIAL_DOPPLER_SPEED = rdbt.readbyte()
        print("+---I001/120 [RADIAL DOPPLER SPEED]: %d " % RADIAL_DOPPLER_SPEED)        
    elif(cat == 48):
        print("+---I048/120 [RADIAL DOPPLER SPEED]")
        PRIMARY = rdbt.readbyte()
        if(PRIMARY & 128):
            print(" |____ CAL: 1 : Calculated Doppler Speed Exists")
            CAL1 = rdbt.readbyte()
            CAL2 = rdbt.readbyte()

            CAL  = (CAL1<<8) | CAL2
            if(CAL1 & 128):
                print(" |   |____D:1:Doppler Speed Doubtful ")
            else:
                print(" |   |____D:0:Doppler Speed Valid ")
            print(" |   |____bits15-11: Spare bits set to 0 ")
                
            CAL_SPEED = (CAL & 0x1FF)
            if(CAL & 0x200):
                print(" |   |____Doppler Speed : -%d m/sec" % CAL_SPEED)
            else:
                print(" |   |____Doppler Speed :  %d m/sec" % CAL_SPEED)



        if(PRIMARY & 64):
            print(" |____ RDS: 1 : Raw Doppler Speed Exists")
            REP = rdbt.readbyte()
            while(REP):
                print(" |   |   (Data%d)" % REP)
                DOP1=rdbt.readbyte()
                DOP2=rdbt.readbyte()
                DOP = (DOP1<<8) | DOP2
                print(" |   |____Doppler Speed: %d m/sec" % DOP)
                AMB1=rdbt.readbyte()
                AMB2=rdbt.readbyte()
                AMB = (AMB1<<8) | AMB2
                print(" |   |____Ambiguity Range: %d m/sec" % AMB)
                FRQ1= rdbt.readbyte()
                FRQ2= rdbt.readbyte()
                FRQ = (FRQ1<<8) | FRQ2
                print(" |   |____Transmitter Frequency: %d Mhz" % FRQ)

                REP = REP - 1
        print(" |____ 1-6bits: 0 : Spare bits")
        






def TRACK_STATUS(cat):
    TRACK_STATUS =  rdbt.readbyte()
    if(cat == 1):
        print("+---I001/170 [TRACK STATUS] :")

        if(TRACK_STATUS & 128):
            print(" |____ CON : 1 : Track in initialisation phase")
        else:       
            print(" |____ CON : 0 : Track Confirmed")       
        if(TRACK_STATUS & 64):
            print(" |____ RAD : 1 : SSR Combined Track")
        else:
            print(" |____ RAD : 0 : Primary Track")
        if(TRACK_STATUS & 32):
            print(" |____ MAN : 1 : Aircraft Manoeuvring")
        else:
            print(" |____ MAN : 0 : Deafault")
        if(TRACK_STATUS & 16):
            print(" |____ DOU : 1 : Doubtful plot to Track Association")
        else:
            print(" |____ DOU : 0 : Default")
        if(TRACK_STATUS & 8):
            print(" |____ RDPC: 1 : RDP (Radar Data Processing) chain 2")
        else:
            print(" |____ RDPC: 0 : RDP (Radar Data Processing) chain 1")
        print(" |____ bit-3 : Spare bit set to 0")  
        if(TRACK_STATUS & 2):
            print(" |____ GHO: 1 : Ghost Track")
        else:
            print(" |____ GHO: 0 : Default")

        if(TRACK_STATUS & 1):
            print(" |____ Extension Data Found:")
            TRACK_STATUS2 = rdbt.readbyte()
            if(TRACK_STATUS2 & 128):
                print("   |____ (Extension) TRE: 1 : Last Report for a Track")
            else:
                print("   |____ (Extension) TRE: 0 : Default")
            print("   |____ (Extension) bits 0-7 : Spare Bits set To 0")
            if(TRACK_STATUS2 & 1):
                TRACK_STATUS3 = rdbt.readbyte()
                print("     |____ There a Second Extension: %d " % TRACK_STATUS3)
            else:
                print("     |____ Second Extension Does Not Exist")
        else:
            print(" |____ FX : 0 : Extension Not Exist")

    
    elif(cat == 48):
        print("+---I048/170 [TRACK STATUS] :")              
        if(TRACK_STATUS & 128):
            print(" |____ CNF : 1 : Tentative Track")
        else:       
            print(" |____ CNF : 0 : Confirmed Track")

        RAD = (TRACK_STATUS & 96)   
        if(RAD == 96):
            print(" |____ RAD : 11 : Invalid Track")
        elif(RAD == 64):
            print(" |____ RAD : 10 : SSR/Mode S Track")
        elif(RAD == 32):
            print(" |____ RAD : 01 : PSR Track")    
        elif(RAD == 0):
            print(" |____ RAD : 00 : Combined Track")
                
        if(TRACK_STATUS & 16):
            print(" |____ DUO : 1 : Low Confidence in plot to track Confidence")
        else:
            print(" |____ DUO : 0 : Normal Confidence")

        if(TRACK_STATUS & 8):
            print(" |____ MAH : 1 : Horizontal Manoeuvre Sensed")
        else:
            print(" |____ MAH : 0 : No Horizontal Manoeuvre Sensed")


        CDM = (TRACK_STATUS & 6)    
        if(CDM == 0):
            print(" |____ CDM: 00 : Maintaining Mode")
        elif(CDM == 2):
            print(" |____ CDM: 01 : Climbing Mode")
        elif(CDM == 4):
            print(" |____ CDM: 10 : Descending Mode")   
        elif(CDM == 6):
            print(" |____ CDM: 11 : Invalid Mode")

        if(TRACK_STATUS & 1):
            print(" |____ Extension Data Found:")
            TRACK_STATUS2 = rdbt.readbyte()
            if(TRACK_STATUS2 & 128):
                print("   |____ (Extension) TRE: 1 : End Of Track Lifetime")
            else:
                print("   |____ (Extension) TRE: 0 : Track Still Alive")

            if(TRACK_STATUS2 & 64):
                print("   |____ (Extension) GHO: 1 : Ghost Target Track")
            else:
                print("   |____ (Extension) GHO: 0 : True (Not Ghost) Target Track")

            if(TRACK_STATUS2 & 32):
                print("   |____ (Extension) SUP: 1 : Track Maintained With Track infos from Neighbouring Node B On The cluster")
            else:
                print("   |____ (Extension) SUP: 0 : No Infos Maintained With Track from Neighbouring Node B ")     

            if(TRACK_STATUS2 & 16):
                print("   |____ (Extension) TCC: 1 : Slant Range Correction + Suitable Projection Techniques Used To track in 2D")  
            else:
                print("   |____ (Extension) TCC: 0 : Tracking Performed in Radar Plane (No Slant Range Correction + No StereoGeographical Projection)")                     
            
            print("   |____ (Extension) bits4,3,2 set to 0")

            if(TRACK_STATUS2 & 1):  
                TRACK_STATUS3 = rdbt.readbyte()
                print("     |____ There a Second Extension: [%s] " % bin(TRACK_STATUS3))
            else:
                print(" |____ FX : 0 : Second Extension Not Exist")





def TRACK_QUALITY(cat):
    if (cat == 1):
        #global index
        TRACKQ     = rdbt.readbyte()
        #print TRACK_QUALITY
        TRACK_QUALITY_IND = TRACKQ >> 1

        print("+---I001/210 [TRACK QUALITY INDICATOR] : %d" % TRACK_QUALITY_IND)
        if (TRACKQ & 1):
            TRACK_QUALITY_EXTENSION = rdbt.readbyte()
            print(" |____ Extension Byte: %d" % TRACK_QUALITY_EXTENSION)
        else:
            print(" |____ FX : 0 : Extension Not Exist")    
        

        #print ("index is : %d" % index)
    elif(cat == 48):

         SIGMA_X = rdbt.readbyte()
         SIGMA_Y = rdbt.readbyte()
         SIGMA_V = rdbt.readbyte()
         SIGMA_H = rdbt.readbyte()
         print("+---I048/210 [TRACK QUALITY]")
         print(" |____ Sigma X (Standard Deviation On Horizontal axis): %.2f NM"  % (SIGMA_X * 1/128))  
         print(" |____ Sigma Y (Standard Deviation On Vertical axis)  : %.2f NM"  % (SIGMA_Y * 1/128))
         print(" |____ Sigma V (Standard Deviation On The GroundSpeed): %.2f kt"  % (SIGMA_V * 0.22))
         print(" |____ Sigma X (Standard Deviation On Horizontal axis): %.2f deg" % (SIGMA_H * 0.08789))

def MODE_2_CODE(cat):
    MODE_2_CODE1 = rdbt.readbyte()
    MODE_2_CODE2 = rdbt.readbyte()
    MODE_2_CODE  = (MODE_2_CODE1 << 8) |  MODE_2_CODE2
    MODE_2_CODE_OCTAL  =  (MODE_2_CODE & 0xFFF) # 0xFFF = 4095

    if(cat == 1):

        print("+---I001/050 [MODE-2 CODE IN OCTAL]")
    elif(cat == 48):
        print("+---I048/050 [MODE-2 CODE IN OCTAL]")

    if(MODE_2_CODE1 & 128):
        print(" |____ V: 1 : Not Validated")
    else:
        print(" |____ V: 0 : Code Validated")

    if(MODE_2_CODE1 & 64):
        print(" |____ G: 1 : Garbled Code")
    else:
        print(" |____ G: 0 : Default")

    if(MODE_2_CODE1 & 32):
        print(" |____ L: 1 : Mode-2 Code Derived From the Reply Of The Transponder")

    print(" |____ Mode2_code : [%s]" % bin(MODE_2_CODE_OCTAL))  

def MODE_3_CONF(cat):
    MCODE_3_CONFIDENCE1 = rdbt.readbyte()
    MCODE_3_CONFIDENCE2 = rdbt.readbyte()

    MCODE_3_CONFIDENCE  = (MCODE_3_CONFIDENCE1 << 8) | MCODE_3_CONFIDENCE2
    MCODE_3_CONFIDENCE_IND = MCODE_3_CONFIDENCE >> 4

    if (cat == 1):
        print("+---I001/080 [MCODE_3A_CONFIDENCE] :")
    elif(cat == 48):
        print("+---I048/080 [MCODE_3A_CONFIDENCE] :")

    print(" |____ MCODE-3A CONFIDANCE INDICATOR : [%s]" % bin(MCODE_3_CONFIDENCE_IND))
    print(" |____ bits 13-16: Spare bits set to 0")

def MODE_C_CODE_CONF(cat):
    MODE_C_CODE_AND_CODE_CONF1 = rdbt.readbyte()
    MODE_C_CODE_AND_CODE_CONF2 = rdbt.readbyte()
    MODE_C_CODE_AND_CODE_CONF3 = rdbt.readbyte()
    MODE_C_CODE_AND_CODE_CONF4 = rdbt.readbyte()

    MODE_C_CODE_1_16  = (MODE_C_CODE_AND_CODE_CONF1 << 8) | MODE_C_CODE_AND_CODE_CONF2
    MODE_C_CODE_17_32 = (MODE_C_CODE_AND_CODE_CONF3 << 8) | MODE_C_CODE_AND_CODE_CONF4

    MODE_C_GRAY                     =  MODE_C_CODE_17_32 >> 4
    MODE_C_CODE_QUALITY_PULSE       =  MODE_C_CODE_1_16 >> 4

    MODE_C_V = (MODE_C_CODE_AND_CODE_CONF1 & 128)
    MODE_C_G = (MODE_C_CODE_AND_CODE_CONF1 & 64)

    if(cat == 1):
        print("+---I001/100 [MODE-C Code & Confidence Indicator]:")
    elif(cat == 48):
        print("+---I048/100 [MODE-C Code & Confidence Indicator]:")

    if(MODE_C_V):   
        print(" |____ V: 1 : Code Not Validated")
    else:
        print(" |____ V: 0 : Code Validated")
    if(MODE_C_G):
        print(" |____ G: 1 : Garbled Code")
    else:
        print(" |____ G: 0 : Default")

    print(" |____ Mode-C replay in Gray Notation" % MODE_C_GRAY)
    print(" |____ Quality Pulse :[%s]" % bin(MODE_C_CODE_QUALITY_PULSE))

def MODE_2_IND(cat):
    MODE_2_CONFIDENCE_IND1 = rdbt.readbyte()
    MODE_2_CONFIDENCE_IND2 = rdbt.readbyte()

    MODE_2_CONF = (MODE_2_CONFIDENCE_IND1 << 8) | MODE_2_CONFIDENCE_IND2
    MODE_2_CONF_QUALITY = MODE_2_CONF >> 4

    if(cat == 1):
        print("+---I001/060 [Mode-2 Code Confidence Indicator]")
    elif(cat == 48):
        print("+---I048/060 [Mode-2 Code Confidence Indicator]")

    print(" |____ Quality Pulse %s" % bin(MODE_2_CONF_QUALITY))
    print(" |____ bits 13-16: Spare bits set to 0")

def WARNING(cat):
    WARNING1 = rdbt.readbyte()
    WAR = WARNING1 >> 1
    if(cat == 1):
        print("+---I001/030 [Warning Code]: [%s]" % bin(WAR))
    elif(cat == 48):
        print("+---I048/030 [Warning Code]: [%s]" % bin(WAR))

    print("\nN.B: See The Documentation To Know More About Warnings Bits\n")

    
    if(WARNING1 & 1):
        EXT = rdbt.readbyte()
        print(" |____ WARNING EXTENSION BYTE: [%s]" % bin(EXT))


def X_PULSE():
    print("+---I001/150 [X-PULSE] Exists:")
    X_PULSE = rdbt.readbyte()
    if(X_PULSE & 128):
        print(" |____ XA : 1 : X-Pulse Received in Mode-3A Reply")
    else:   
        print(" |____ XA : 0 : Default")
    print(" |____ bit-7 : Set to 0")    
    if(X_PULSE & 32):
        print(" |____ XC : 1 : X-Pulse Received in Mode-C Reply")   
    else:
        print(" |____ XC : 0 : Default")

    print(" |____ bits-5-4 : Set to 0")
    
    if(X_PULSE & 4):
        print(" |____ X2 : 1 : X-Pulse Received in Mode-2 Reply")
    else:   
        print(" |____ X2 : 0 : Default")

    print(" |____ bits2-1 : Set to 0")          
    
def READ_SIC_SAC(cat):
    if (cat == 1):
        print ("+---I001/010 [Data Source Identifier]")
    elif(cat == 48):
        print ("+---I048/010 [Data Source Identifier]")
    SAC = rdbt.readbyte()
    print(" |____ SAC : %d" % SAC)
    SIC = rdbt.readbyte()
    print(" |____ SIC : %d\n" % SIC)    

def READ_DESCRIPTOR(cat):

    if(cat == 48):
        Glob.track = 0
        Glob.plot  = 0 

    DES1 = rdbt.readbyte()
    if(cat == 1):
        print("+---I001/020 [Target Report Descriptor] %s: " % bin(DES1))
    elif(cat == 48):
        print("+---I048/020 [Target Report Descriptor] %s: " % bin(DES1))
    if (DES1 & 1):  # Test if the Extension bit is Set
        DES2 = rdbt.readbyte()
        print("+---DES2 %s: 1 : [Target Report Descriptor]" % bin(DES2))
    
    '''
    Here we Get TYP bit
    '''
    if (cat == 48):
        TYP = DES1 >> 5
        if (TYP == 7):
            print(" |____ DES.TYP : 111 : ModeS Roll-Call+PSR")
        elif(TYP == 6):
            print(" |____ DES.TYP : 110 : ModeS All-Call+PSR")
        elif(TYP == 5):
            print(" |____ DES.TYP : 101 : Single ModeS Roll-Call")
        elif(TYP == 4):
            print(" |____ DES.TYP : 100 : Single ModeS All-Call")
        elif(TYP == 3):
            print(" |____ DES.TYP : 011 : SSR+ PSR Detection")
        elif(TYP == 2):
            print(" |____ DES.TYP : 010 : Single SSR detection")
        elif(TYP == 1):
            print(" |____ DES.TYP : 001 : Single PSR detection")
        elif(TYP == 0):
            print(" |____ DES.TYP : 000 : No detection")

                                               

    elif(cat == 1):
            
        if (DES1 & 128):
            print(" |____ DES.TYP : 1 : There is Track information (Not Plot)")
            Glob.track = 1
            Glob.plot  = 0
        else:
            print(" |____DES.TYP : 0 :There is Plot information  (Not Track)")
            Glob.plot  = 1
            Glob.track = 0

    if (cat == 48):
        if(DES1 & 16):
            print(" |____ DES.SIM : 1 : Simulated Target Report ")
        else:
            print(" |____ DES.SIM : 0 : Actual Target Report ")
        
        if(DES1 & 8):
            print(" |____ DES.RDP : 1 : Report From RDP Chain 2 ")
        else:
            print(" |____ DES.RDP : 0 : Report From RDP Chain 1 ")
    
    elif (cat == 1):
        '''
        Here we Get SIM bit
        ''' 
        if(DES1 & 64):
            if (Glob.track): 
                print(" |____ DES.SIM : 1 : Simulated Track \n")    
            if(Glob.plot):
                print(" |____ DES.SIM : 1 : Simulated Plot \n")

        else:       
            if (Glob.track): 
                print(" |____ DES.SIM : 0 : Actual Track ") 
            if(Glob.plot):
                print(" |____ DES.SIM : 0 : Actual Plot ")
    
        '''
        Here we Get SSR/PSR bits
        '''
        Test = (DES1 & 48) >> 4     
        
        if(Test == 3 ):
                print(" |____ DES.SSR/PSR : 11 : Primary + Secondary Detection ")
        
        if(Test == 2):
            
            print(" |____ DES.SSR/PSR : 10 : Secondary Detection ")     

        if(Test == 1):
            print(" |____ DES.SSR/PSR : 01 : Primary Detection ")

        if(Test == 0):

            print(" |____ DES.SSR/PSR : 00 : No Detection ")    

        '''
        Here we Get ANT bit
        ''' 
        if(DES1 & 8):
            print(" |____ DES.ANT : 1 : Report from Antenna 2 ")
        else:
            print(" |____ DES.ANT : 0 : Report from Antenna 1 ")    

    if(DES1 & 4):
        print(" |____ DES.SPI : 1 : Special Position Identification ")
    else:
        print(" |____ DES.SPI : 0 : Default (No SPI) ")
    if(DES1 & 2):
        if (cat == 1):
            print(" |____ DES.RAB : 1 : Track/Plot from a Fixed Trasnponder ")
        elif(cat == 48):
            print(" |____ DES.RAB : 1 : Report from a Fixed Trasnponder (Field Monitor) ")
    
    else:
        if (cat == 1):
            print(" |____ DES.RAB : 0 : Default (Track/Plot Not From Fixed Transponder) ")
        elif(cat == 48):
            print(" |____ DES.RAB : 0 : Report from aircraft transponder")
    
    if(DES1 & 1):
        DES2 = rdbt.readbyte()
        print(" |____ DES.FX : 1 : Extension %s exists" % bin(DES2))
    else:
        print(" |____ DES.FX : 0 : Extension Does not exist")       

    if(cat == 1):
        print("-----------------------------------------------------------------")      
        print("DES.TYP bit (Track/Plot) decides The Order of the Next Data Items")      
        print("-----------------------------------------------------------------")
    
def TRACK_NUMBER(cat):
    if(cat == 1):
        print ("Track :")
        TRACKN1 = rdbt.readbyte()
        TRACKN2 = rdbt.readbyte()
        TRACKN  = (TRACKN1 << 8) | TRACKN2
        print("+---I001/161 [TRACKN NUMBER]: %d " % TRACKN)
    elif(cat == 48):
        TRACKN1 = rdbt.readbyte()
        TRACKN2 = rdbt.readbyte()
        TRACKN  = (TRACKN1 << 8) | TRACKN2
        print("+---I048/161 [TRACKN NUMBER]: %d " % TRACKN)

def FLIGHT_LEVEL():
    FL1 = rdbt.readbyte()
    FL2 = rdbt.readbyte()
    FL   = (FL1 << 8) | (FL2)
    print("+---I048/090 [FLIGHT LEVEL IN BINARY REPRESENTATION]: %s" % bin(FL))

    FL_V = (FL1 & 128)
    FL_L = (FL1 & 64)

    if(FL_V):
        print(" |____ V: 1 : Code not Validated")
    else:
        print(" |____ V: 0 : Code Validated")

    if(FL_L):
        print(" |____ L: 1 : Code Garbled")
    else:
        print(" |____ L: 0 : Default (Code Not Garbled)")

    LEV = (FL & 0x3FFF)
    print(" |____ Flight Level : (%d) %.2f FL" % (LEV , (LEV * 1/4)))              

def AIRCRAFT_ADD():
    air_craft = rdbt.readbyte()

    add1      = rdbt.readbyte()
    add2      = rdbt.readbyte()

    address = (add1 << 8) | add2    

    print("+---I048/220 [Aircraft Address]:")

    print(" |____Aircraft: 0x%x (%d)" % (air_craft, air_craft))
    print(" |____Address : 0x%x (%d)" % (address, address))

def AIRCRAFT_ID():
    Octet1=rdbt.readbyte()
    Octet2=rdbt.readbyte()
    Octet3=rdbt.readbyte()
    Octet4=rdbt.readbyte()
    Octet5=rdbt.readbyte()
    Octet6=rdbt.readbyte()

    Char1 = Octet1 >> 2
    Char2 = ((Octet1<<4)& 0x3F) | (Octet2 >> 4)
    Char3 = ((Octet2<<2) & 0x3F) | (Octet3 >> 6)
    Char4 = (Octet3 & 0x3F)
    Char5 = (Octet4>>2)
    Char6 = ((Octet4<<4)& 0x3F) | (Octet5 >> 4)
    Char7 = ((Octet5<<2) & 0x3F) | (Octet6 >> 6)
    Char8 = (Octet6 & 0x3F)
    #print("%x%x%x%x%x%x" % (Octet1, Octet2, Octet3, Octet4, Octet5, Octet6))
    #print("%x%x%x%x%x%x%x%x" % (Char1, Char2, Char3,Char4, Char5, Char6,Char7,Char8))
    print("\n+---I048/240 [AIRCRAFT ID]: [%s][%s][%s][%s][%s][%s][%s][%s]" % (bin(Char1),bin(Char2),bin(Char3),bin(Char4),bin(Char5),bin(Char6),bin(Char7),bin(Char8)))  
    
    C1 = SIX_BITS_CHAR(Char1)
    C2 = SIX_BITS_CHAR(Char2)
    C3 = SIX_BITS_CHAR(Char3)
    C4 = SIX_BITS_CHAR(Char4)
    C5 = SIX_BITS_CHAR(Char5)
    C6 = SIX_BITS_CHAR(Char6)
    C7 = SIX_BITS_CHAR(Char7)
    C8 = SIX_BITS_CHAR(Char8)

    print ("    |")
    print ("    |____ %s%s%s%s%s%s%s%s" % (C1,C2,C3,C4,C5,C6,C7,C8))
    
    Name = C1 + C2 + C3
    for name in airline_code:
        if (name[0] == Name):
            print (" %s => %s" % (name[0],name[1]))
            
def MODE_SMB_DATA():
    print("+---I048/250 [MODE S MB DATA]")
    REP = rdbt.readbyte()
    print(" |   (There Are %d MBData Blocks/ See refrences for BDS Codes Formats)" % REP)
    
    while (REP):
        MB1 = rdbt.readbyte()
        MB2 = rdbt.readbyte()
        MB3 = rdbt.readbyte()
        MB4 = rdbt.readbyte()
        MB5 = rdbt.readbyte()
        MB6 = rdbt.readbyte()
        MB7 = rdbt.readbyte()
        print(" |____ MBdata%d: %x%x%x%x%x%x%x" % (REP, MB1,MB2,MB3,MB4,MB5,MB6,MB7))

        BDS  = rdbt.readbyte()
        BDS1 = (BDS >> 4)
        BDS2 = (BDS & 0x0F)
        print(" |____ BDS %d.%d code" % (BDS1,BDS2))
        
        # Extract BDS Codes Infos/ See refrences for BDS Codes Formats
        # according to the BDS code number.
        
        #Debut Traitement des BSD 4/5/6 -----------------------------------------------------------------------------

        #Traitement des Donnees BDS 4.0
        if((BDS1 == 4) and (BDS2 == 0)):   
            if(MB1 & 128):
                FCU = (MB1 << 8) | MB2
                FCU = (FCU & 0x7FFF) >> 3
                print("     |___MCP/FCU Selected Altitude :% .2f ft" % (FCU * 16))
            if(MB2 & 4):
                FMS = ((MB2 & 0x3) << 8) | MB3  
                FMS = (FMS << 2) | (MB4 >> 6)    
                print("     |___FMS Selected Altitude :% .2f ft" % (FMS * 16))
            if(MB4 & 32):
                BARO_PRESSURE = ((MB4 & 0x1F)<<8) | MB5
                BARO_PRESSURE = BARO_PRESSURE >> 1 
                print("     |___Barometric Pressure :% .2f mb" % ((BARO_PRESSURE * 0.1) + 800))
            print("     |___bits40-47: reserved")           
            if(MB6 & 1):
                if(MB7 & 128):
                    print("     |___VNAV Mode: Active")
                if(MB7 & 64):
                    print("     |___Alt Hold Mode: Active")             
                if(MB7 & 32):
                    print("     |___Approach Mode: Active")
                                            
            print("     |___bits52-53: reserved")
            if(MB7 & 4):
                if(MB7 == 0):
                    print("     |___Target Alt Source: UNKNOWN")
                elif(MB7 == 1):
                    print("     |___Target Alt Source: AIRCRAFT Altitude")
                elif(MB7 == 2):
                    print("     |___Target Alt Source: FCU/MCP Selected Altitude")
                elif(MB7 == 3):
                    print("     |___Target Alt Source: FMS Selected Altitude")
            print("\n")

        #Traitement des Donnees BSD 5.0     
        elif((BDS1 == 5) and (BDS2 == 0)):
            if(MB1 & 128):
                ROLL = ((MB1 << 8) | MB2)
                ROLL = ((ROLL & 0x3FE0) >> 5)
                if(MB1 & 64):
                    print("     |___Rolling (to left) Angle: -%.2f deg" % (ROLL * 45/256))
                else:
                    print("     |___Roll (to right) Angle: %.2f deg" % (ROLL * 45/256))
            if(MB2 & 10):
                TRUE_ANGLE = (MB2 << 8) | MB3
                TRUE_ANGLE = (TRUE_ANGLE & 0x7FE) >> 1
                if (MB2 & 8):
                    print("     |___ True Track (to WEST) Angle: -%.2f deg" % (TRUE_ANGLE * 90/512))
                else:
                    print("     |___ True Track (to EAST) Angle: %.2f deg" % (TRUE_ANGLE * 90/512))
            if(MB3 & 1):
                GROUND_SPEED = (MB4 << 8) | MB5
                GROUND_SPEED = (GROUND_SPEED & 0xFFC0) >> 6
                print("     |___Ground Speed: %.2f Knots" % (GROUND_SPEED * 2))
            if(MB5 & 32):
                TRACK_ANGLE_RATE = (MB5 << 8) | MB6
                TRACK_ANGLE_RATE = (TRACK_ANGLE_RATE & 0xFF8) >> 3
                if(MB5 & 16):
                    print("     |___ Track Angle Rate: -%.2f deg/sec" % (TRACK_ANGLE_RATE * 8/256))             
                
                else:
                    print("     |___ Track Angle Rate: %.2f deg/sec" % (TRACK_ANGLE_RATE * 8/256))

            if(MB6 & 4):
                TRUE_AIR_SPEED = (MB6 << 8) | MB7
                TRUE_AIR_SPEED = (TRUE_AIR_SPEED & 0x3FF)
                print("     |___ True Air Speed: %.2f knots" % (TRUE_AIR_SPEED * 2))
    
            print("\n")

        #Traitement des Donnees de BSD 6.0
        elif((BDS1 == 6) and (BDS2 == 0)):
            if(MB1 & 128):
                MAGN_HEAD = (MB1 << 8) | MB2
                MAGN_HEAD = (MAGN_HEAD & 0x3FF0) >> 4
                if(MB1 & 64):
                    print("     |___ Magnetic Heading : -%.2f deg" % (MAGN_HEAD * 90/512)) 
                else:
                    print("     |___ Magnetic Heading : %.2f deg" % (MAGN_HEAD * 90/512))

            if(MB2 & 8):
                INDIC_AIR_SPEED = (MB2 << 8) | MB3
                INDIC_AIR_SPEED = (INDIC_AIR_SPEED & 0x7FE) >> 1
                print("     |___ Indicated Air Speed : %.2f knots" % (INDIC_AIR_SPEED * 1))     
            if(MB3 & 1):
                MACH_NBR = (MB3 << 8) | MB4
                MACH_NBR = (MACH_NBR & 0xFFC0) >> 6
                print("     |___ Mach Number : %.4f Mach" % (MACH_NBR * (2.048/512)))
            if(MB4 & 32):
                BARO_ALT_RATE = (MB5 << 8) | MB6
                BARO_ALT_RATE = (BARO_ALT_RATE & 0xFF8) >> 3 
                
                if(MB4 & 16):                   
                    print("     |___ Barometric Altitude Rate: -%.2f feet/min" % (BARO_ALT_RATE * 32))
                else:
                    print("     |___ Barometric Altitude Rate: %.2f feet/min" % (BARO_ALT_RATE * 32))


            if(MB6 & 4):
                INER_ALT_RATE = (MB6 << 8) | MB7
                INER_ALT_RATE = (INER_ALT_RATE & 0x1FF)
                if (MB6 & 2):
                    print("     |___ Inertial Altitude Rate: -%.2f feet/min" % (INER_ALT_RATE * 32))
                else:
                    print("     |___ Inertial Altitude Rate: %.2f feet/min" % (INER_ALT_RATE * 32)) 

            print("\n")
        #Fin Traitement des BSD 4/5/6 -----------------------------------------------------------------------------         

        REP = REP - 1

def HIEGH_3D():
    H1 = rdbt.readbyte()
    H2 = rdbt.readbyte()

    H = ((H1 & 0x1F) << 8) | H2

    print("+---I048/110 [HEIGHT MEASURED BY 3D RADAR]")
    if(H1 & 32):
        
        print(" |____ 3D-Height: -%d ft" % (H * 25))
    else:

        print(" |____ 3D-Height:  %d ft" % (H * 25))    



def COMM_ACAS_CAP_FLY_STAT():
    print("+---I048/230 [COMM ACAS CAPABILITY & FLIGHT STATUS]")
    C1 = rdbt.readbyte()
    C2 = rdbt.readbyte()

    COM = ((C1 & 0xE0) >> 5)
    if(COM == 0):
        print(" |____ COM: 000 : No Communication Capability")
    elif(COM == 1):
        print(" |____ COM: 001 : Comm_A & Comm_B Capabilities")
    elif(COM == 2):
        print(" |____ COM: 010 : Comm_A & Comm_B & UpLINK ELM")
    elif(COM == 3):
        print(" |____ COM: 011 : Comm_A & Comm_B & UpLINK & DownLINK ELM")
    elif(COM == 4):
        print(" |____ COM: 100 : Level 5 Transponder Capability")

    STAT = ((C1 & 0x1C) >> 2)
    if(STAT == 0):
        print(" |____ STAT: 000 : No Alert + No SPI + aircraft airborne")
    elif(STAT == 1):    
        print(" |____ STAT: 001 : No Alert + No SPI + aircraft On Ground")
    elif(STAT == 2):
        print(" |____ STAT: 010 : Alert + No SPI + aircraft airborne")
    elif(STAT == 3):
        print(" |____ STAT: 011 : Alert + No SPI + aircraft on Ground")
    elif(STAT == 4):
        print(" |____ STAT: 100 : Alert + SPI + aircraft airborne OR On Ground")
    elif(STAT == 5):
        print(" |____ STAT: 101 : No Alert + SPI + aircraft airborne OR On Ground")

    if(C1 & 2):
        print(" |____ SI: 1 : SI/II Transponder Capability")
    print(" |____ bit9: Spare bit set to 0")
    
    if(C2 & 128):
        print(" |____ MSSC: 1 : Mode-S Specific Service Capability (YES)")
    else:
        print(" |____ MSSC: 0 : Mode-S Specific Service Capability (NO)")   
    if(C2 & 64):
        print(" |____ ARC : 1 : Altitude Reporting Capability (25ft Resolution)")
    else:
        print(" |____ ARC : 0 : Altitude Reporting Capability (100ft Resolution)")                      
                    
    if(C2 & 32):
        print(" |____ AIC : 1 : Aircraft Identification Capability (YES)")
    else:
        print(" |____ AIC : 0 : Aircraft Identification Capability (NO)")
    
    B1A = ((C2 & 0x10) >> 4)
    print(" |____ B1A : BDS1.0 bit 16 = %d" % B1A)
    
    
    B1B = C2 & 0xF
    print(" |____ B1B : BDS1.0 bits37/40 = %s" % bin(B1B))  
            
            
def ACAS_RES_ADV_REPORT():
    print("+---I048/260 [ACAS RESOLUTION ADVISORY REPORT]")

    AC1= rdbt.readbyte()
    AC2= rdbt.readbyte()
    AC3= rdbt.readbyte()
    AC4= rdbt.readbyte()
    AC5= rdbt.readbyte()
    AC6= rdbt.readbyte()
    AC7= rdbt.readbyte()
    
    print(" |____ Mode S Comm B Message Data of BDS 3.0 :\n |____[%x%x%x%x%x%x%x]" % (AC1,AC2,AC3,AC4,AC5,AC6,AC7))


def MODE1_CODE_OCTAL():
    print("+---I048/055 [MODE 1 CODE OCTAL REPRESENTATION]")
    M1 = rdbt.readbyte()
    if(M1 & 128):
        print(" |____ V: 1 : Code Not Validated")
    else:
        print(" |____ V: 0 : Code Validated")   
    if(M1 & 64):
        print(" |____ G: 1 : Garbled Code")
    else:
        print(" |____ G: 0 : Code Not Garbled")     

    if(M1 & 32):
        print(" |____ L: 1 : Mode-1 Code As Derived From the Reply Transponder")
    else:
        print(" |____ L: 0 : Smoothed Mode-1 Code as Provided by Local Tracker")
    Mode1_code = (M1 & 0x1F)
    print(" |____ Mode-1 Code: [%s]" % bin(Mode1_code))

def MODE1_CONF():
    print("+---I048/065 [MODE 1 CODE CONFIDENCE INDICATOR")
    CO = rdbt.readbyte()
    MO1_CONF = (CO & 0x1F)
    print( "|____Mode-1 Confidence Indicator: [%s]" % bin(MO1_CONF))


def Decode_48():
    if(Glob.FSPEC1 & 128):
        
        READ_SIC_SAC(Glob.cat)
    else:
        print("Should Have an Identifier. Inspect Where is the Problem")
        sys.exit()

    if(Glob.FSPEC1 & 64):
        TIME1 = rdbt.readbyte()
        TIME2 = rdbt.readbyte()
        TIME3 = rdbt.readbyte()

        TIME  = (TIME1 << 16) | (TIME2 << 8) | (TIME3)

        print("+---I048/140 [Time Stamping] : %f sec" % (TIME * 1/128)) 
    
    if(Glob.FSPEC1 & 32):
        READ_DESCRIPTOR(Glob.cat)
    if(Glob.FSPEC1 & 16):
        POLAR_CORD(Glob.cat)                             
    if(Glob.FSPEC1 & 8):
        MODE3_A_REPLAY_OCTAL(Glob.cat)
    if(Glob.FSPEC1 & 4):
        FLIGHT_LEVEL()
    if(Glob.FSPEC1 & 2):
        RADAR_PLOT_CHARAC(Glob.cat)
    if (Glob.FSPEC1 & 1):
        if(Glob.FSPEC2 & 128):
            AIRCRAFT_ADD()
        if(Glob.FSPEC2 & 64):
            AIRCRAFT_ID()
        if(Glob.FSPEC2 & 32):
            MODE_SMB_DATA()
        if(Glob.FSPEC2 & 16):
            TRACK_NUMBER(Glob.cat)   
        if(Glob.FSPEC2 & 8):
            CARTESIAN_CORD()
        if(Glob.FSPEC2 & 4):
            TRACK_VELOCITY(Glob.cat)
        if(Glob.FSPEC2 & 2):
            TRACK_STATUS(Glob.cat)
        if(Glob.FSPEC2 & 1):
            if(Glob.FSPEC3 & 128):
                TRACK_QUALITY(Glob.cat)
            if(Glob.FSPEC3 & 64):
                WARNING(Glob.cat)
            if(Glob.FSPEC3 & 32):
                MODE_3_CONF(Glob.cat)        
            if(Glob.FSPEC3 & 16):
                MODE_C_CODE_CONF(Glob.cat)
            if(Glob.FSPEC3 & 8):
                HIEGH_3D()
            if(Glob.FSPEC3 & 4):
                RADIAL_DOPPLER_SPEED(Glob.cat)
            if(Glob.FSPEC3 & 2):
                COMM_ACAS_CAP_FLY_STAT()
            if(Glob.FSPEC3 & 1):
                if(Glob.FSPEC4 & 128):
                    ACAS_RES_ADV_REPORT()
                if(Glob.FSPEC4 & 64):
                    MODE1_CODE_OCTAL()
                if(Glob.FSPEC4 & 32):
                    MODE_2_CODE(Glob.cat)
                if(Glob.FSPEC4 & 16):
                    MODE1_CONF()
                if(Glob.FSPEC4 & 8):
                    MODE_2_IND(Glob.cat)
                if(Glob.FSPEC4 & 4):
                    SP_DATA = rdbt.readbyte()
                    print("SP data: %d" % SP_DATA)
                    if(SP_DATA & 128 ):
                        SP_DATA_EXT1 = rdbt.readbyte()
                        print("SP data EXT 1: %d" % SP_DATA_EXT1)
                        if(SP_DATA_EXT1 & 128):
                            SP_DATA_EXT2 = rdbt.readbyte()
                            print("SP data EXT 2: %d" % SP_DATA_EXT2)
                if(Glob.FSPEC4 & 2):
                    RE_DATA = rdbt.readbyte()
                    print("RE data: %d" % RE_DATA)
                    if(RE_DATA & 128 ):
                        RE_DATA_EXT1 = rdbt.readbyte()
                        print("RE data EXT 1: %d" % RE_DATA_EXT1)
                        if(RE_DATA_EXT1 & 128):
                            RE_DATA_EXT2 = rdbt.readbyte()
                            print("RE data EXT 2: %d" % RE_DATA_EXT2)           


def Decode_01():
    if(Glob.FSPEC1 & 128):
        
        READ_SIC_SAC(Glob.cat)
    else:
        print("Should Have an Identifier. Inspect Where is the Problem")
        sys.exit()

    if(Glob.FSPEC1 & 64):
        READ_DESCRIPTOR(Glob.cat)
    
    if(Glob.FSPEC1 & 32):
        if(Glob.track):
            TRACK_NUMBER(Glob.cat)
        else:
            print ("Plot :")
            POLAR_CORD(Glob.cat)
    
    if(Glob.FSPEC1 & 16) :
        if(Glob.track):
            print ("Track :")
            POLAR_CORD(Glob.cat)

        else:
            print ("Plot :")
            MODE3_A_REPLAY_OCTAL(Glob.cat)

    if(Glob.FSPEC1 & 8):
        if(Glob.track):
            print ("Track :")
            CARTESIAN_CORD()
        else:
            print ("Plot :")
            MODE_C_BINARY()

    if(Glob.FSPEC1 & 4):
        if(Glob.track):
            print ("Track :")
            TRACK_VELOCITY(Glob.cat)
        else:
            print("Plot :")
            RADAR_PLOT_CHARAC(Glob.cat)

    if(Glob.FSPEC1 & 2):
        if(Glob.track):
            print ("Track :")
            MODE3_A_REPLAY_OCTAL(Glob.cat)
        else:
            print ("Plot :")
            TRUNCATED_TIME()

    if (Glob.FSPEC1 & 1):

    #FSPEC 2        
        if(Glob.FSPEC2 & 128):
            if(Glob.track):
                print ("Track :")
                MODE_C_BINARY()
            else:
                print ("Plot :")
                MODE_2_CODE(Glob.cat)
        if(Glob.FSPEC2 & 64):
            if (Glob.track):
                print ("Track :")
                TRUNCATED_TIME()
            else:
                print ("Plot :")
                RADIAL_DOPPLER_SPEED(Glob.cat)       
        if(Glob.FSPEC2 & 32):
            if(Glob.track):
                print ("Track :")
                RADAR_PLOT_CHARAC(Glob.cat)
            else:
                print ("Plot :")
                RECIEVED_POWER()    
        if(Glob.FSPEC2 & 16):
            if(Glob.track):
                print ("Track :")
                RECIEVED_POWER()
            else:
                print ("Plot :")
                MODE_3_CONF(Glob.cat)
        if(Glob.FSPEC2 & 8):
            if(Glob.track):
                print ("Track :")
                RADIAL_DOPPLER_SPEED(Glob.cat)
            else:
                print ("Plot :")
                MODE_C_CODE_CONF(Glob.cat)   
        if(Glob.FSPEC2 & 4):
            if(Glob.track):
                print ("Track :")
                TRACK_STATUS(Glob.cat)
            else:
                print ("Plot :")
                MODE_2_CONF()
        if(Glob.FSPEC2 & 2):
            if(Glob.track):
                print ("Track :")
                TRACK_QUALITY(Glob.cat)
            else:
                print ("Plot :")
                WARNING(Glob.cat)
    # Glob.FSPEC3
        if(Glob.FSPEC2 & 1):
            if(Glob.FSPEC3 & 128):

                if(Glob.track):
                    print ("Track :")
                    MODE_2_CODE(Glob.cat)            
                else:
                    print ("Plot :")
                    X_PULSE()
            
            if(Glob.FSPEC3 & 64):
                if(Glob.track):
                    print ("Track :")
                    MODE_3_CONF(Glob.cat)
                else:
                    print ("Plot :")
                    print("Just Empty For Plot Infos.") 
            if(Glob.FSPEC3 & 32):
                if(Glob.track):
                    print ("Track :")
                    MODE_C_CODE_CONF(Glob.cat)
                else:
                    print ("Plot :")
                    print("Just Empty For Plot Infos.")     
            if(Glob.FSPEC3 & 16):

                if(Glob.track):
                    print ("Track :")
                    MODE_2_IND(Glob.cat)
                else:
                    print ("Plot :")
                    print("Just Empty For Plot Infos.")     
            if (Glob.FSPEC3 & 8):
                if(Glob.track):
                    print ("Track :")
                    WARNING(Glob.cat)
                else:
                    print ("Plot :")
                    print("Just Empty For Plot Infos.")     
                
            if (Glob.track):
                print ("Track :")       
                if (Glob.FSPEC3 & 1):
                    X_PULSE()
