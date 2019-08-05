import cv2
import numpy as np
import matplotlib.pyplot as plt

## (1) read
def partition(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)[:,50:]

    ## (2) threshold
    threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)[1]

    ## (3) minAreaRect on the nozeros


    ## (5) find and draw the upper and lower boundary of each lines
    hist = cv2.reduce(threshed,1, cv2.REDUCE_MAX).reshape(-1)


    th = 0
    H,W = img.shape[:2]
    uppers = [y for y in range(H-1) if hist[y]<=th and hist[y+1]>th]
    lowers = [y+1 for y in range(H-1) if hist[y]>th and hist[y+1]<=th]
    blankscenters=[(i+j)/2 for i,j in zip(uppers[1:],lowers[:-2])]
    blankspans=[(i-j)/2 for i,j in zip(uppers[1:],lowers[:-2])]
    delimiters=[]
    for i in range(len(blankspans)):
        if blankspans[i]>10:
            delimiters+=[int(blankscenters[i])]

    threshed = cv2.cvtColor(threshed, cv2.COLOR_GRAY2BGR)
    for y in uppers:
        cv2.line(threshed, (0,y), (W, y), (255,0,0), 1)

    for y in lowers:
        cv2.line(threshed, (0,y), (W, y), (0,255,0), 1)

    #cv2.imwrite("result.png", threshed)
    #plt.figure(figsize=(20,60))
    delimiters=[0]+delimiters+[H]
    #for i in range(len(delimiters)-1):
    #    plt.subplot(len(delimiters)-1,1,i+1)
    #    plt.imshow(threshed[delimiters[i]:delimiters[i+1],:])
    delimiters=[int(i/25*3) for i in delimiters]
    return delimiters

folder="/home/maxwell/Desktop/Regina Phalange/circumstance/movy/Persian/Tajiki/Farhangi-tafsirii/bycolumns/burst/"
commandstrings=[]
for i in range(1,1481):
    numstring=str(i)
    name="pg_"+"0"*(4-len(numstring))+numstring
    limits=partition(folder+name+".png")
    if(i%10==0):
        print(i)
    for j in range(len(limits)-1):
        h=limits[-1]
        commandstrings+=["pdfcrop --margins '0 -{} 0 -{}' {}.pdf j{}-{}.pdf".format(limits[j], h-limits[j+1],name,name,"0"*(2-len(str(j)))+str(j))]
        #print(commandstrings[-1])
with open(folder+"commands.bash","w") as fout:
    fout.write("\n".join(commandstrings))
