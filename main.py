#print("1676")
myFile = open("advent1a.txt")
myData = myFile.read().splitlines()
count = 0
#stupid fence post error 
for i in range(len(myData)-1):
#checks if num is bigger
  if int(myData[i]) < int(myData[i+1]):
   
    count = count + 1
print(count)