NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def move(n, source, auxiliary, target):
    if n <= 0:
        return
        # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
        
        # move the nth disk from source to target
    target.append(source.pop())
        
        # display our progress
    print(A, B, C, '\n')
        
        # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1,  auxiliary, source, target)
              
# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)

#The Hanoi Puzzle, also known as the Tower of Hanoi, is a classic mathematical puzzle that involves three rods and a number of disks of different sizes. 
#The objective is to move all the disks from the source rod to the target rod, following these rules:

    #Only one disk can be moved at a time.
    #A disk can only be placed on an empty rod or on top of a larger disk.
    #All disks must maintain their original stacked order (smallest at the top).

#Recursion is a programming technique where a function calls itself to solve smaller instances of a problem until it reaches a base case (stopping condition).
#It is often used in problems involving repetitive or hierarchical structures, such as the Hanoi Puzzle.

#For example: In the Tower of Hanoi:
 #Move n-1 disks to an auxiliary rod.
 #Move the largest disk to the target rod.
 #Move n-1 disks from the auxiliary rod to the target rod.
