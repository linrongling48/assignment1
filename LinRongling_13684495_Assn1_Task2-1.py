import random
import time

lowerLimit = -13800
upperLimit = 96800
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

def insertionSort(resList):
   for i in range(1,len(resList)):
      current = resList[i]
      j = i
      while j > 0 and resList[j-1] > current:
         resList[j] = resList[j-1]
         j -= 1
         resList[j] = current
   return resList

resListUnsort = rNGenerator(lowerLimit,upperLimit,numOfValues,noDuplicates)
startTime = time.time()
resLisSorted = insertionSort(resListUnsort)
saveToFile(str(resLisSorted),"Desktop/RandomNum_Sorted.txt")
print("lowerLimit: "+str(lowerLimit)+"\nupperLimit: "+str(upperLimit)+"\nnumOfValues: "+str(numOfValues)+"\nnoDuplicates:",noDuplicates,"\nThe algorithm spent {:.3f}s.".format(time.time()-startTime))