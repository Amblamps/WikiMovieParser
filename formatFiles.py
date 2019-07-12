import os
import re
import fnmatch
import csv

pattern = "*.txt"
movieDir = "moviesFiles"
fileNames = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(movieDir)
    for f in fnmatch.filter(files, pattern)]

nameReg = "(?<=name)(\s*=\s*)(.*)"
runtimeReg = "(?<=runtime)(\s*=\s*\d*\s*minutes)"
budgetReg = "(?<=budget)(\s*=\s\$*\d*,?\.?-?–?\d*[,\.]?\d*[,\.]?\s?)([tT]housand|[mM]illion|[bB]illion)?"
grossReg = "(?<=gross)(\s*=\s\$*\d*,?\.?-?–?\d*[,\.]?\d*[,\.]?\s?)([tT]housand|[mM]illion|[bB]illion)?"
countryReg = "United States"
count = 0
output = open("movieNames.csv", "w", newline='', encoding = "utf8")
wr = csv.writer(output, dialect = "excel")
for file in fileNames:
    with open(file, "r", encoding= "utf8") as f:
        fread = f.read()
        matchName = re.search(nameReg, fread)
        matchRun = re.search(runtimeReg, fread)
        matchBud = re.search(budgetReg, fread)
        matchGros = re.search(grossReg, fread)
        matchCountry = re.search(countryReg, fread)
	# Found movie
        if(matchName and matchRun and matchBud and matchGros and matchCountry):
            name = matchName[0].strip()[1:].strip()
            runtime =  matchRun[0].strip()[1:].strip()
            budget = matchBud[0].strip()[1:].strip()
            gross = matchGros[0].strip()[1:].strip()
            if(name and runtime and budget and gross):
                wr.writerow([name, runtime, budget, gross, count])
                count = count + 1
output.close()
print(count)
    

    
