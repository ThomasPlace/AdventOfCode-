#print("1882980")
x=0
# Read in the data
vpos=0
hzpos=0

myFile = open("advent2.txt")

myData = myFile.read().splitlines()
#algrithem 
for i in range(len(myData)):
  myFile=myData[i]
  if (myFile == "forward 1"):
      hzpos=hzpos+1
  elif (myFile == "forward 2"):
      hzpos=hzpos+2
  elif (myFile == "forward 3"):
      hzpos=hzpos+3
  elif (myFile == "forward 4"):
      hzpos=hzpos+4
  elif (myFile == "forward 5"):
      hzpos=hzpos+5
  elif (myFile == "forward 6"):
      hzpos=hzpos+6
  elif (myFile == "forward 7"):
      hzpos=hzpos+7
  elif (myFile == "forward 8"):
      hzpos=hzpos+8 
  elif (myFile == "forward 9"):
      hzpos=hzpos+9 
  elif (myFile == "up 1"):
      vpos=vpos-1
  elif (myFile == "up 2"):
      vpos=vpos-2
  elif (myFile == "up 3"):
      vpos=vpos-3
  elif (myFile == "up 4"):  
      vpos=vpos-4
  elif (myFile == "up 5"):
      vpos=vpos-5
  elif (myFile == "up 6"):  
      vpos=vpos-6
  elif (myFile == "up 7"):  
      vpos=vpos-7
  elif (myFile == "up 8"):  
      vpos=vpos-8
  elif (myFile == "up 9"): 
      vpos=vpos-9
  elif (myFile == "down 1"): 
      vpos=vpos+1
  elif (myFile == "down 2"): 
      vpos=vpos+2
  elif (myFile == "down 3"): 
      vpos=vpos+3
  elif (myFile == "down 4"): 
      vpos=vpos+4
  elif (myFile == "down 5"): 
      vpos=vpos+5
  elif (myFile == "down 6"): 
      vpos=vpos+6
  elif (myFile == "down 7"): 
      vpos=vpos+7
  elif (myFile == "down 8"): 
      vpos=vpos+8
  elif (myFile == "down 9"): 
    vpos=vpos+9

cat=vpos*hzpos
print(cat)