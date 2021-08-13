from PIL import Image
import os
import time

mult=0.0
alc=0

#!!!DO NOT CHANGE!!!
def img(path):
    file = open("log.txt", 'a')

    img1=Image.open(path)
    arr=img1.load()
    
    arr2=img1.copy().load()
    
    pxa=0

    for i in range(0, img1.size[0]):
        for j in range(0, img1.size[1]):
            pxa+=(arr[i,j][0]+arr[i,j][1]+arr[i,j][2])/3

    pxa/=(img1.size[0]*img1.size[1])

    for i in range(1, img1.size[0]):
        for j in range(0, img1.size[1]):
            tmpa0=(arr[i,j][0]+arr[i,j][1]+arr[i,j][2])/3
            tmpa1=(arr[i-1,j][0]+arr[i-1,j][1]+arr[i-1,j][2])/3

            if abs(tmpa0-tmpa1)>pxa*mult:
                if arr[i-1,j]==(255,255,255):
                    arr[i,j]=(0, 255, 0)
                else:
                    arr[i,j]=(255, 0, 0)
            else:
                arr[i,j]=(255, 255, 255)

    for i in range(1, img1.size[0]):
        for j in range(0, img1.size[1]):
            if(arr[i, j]==(0, 255, 0)):
                arr[i,j]=(255, 255, 255)

            tmpf=(arr2[i,j][0]+arr2[i,j][2])/2-arr2[i,j][1];

            if tmpf*-1>=alc:
                arr[i,j]=(255, 255, 0)
       

    #uncomment for debug
    img1.show()
    
    ans1=0
    ln1=0

    ans2=0
    ln2=0

    ans3=0
    ln3=0
    
    for i in range(1, img1.size[0]):
        for j in range(0, img1.size[1]): 
            if arr[i,j]==(255, 0, 0):
                ans1+=(arr2[i,j][0]+arr2[i,j][1]+arr2[i,j][2])/3
                ln1+=1
            elif arr[i,j]==(255, 255, 255):
                ans2+=(arr2[i,j][0]+arr2[i,j][1]+arr2[i,j][2])/3
                ln2+=1
            else:
                ans3+=(arr2[i,j][0]+arr2[i,j][1]+arr2[i,j][2])/3
                ln3+=1

    ans1/=ln1
    ans2/=ln2
    ans3/=ln3

    timest=""

    tmptime=time.localtime()

    timest+=str(tmptime[0])+"."+str(tmptime[1])+"."+str(tmptime[2])+", "+str(tmptime[3])+":"+str(tmptime[4])+":"+str(tmptime[5])

    file.write(path+"\n")
    file.write(timest+"\n")
    file.write("Background:\n")
    file.write(str(ans1) + "/ 255\n")
    file.write(str(ln1)+"\n")
    file.write("Bacterial:\n")
    file.write(str(ans2) + "/ 255\n")
    file.write(str(ln2)+"\n")
    file.write("Algae:\n")
    file.write(str(ans3) + "/ 255\n")
    file.write(str(ln3)+"\n")

    file.close()
#DO NOT CHANGE

#CHANGE ONLY HERE
print("Directory (global):")

#reading directory
st=input()

print("Multiplier (higher for more contrast, lower for less). Strange things are used to happen when it's less than 0.5-0.4:")

#reading multiplier
mult=float(input())

print("Algae green value higher than other in (usually 10-12):")

alc=int(input())

#getting all files in directory. There must be only images
for current_file in os.listdir(st):
    if current_file!="1.py":
        #if you want directory with something else then uncomment following and put Tab before img(current_file)
        #try:
        img(st+current_file)
        #except:
        #   pass
