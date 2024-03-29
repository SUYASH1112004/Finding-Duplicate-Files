#Creating Automation Script which will check duplicate files and returns it ...

from sys import *
import os
#import time
import hashlib

def hashfile(path,blocksize=1024):          #Creating function for calculating checksum ...
    fd=open(path,'rb')                      #To Calculate checksum we must open File And read content of it..
    hasher=hashlib.md5()
    buf=fd.read(blocksize)
    
    while(len(buf)>0):
        hasher.update(buf)
        buf=fd.read(blocksize)

    fd.close()

    return hasher.hexdigest()

def Finddupli(path):
    flag=os.path.isabs(path)
    if(flag==False):
        path=os.path.abspath(path)
    exist=os.path.isabs(path)
    dups={}
    if exist:
        for direcName,subdir,filename in os.walk(path):
            print("current folder is :",direcName)
            for fname in filename:
                path=os.path.join(direcName,fname)
                filehash=hashfile(path)
                if filehash in dups:
                    dups[filehash].append(path)
                else:
                    dups[filehash]=[path]
        return dups
    
    else:
        print("Invalid path")

def printdupli(dict1):
    results=list(filter(lambda x: len(x)>1,dict1.values()))

    if(len(results)>0):
        print("Duplictes Found ...")
    
        print("The Following Files Are Identical..")

        icnt=0
        for result in results:
            for subresult in result:
                icnt+=1
                if(icnt>=2):
                    print('/t/t%s'%subresult)
                    

    else:
        print("No Duplicate Files Found ...")


def main():
    print("...Automation Script ...")
    print("For checking the Duplicate Files are present or not..")
    if(len(argv)!=2):
        print("Error : Invalid No Of Arguments ..")

    if(argv[1]=="h" or argv[1]=="H"):
        print("This Script Is used To Find Duplicate Files ...")
    
    if(argv[1]=="u" or argv[1]=="U"):
        print("Script Used For Finding Duplicate Eliments ..\nAnd Will Display Names Of Duplicate Files ..")

    else:
        try:
            dir={}
            dir=Finddupli(argv[1])
            printdupli(dir)
        except ValueError:              #Value error occurs when we put invalid iterals ...
            print("Invalid Data Type Of Input !!!")

if __name__=="__main_":
    main()
        



