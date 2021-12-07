#Danny Radosevich
#Dive XML Generator
import subprocess as sp
import os
import re

toOpen = input("Enter the file to read from:\n") #prompt user for input
readFrom = open(toOpen) #open file
readFrom = readFrom.read() #read in
readFrom = readFrom.split("\n") #get each individual line
lineNum = 1 #control variable
writeOut = 0 #will be used as the write out file
for line in readFrom: #go through every line
    #print(line+" "+str(lineNum))
    if lineNum == 6: #this is the line with the meet title
        newFile = line.replace(' ','')+".xml" #remove spaces, add xml extension, to make file name
        newFile = newFile.replace('/','-') #clean up bad characters for the date
        #os.system("touch "+newFile)
        newFile = str(newFile) #not needed at all
        writeOut = open(newFile,"w")#open file to write out
        writeOut.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")#header
        writeOut.write("<divingevent>\n") #denote this is a diving event
        writeOut.write("<eventtitle>"+newFile[:-4]+"</eventtitle>\n") #use file name to make title
    elif lineNum > 13 and "</" not in line: #now to do the divers, if at rigth line
        #print(line)
        #re.sub('\s+', ' ',line).strip()
        #line.replace("\t"," ")
        if "," in line:
            line = line.replace(",","")
        if "FR" in line:
            line = line.replace("FR","")
        if "SO" in line:
            line = line.replace("SO","")
        if "JR" in line:
            line = line.replace("JR","")
        if "SR" in line:
            line = line.replace("SR","")
        for char in line: #for every character in the line
            if char.isdigit():
                line = line.replace(char, '') #if it is a number remove it
        line = line.replace('.','') #remove all periods
        while '  'in line:
            line = line.replace('  ',' ') #get down to single spacing

        print(line) #print out line for verification, not needed
        line = line.split(" ") #split out the line to individual words
        if(len(line)>4): #bounds check
            newDiver = "\t<diver>\n" #xml write out
            newDiver+= "\t\t<lastname>"+line[2]+"</lastname>\n" #write out last name
            newDiver+= "\t\t<firstname>"+line[1]+"</firstname>\n" #writeout first name
            newDiver+="\t\t<team>"+line[3][:3]+"</team>\n" #write out team
            newDiver+="\t</diver>\n" #end the diver
            writeOut.write(newDiver) #write out to the file
    lineNum+=1 #increment control
writeOut.write("</divingevent>") #end the diving event
#readFrom.close()
writeOut.close() #close the file
