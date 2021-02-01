# Danny Radosevich
# Scores generator



readFrom = open("DualScores.htm") #open file
readFrom = readFrom.read() #read in file
readFrom = readFrom.split("\n") #split by line
writeOut = open("scores.txt","w")
toPrint = "" #what we will print out
lineNum = 1
readFrom = readFrom[10:-1]
readFrom = readFrom[:-4]
for line in readFrom:
    print(line)
    line = line.replace("\n","")
    line = line.lstrip()
    line = line.rstrip()
    line = "[" + line + "] "
    toPrint = toPrint+line
writeOut.write(toPrint)
#print(readFrom)#output scores as line
