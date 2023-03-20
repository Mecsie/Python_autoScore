import subprocess
from pathlib import Path
from function import *
import natsort # pip install natsort -> if not used: remove natsort.natsorted
import re
import openpyxl

questionType = "numeric"
# questionType = "graph"
targetPythonFile = r'[pP]4.py*'

# targetPythonFile = r"../hw2/q2.py"
allHwsDirectory = Path("../studentHws")
logFilePath = Path("./log/logForScoredFiles.txt")

logForFailPath = Path("./log/scoredFailPath.txt")
logForExcelFoundPath = Path("./log/pythonFileScoredOnExcel.txt")
logForExcelNotFoundPath = Path("./log/pythonFileScoredNotInExcel.txt")
logForNotFoundFilePath = Path("./log/pythonFileNotFound(unScored).txt")

initLogFile(logFilePath)
initFailLogFile(logForFailPath)
initLogForExcelFile(logForExcelFoundPath)
initLogForExcelFile(logForExcelNotFoundPath)
initLogForExcelFile(logForNotFoundFilePath)

# targetPythonFile = input("input target python file name (ex: p1.py -> [pP]1.py) ")


# specify the directory path where you want to search
# allHwsDirectory = Path('/path/to/directory')

# use the glob() method to search for directories recursively
directories = allHwsDirectory.glob('*')
# print(len(list(directories)))
# exit()
# print(directories)
# loop through the directories and search for files with the specified pattern
notFoundCount = 0
count = 0
for dir in directories:

    print(dir)
    # print(type(dir))
    targetPythonFilesPath = dir.rglob(targetPythonFile)
    
    # print(list(targetPythonFilesPath))
    dirFoundPythonFile = False
    for pythonFilePath in targetPythonFilesPath:
        # print(pythonFilePath)
        if pythonFilePath.is_file() and pythonFilePath.suffix  in {'.py', '.py.py' ,'.py.txt'}:
            # print("target python",pythonFilePath)
            studentID=pythonFilePath.parent.name.split("_")[0]
            # print(studentID)
            if questionType == "graph":
                score,logMsgFromFile = scoreOnePythonFile_graph(pythonFilePath)
            elif questionType == "numeric":
                score,logMsgFromFile = scoreOnePythonFile_numeric(pythonFilePath)
            # print("-----------------------------------")
            # print(score)
            # print(logMsg)
            pythonFilePathAndScore = pythonFilePath.parent.parent.name + "/"+pythonFilePath.parent.name+"/"+pythonFilePath.name+f": {score}  " 
            logMsg = "----------------------------------------------------------------------------------------------------\n"
            logMsg += f"                {count+1}    {pythonFilePathAndScore}                         \n"
            logMsg += "----------------------------------------------------------------------------------------------------\n"
            logMsg += f"file dir path: \n{Path(pythonFilePath).parent.absolute()}\n\n"
            logMsg += logMsgFromFile
            writeLogFile(logFilePath,logMsg)
            if score == "fail":
                writeFailLogFile(logForFailPath,pythonFilePathAndScore+"\n")

            found = writeToExcel(studentID,score)
            if found == False and studentID != None:
                writeLogForExcelFile(logForExcelNotFoundPath,pythonFilePathAndScore)
            else:
                writeLogForExcelFile(logForExcelFoundPath,pythonFilePathAndScore)
            count += 1
            dirFoundPythonFile = True
    if not dirFoundPythonFile:
        notFoundCount += 1
        writeLogForNotFoundFile(logForNotFoundFilePath,str(dir.absolute())+"\n")
        

print(f"total processed {count} files")
print(f"python file not found {notFoundCount}")
print(f"iterate through {count+notFoundCount} student directories")
# scoreOnePythonFile(targetPythonFile)


    


    
    

# inputString = inputLines[2]+inputLines[3]
# print("input len",len(inputLines))

# for i in range(0,len(inputLines),inputNum):
#     inputString = ""
#     for j in range(i,i+inputNum):
#         inputString += inputLines[j]
#     executeHwFile(targetPythonFile,inputString)
# print(repr(lines))

