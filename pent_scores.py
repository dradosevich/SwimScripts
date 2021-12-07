# Danny Radosevich
# score the WHSAA Pentathlon Swim Meets

import collections 

swim_scores =[48, 42, 38, 36, 34, 32, 30, 28, 26, 24, 23, 22, 21, 20, 
                19, 18, 17, 16, 15, 13, 12, 11, 10, 8, 6, 5, 4, 3, 2, 1]
dive_scores = [14, 11, 10, 9, 8, 6, 4, 3, 2, 1]
team_scores = {} 
team_scorers = {} 
print("File to score for swimming")
#file = input()#get file from command line
file = "pent_results.htm"
file = open(file) #open file
file = file.read() #read the file 
file = file.split("\n") #get a list of all the lines
for line in file:
    line = line.lstrip()
    while "  " in line:
        line = line.replace("  "," ")
    if line.split(" ")[0].isnumeric():
        #finally where we need to be 
        line = line.replace(", ",",")
        line = line.split(" ")
        #print(line)
        if int(line[0])<=30:
            #one of the scoring swimmers 
            #print(line)
            if len(line)<9:
                #too small 
                pass
            else:
                team = line[len(line)-7]
                #print(team)
                if team in team_scores: #team already in deque
                    team_scores[team] = team_scores[team]+swim_scores[int(line[0])-1] #update their score
                    team_scorers[team].append([line[1],swim_scores[int(line[0])-1]]) #add the scoring swimmer
                else:
                    team_scores[team] = swim_scores[int(line[0])-1] #add the swimmer's score
                    team_scorers[team] = [[line[1],swim_scores[int(line[0])-1] ]]#put the swimmer and their score in
        else:
            break 
'''
print("Dive results file")
file = input()
'''
file = "dive_pent.htm"
file = open(file)
file = file.read()
file = file.split("\n")
for line in file:
    line = line.lstrip()
    line = line.rstrip()
    while "  " in line:
        line = line.replace("  "," ")
    if line.split(" ")[0].isnumeric():
        #finally where we need to be 
        line = line.replace(", ",",")
        line = line.split(" ")
        #print(line)
        if int(line[0])<=10:
            #one of the scoring swimmers 
            #print(line)
            if len(line)<5:
                #too small 
                pass
            else:
                team = line[len(line)-3]
                #print(line)
                if team in team_scores: #team already in deque
                    team_scores[team] = team_scores[team]+dive_scores[int(line[0])-1] #update their score
                    team_scorers[team].append([line[1],dive_scores[int(line[0])-1]]) #add the scoring swimmer
                else:
                    team_scores[team] = dive_scores[int(line[0])-1] #add the swimmer's score
                    team_scorers[team] = [[line[1],dive_scores[int(line[0])-1] ]]#put the swimmer and their score in
        else:
            break 

out_file = open("pent_scores.txt","w")
#team_scores = collections.OrderedDict(team_scores)
print(team_scores)
#print(team_scorers)

for key in sorted(team_scores, key=team_scores.get,reverse=True):
    out_file.write("---------------------------------------------\n")
    out_file.write(str(key).replace("-WY","")+"\t\t"+ str(team_scores[key])+" \n")
    for swimmer in team_scorers[key]:
        swmr = swimmer[0].split(",")
        swimmer = str(swimmer[1])+"\t"+swmr[1]+" "+swmr[0]
        out_file.write("\t\t"+str(swimmer)+"\n")#        



