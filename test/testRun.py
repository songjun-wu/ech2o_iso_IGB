import os
import sys

os.chdir('../Release-Linux/')

try:
    os.system('make clean')
    os.system('make')
except:
    print('Error in make')
    sys.exit()
else:
    os.system('cp ~/Documents/ech2o_iso_igb/Release-Linux/ech2o_iso ~/Documents/ech2o_iso_igb/test/ech2o_iso')





