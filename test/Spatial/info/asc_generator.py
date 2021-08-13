import numpy as np

def add_nodata(arr):
    arr[0,:] = -9999.0
    arr[-1,:] = -9999.0
    arr[:,0] = -9999.0
    arr[:,-1] = -9999.0
    return arr


name_list = ['dem','chanmask','chanwidth','ClimZones','patches','type1','type2']

# DEM
tmp = np.full((12,7),0.0)
for i in range(12):
    tmp[i,:]=[0, 56-i*0.2,55-i*0.2,54-i*0.2,55-i*0.2,56-i*0.2, 0]
add_nodata(tmp)
np.savetxt(name_list[0]+'.asc', tmp)

#chanmask
tmp = np.full((12,7),0.0)
tmp[:,3] = 1
add_nodata(tmp)
np.savetxt(name_list[1]+'.asc', tmp)

# chanwidth
for i in range(10):
    tmp[i,3] += 0.05*i+2
add_nodata(tmp)
np.savetxt(name_list[2]+'.asc', tmp)

#ClimZones
tmp = np.full((12,7),1.0)
add_nodata(tmp)
np.savetxt(name_list[3]+'.asc', tmp)

#patches
tmp = np.full((12,7),2.0)
for i in range(3):
    tmp[:,i] = 1.0
add_nodata(tmp)
np.savetxt(name_list[4]+'.asc', tmp)

# type1
tmp = np.full((12,7),0.0)
for i in range(3):
    tmp[:,i] = 1.0
add_nodata(tmp)
np.savetxt(name_list[5]+'.asc', tmp)
tmp2 = np.full((12,7),1.0) - tmp
add_nodata(tmp2)
np.savetxt(name_list[6]+'.asc', tmp2)





line1 = 'ncols 7'
line2 = 'nrows 12'
line3 = 'xllcorner 441700'
line4 = 'yllcorner 5797500'
line5 = 'cellsize 250'
line6 = 'NODATA_value -9999'
for name in name_list:
    with open('./'+name+'.asc', 'r+') as f:
        content = f.read()
        f.seek(0,0)
        f.write(line1+'\n'+line2+'\n'+line3+'\n'+line4+'\n'+line5+'\n'+line6+'\n'+content)
