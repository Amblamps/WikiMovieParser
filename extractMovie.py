import re
import sys
import time
from itertools import islice

def writeToFiles (fileName, data, encoding, mode):
    if encoding:
        output = open(fileName, mode, encoding = encoding)
    else:
        output = open(fileName, mode)
    output.write(data)
    output.close()
    return;

fileName = "wikipedia4202017.xml"
f = open(fileName, "r", encoding="utf8");
filePrefix = "movies\\movie"

detFileName = "extractionLog.txt"
timeDet = "Extracted from " + fileName + " at " + time.strftime("%H:%M:%S") + " on " + time.strftime("%m/%d/%Y") + "\n"
writeToFiles(detFileName, timeDet, "", "a")  

data = ''
dataFound = ''
filmRE = "({{Infobox\sfilm)" #Find a film Infobox from wiki article
dataRE = "(.*)(?=''''')" #Get all text preceding '''' string
readNLines = 60 #Extracted 109657 movie articles when reading 60 lines, could have missed some
count = 0;
for line in f:
    filmFound = re.search( filmRE, line)
    if filmFound:
        data = ''.join(islice(f,readNLines))
        dataFound = re.findall(dataRE, data, re.DOTALL)
        if dataFound:
                fileOutName = filePrefix + str(count) +".txt"
                writeToFiles(fileOutName, dataFound[0], "utf8", "w")
                count = count + 1
timeDet = "Extraction finished on " + time.strftime("%H:%M:%S") + " on " + time.strftime("%m/%d/%Y")
writeToFiles(detFileName, timeDet, "", "a")
f.close()
print("ALL DONE!!!!!!!!")

