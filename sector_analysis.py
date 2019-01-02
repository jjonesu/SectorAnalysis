### JHJ 1-2-2019 (jjonesu@gmu.edu and GitHub user jjonesu)
# Simple sector analysis
# outputs sector number: hash, entropy measure, all 0xFF, all 0x00

import hashlib
import binascii
import gzip

# for debugging
#import pdb
#pdb.set_trace()
#

def analyzeSectors(f,s,o):
    sector_number = 0
    data = f.read(s)
    while(len(data) == s):
        print("SectorNumber: " + str(sector_number))
        if (o[0] == 'y'): # hash
            hash_value_raw = hashlib.md5(data).digest()
            hash_value = (str(binascii.b2a_hex(hash_value_raw)))[2:-1]
            print("    Hash: " + hash_value)
        if (o[1] == 'y'): # entropy
            # generally accepted entropy approximation...
            entropy = len(gzip.compress(data))/len(data) 
            print("    Entropy: " + str(entropy))
        if (o[2] == 'y'): # all 0xFF
            xFF='yes'
            for c in range (0,s-1,1):
                if (data[c] != 255): # 0xFF = int 255
                    xFF='no'
                    break
            print("    All 0xFF: " + xFF)
        if (o[3] == 'y'): # all 0x00
            x00='yes'
            for c in range (0,s-1,1):
                if (data[c] != 0): # 0x00 = int 0
                    x00='no'
                    break
            print("    All 0x00: " + x00)
        data = f.read(s)
        sector_number += 1

if __name__ == '__main__':
    ### change these:
    filename = "172641C01_VERIFONE_VX610_CHIPOFF_RBO2.BIN"
    sector_size = 65536
    output = 'yyyy' # y/n for hash, entropy measure, all 0xFF, all 0x00
    ###
    file_handle = open(filename,'rb')
    analyzeSectors(file_handle, sector_size, output)
