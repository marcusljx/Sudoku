#sudoku attempt 1 
import random
# creating all the availnums in each row and column and box
allcubes =[]
onetonine=[1,2,3,4,5,6,7,8,9]
availnuminx=[]
availnuminy=[]
availnuminbox=[]
for repeat in range(9):
    availnuminx.append(onetonine)
    availnuminy.append(onetonine)
    availnuminbox.append(onetonine)

#initializing x,y and box coords for all cubes
for xcoord in range(9):
    for ycoord in range(9):
        box = xcoord//3 + 3*(ycoord//3)
        allcubes.append([xcoord,ycoord,box,0])

#setting up numbers for cubes
for eachcube in allcubes:
    availnums= []
    for number in availnuminx[eachcube[0]]:
        if number in availnuminy[eachcube[1]] and number in availnuminbox[eachcube[2]]:
            availnums.append(number)
    eachcube[3]= random.choice(availnums)
    availnuminx[eachcube[0]].remove(eachcube[3])
    availnuminy[eachcube[1]].remove(eachcube[3])
    availnuminbox[eachcube[2]].remove(eachcube[3])

print(allcubes)
    
            
