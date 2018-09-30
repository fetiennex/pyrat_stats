#!/usr/bin/python

import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mud', type=str, metavar = "mud", help='Plot with constant mud at set value', default="")
parser.add_argument('--size', type=str, metavar = "size", help='Plot with constant size at set value', default="")
args = parser.parse_args()

#  algorithm;mud;map_width;map_height;map_size;turns
# [str;str;str;str;str]
# [str;str;str;str;str]
# [str;str;str;str;str]
# ...
fn = "stats.csv"
file = open(fn,"r")
lines = file.readlines()[1:]
la = []
for line in lines:
    l = line.split(";")
    la.append(l[0])
la = sorted(set(la))
file.close()

def plotmudcst(fn, algo, mud):
    f = open(fn, "r")
    lines = f.readlines()[1:]
    j = 5
    i = 4
    a = []
    b = []
    for line in lines:
        l = line.split(";")
        if l[0] != algo :
            continue
        if l[1] != mud:
            continue
        a.append(float(l[i]))
        b.append(float(l[j]))
    f.close()
    plt.plot(a,b,'o', label = algo)
    print("a="+str(a)+ "\n")
    print("b="+str(b)+ "\n")
    
def plotsizecst(fn, algo, size):
    f = open(fn, "r")
    lines = f.readlines()[1:]
    j = 5
    i = 1
    
    a = []
    b = []
    for line in lines:
        l = line.split(";")
        if l[0] != algo :
            continue
        if l[4] != size:
            continue
        a.append(float(l[i]))
        b.append(float(l[j]))
    f.close()
    plt.plot(a,b,'o', label = algo)
    print("a="+str(a)+ "\n")
    print("b="+str(b)+ "\n")
    
for a in la:
    print("algo =" +a +"\n")    
    if args.mud != "":
        plt.title("mud =" +str(args.mud))
        plotmudcst(fn,a,args.mud)
        plt.xlabel('map_size')
    else :
        if args.size == "":
            raise Exception("You must pass an argument !")
        plt.title("size =" +str(args.size))
        plotsizecst(fn,a,args.size)
        plt.xlabel('mud')
        
plt.ylabel("turns")
plt.legend()    
plt.show()
