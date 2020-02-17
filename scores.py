# Danny Radosevich
# Scores generator



readFrom = open("scores.htm") #open file
readFrom = readFrom.read() #read in file
readFrom = readFrom.split("\n") #split by line
toPrint = "" #what we will print out
lineNum = 1
for line in readFrom: #for every line in file
    while '  'in line:
        line = line.replace('  ',' ') #tidy up the lines to singel space
    line.replace('\t','') #remove tab characters
    line = line.lstrip() #remove leading spaces
    line = line.rstrip() #remove ending spaces
    line = line.split(' ') #make a list by splitting line on the spaces
    #print(line)
    if line[0].isdigit(): #on a line with a team
        myLen = len(line) #get the length
        toPrint+="["+line[myLen-2][:3]+" "+line[myLen-1]+"] " #get the team abv and scores

print(toPrint)#output scores as line
