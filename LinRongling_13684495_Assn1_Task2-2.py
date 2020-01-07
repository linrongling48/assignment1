import random
import time

lowerLimit = -13800
upperLimit = 36600
numOfValues = 8000
noDuplicates = False

def saveToFile(resString, fileName):
   file = open(fileName, mode = "w", encoding = "utf-8")
   file.write(resString)
   print("Successful")
   file.close

def rNGenerator(lowerLimit, upperLimit, numOfValues, noDuplicates):
   if noDuplicates == False:
      resLis = []
      for i in range(numOfValues):
         res = random.randint(lowerLimit, upperLimit)
         resLis.append(res)
      return resLis
   else:
      resLis = []
      while len(resLis) < numOfValues:
         res = random.randint(lowerLimit, upperLimit)
         if res in resLis:
            pass
         else:
            resLis.append(res)
      return resLis

def quickSort(resList):
    if len(resList)<2:
        return resList
    mid = resList.pop(0)
    left = []
    right = []
    for i in resList:
        if i > mid:
            right.append(i)
        else:
            left.append(i)
    return quickSort(left) + [mid] + quickSort(right)

resListUnsort = rNGenerator(lowerLimit,upperLimit,numOfValues,noDuplicates)
startTime = time.time()
resLisSorted = quickSort(resListUnsort)
saveToFile(str(resLisSorted),"Desktop/RandomNum_Sorted.txt")
print("lowerLimit: "+str(lowerLimit)+"\nupperLimit: "+str(upperLimit)+"\nnumOfValues: "+str(numOfValues)+"\nnoDuplicates:",noDuplicates,"\nThe algorithm spent {:.3f}s.".format(time.time()-startTime))