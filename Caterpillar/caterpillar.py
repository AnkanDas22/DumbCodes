import pprint

# [x,y] coordinates to be moved
moveDict = {'N':[-1,0],'S':[1,0],'E':[0,1],'W':[0,-1],
            'NE':[-1,1],'SE':[1,1],'NW':[-1,-1],'SW':[1,-1]}

# Sign to be drawn
signDict = {'N':'|','S':'|','E':'-','W':'-',
            'NE':'/','SE':'\\','NW':'\\','SW':r'/'}

nextPos = [0,0] # Next position - Calculate the next position
currPos = [0,0] # Current position - Store the current position

# Print the map line-by-line
def printMoveMap(moveMap):
    for i in range(len(moveMap)):
        print('|',end="")

        print(''.join(moveMap[i]),end="")
            
        print('|\n',end="")
        
# Main driver code
if __name__=='__main__':
    pp = pprint.PrettyPrinter()
    mapRows, mapColumns = list(map(int,input().split()))

    # Create 2D list for storing the map   
    moveMap = [[' ' for i in range(mapColumns)] for j in range(mapRows)]
    
    while True:
        inp = input()
        if len(inp)!=1:
            steps = int(inp.split()[0]) # Number of steps
            direc = inp.split()[1] # Direction to move
            
            for i in range(steps):

                # Store the calculated next pos. into current pos.
                currPos[0],currPos[1] = nextPos[0],nextPos[1]

                # Place direction symbol in moveMap
                moveMap[currPos[0]][currPos[1]] = str(signDict[direc])

                # Print the map
                printMoveMap(moveMap)

                # Calculate next positions
                nextPos[0] = currPos[0] + moveDict[direc][0]
                nextPos[1] = currPos[1] + moveDict[direc][1]

        # Break out of the while loop if input is 'x'
        
        if inp == 'x':
            break
