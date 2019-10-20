import random

############ Variables ##############


npart = 500

side = 51  #Should be an odd number

perc = 0

maxsteps = 10000

steps = [(1,0),(-1,0),(0,1),(0,-1)]

####################################


############ Take in user input from std in ###############

density = input("Enter a density value between 0.0 and 1.0: ")

if (float(density) <= 0.0) or (float(density) >= 1.0):
    print("Invalid value! Exiting...")
    raise SystemExit

density = float(density)

###########################################3###############

########### Initialize grid ##############
grid=[[0 for x in range(side)] for y in range(side)]
print(grid)
##########################################


####### Modify Grid #########
i = 0
j = 0
while i < len(grid):
    while j < len(grid[i]):
        grid[i][j] = random.choices([0,1],[1.0-density,density], k=1)[0]
        j += 1
    i += 1
    j = 0
print(grid)
###########################

#############Core of simulation##############
for ipart in range(npart):

    # Start particle at center of grid
    x,y = side//2,side//2

    # Move particle
    for step in range(maxsteps):

        # Choose a random "step"
        sx,sy = random.choice(steps)

        # Check if the random step chosen is blocked
        # If its blocked choose a different step (hence the continue statement)
        if grid[x+sx][y+sy] == 1:
             continue

        # If the path is not blocked update the values of x and y
        else:
             x += sx
             y += sy
	
        # Checks to see if we have reached an edge
        if (x==0 or y==0 or x==side-1 or y==side-1):
            print('X value: {}'.format(x))
            print('Y value: {}'.format(y))
            perc += 1
            print("Perc: {}".format(perc))
            print("\n")
            break

# Solution
solution=float(perc)/float(npart)

print("Final perc {}".format(perc))
print("Solution: {}".format(solution))