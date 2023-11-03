#print("1706")
myFile = open("advent1b.txt")

myData = myFile.read().splitlines()
x=1

count = 0
#loop
for i in range(len(myData)-3):

  #complacated thing that checks if 3 num is bigger
  sum1 = int(myData[i])+int(myData[i+1])+int(myData[i+2])
  sum2 = int(myData[i+1])+int(myData[i+2])+int(myData[i+3])
  if int(sum1) < int(sum2):
    count = count + 1
#if int(myData[i+1+2]) < int(myData[i+2+3]):
print(count)

