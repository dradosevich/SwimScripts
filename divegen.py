#Danny Radosevich
#Dive XML Generator
import subprocess as sp
import os
import re

#toOpen = input("Enter the file to read from:\n") #prompt user for input
readFrom = open("divers.htm") #open file
readFrom = readFrom.read() #read in
readFrom = readFrom.split("\n") #get each individual line
file_name = input("Enter name for the file: ")
lineNum = 1 #control variable
writeOut = open(file_name+".xml","w") #will be used as the write out file
writeOut.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")#header
writeOut.write("<divingevent>\n") #denote this is a diving event
writeOut.write("<eventtitle>"+file_name+"</eventtitle>\n") #use file name to make title
for line in readFrom: #go through every line
    
    line = line.lstrip()
    if len(line) > 0 and line[0].isdigit(): #now to do the divers, if at rigth line
        
        #print(line)
        #re.sub('\s+', ' ',line).strip()
        #line.replace("\t"," ")
        while '  'in line:
            line = line.replace('  ',' ') #get down to single spacing

        #print(line) #print out line for verification, not needed
        line = line.replace(",","")
        line = line.split(" ") #split out the line to individual words
        
        if(len(line)>=4): #bounds check
            line.remove("")
            print(line)
            
            team = line[-2].upper()
            team = team[:3]
            newDiver = "\t<diver>\n" #xml write out
            newDiver+= "\t\t<lastname>"+line[1]+"</lastname>\n" #write out last name
            newDiver+= "\t\t<firstname>"+line[2]+"</firstname>\n" #writeout first name
            newDiver+="\t\t<team>"+team+"</team>\n" #write out team
            newDiver+="\t</diver>\n" #end the diver
            writeOut.write(newDiver) #write out to the file
    lineNum+=1 #increment control
writeOut.write("</divingevent>") #end the diving event
#readFrom.close()
writeOut.close() #close the file
