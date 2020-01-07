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
      saveToFile(str(resLis),"Desktop/RandomNum_non-unique.txt")
      print("lowerLimit: "+str(lowerLimit)+"\nupperLimit: "+str(upperLimit)+"\nnumOfValues: "+str(numOfValues)+"\nnoDuplicates:",noDuplicates,"\nThe algorithm spent {:.3f}s.".format(time.time()-startTime))
   else: 
      resLis = []
      while len(resLis) < numOfValues:
         res = random.randint(lowerLimit, upperLimit)
         if res in resLis:
            pass
         else:
            resLis.append(res)
      saveToFile(str(resLis),"Desktop/RandomNum_unique.txt")
      print("lowerLimit: "+str(lowerLimit)+"\nupperLimit: "+str(upperLimit)+"\nnumOfValues: "+str(numOfValues)+"\nnoDuplicates:",noDuplicates,"\nThe algorithm spent {:.3f}s.".format(time.time()-startTime))

startTime = time.time()
rNGenerator(lowerLimit, upperLimit, numOfValues, noDuplicates)