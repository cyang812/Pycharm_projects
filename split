# coding=utf-8

import sys,os

kilobytes = 1024
megabytes = kilobytes*1000
chunksize = int(200*megabytes)#default chunksize
char = 'f7 b7' 
#partnum = '0'
#partnum_hex = '00 00'

def getPartSum(fromfile,chunksize):
    if os.path.getsize(fromfile)%chunksize != 0:
        return int(os.path.getsize(fromfile)/chunksize)+1
    else:
        return int(os.path.getsize(fromfile)/chunksize)

def split(fromfile,todir,chunksize=chunksize):
    if not os.path.exists(todir):#check whether todir exists or not
        os.mkdir(todir)          
    else:
        for fname in os.listdir(todir):
            os.remove(os.path.join(todir,fname))
    partnum = 0
    partsum = getPartSum(fromfile,chunksize)
    inputfile = open(fromfile,'rb')#open the fromfile
    while True:
        chunk = inputfile.read(chunksize)
        if not chunk:             #check the chunk is empty
            break
        partnum += 1
        #partnum_hex +=1
        #hexpartnum = repr(partnum)
        #partnum_hex = '00 00'
        filename = os.path.join(todir,('part%04d'%partnum))
        fileobj = open(filename,'wb')#make partfile
        #fileobj.write(hex(partnum))
        fileobj.write(bytes.fromhex('%04x'%partnum))
        fileobj.write(bytes.fromhex('%04x'%partsum))
        fileobj.write(chunk)         #write data into partfile
        fileobj.close()
    return partnum
if __name__=='__main__':
        fromfile  = input('File to be split?')
        todir     = input('Directory to store part files?')
        chunksize = int(input('Chunksize to be split?'))
        absfrom,absto = map(os.path.abspath,[fromfile,todir])
        print('Splitting',absfrom,'to',absto,'by',chunksize)
        try:
            parts = split(fromfile,todir,chunksize)
        except:
            print('Error during split:')
            print(sys.exc_info()[0],sys.exc_info()[1])
        else:
            print('split finished:',parts,'parts are in',absto)
