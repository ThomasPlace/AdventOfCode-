#print("1971232560")
x=0
# Read in the data
vpos=0
hzpos=0
aim=0
myFile = open("advent2.txt")
#reading file
myData = myFile.read().splitlines()
#algrithem loop
for i in range(len(myData)):
  myFile=myData[i]
  if (myFile == "forward 1"):
      hzpos=hzpos+1
      vpos+=1*aim
  elif (myFile == "forward 2"):
      hzpos=hzpos+2
      vpos+=2*aim
  elif (myFile == "forward 3"):
      hzpos=hzpos+3
      vpos+=3*aim
  elif (myFile == "forward 4"):
      hzpos=hzpos+4
      vpos+=4*aim
  elif (myFile == "forward 5"):
      hzpos=hzpos+5
      vpos+=5*aim
  elif (myFile == "forward 6"):
      hzpos=hzpos+6
      vpos+=6*aim
  elif (myFile == "forward 7"):
      hzpos=hzpos+7
      vpos+=7*aim
  elif (myFile == "forward 8"):
      hzpos=hzpos+8 
      vpos+=8*aim
  elif (myFile == "forward 9"):
      hzpos=hzpos+9
      vpos+=9*aim
  elif (myFile == "up 1"):
      aim=aim-1
  elif (myFile == "up 2"):
      aim=aim-2
  elif (myFile == "up 3"):
      aim=aim-3
  elif (myFile == "up 4"):  
      aim=aim-4
  elif (myFile == "up 5"):
      aim=aim-5
  elif (myFile == "up 6"):  
      aim=aim-6
  elif (myFile == "up 7"):  
      aim=aim-7
  elif (myFile == "up 8"):  
      aim=aim-8
  elif (myFile == "up 9"): 
      aim=aim-9
  elif (myFile == "down 1"): 
      aim=aim+1
  elif (myFile == "down 2"): 
      aim=aim+2
  elif (myFile == "down 3"): 
      aim=aim+3
  elif (myFile == "down 4"): 
      aim=aim+4
  elif (myFile == "down 5"): 
      aim=aim+5
  elif (myFile == "down 6"): 
      aim=aim+6
  elif (myFile == "down 7"): 
      aim=aim+7
  elif (myFile == "down 8"): 
      aim=aim+8
  elif (myFile == "down 9"): 
    aim=aim+9  
cat=vpos*hzpos
print(cat)
#adinging everyting up