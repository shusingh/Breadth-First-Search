# a0

### Part - 1: Route Pichu

#### The problem:
In this first task, we were provided with an initial file named `route_pichu.py` which already contains a skeleton code to work with. The code that was already provided was very helpful in understanding the problem and getting a good head start. The code had comments associated almost everywhere which made it easy to understand the code in a very short amount of time. The provided code had some issues that needed to be fixed and so I completed the task as explained below:

#### My Solution:
Looking at the code, the first thing I noticed was that we were returning a “dummy answer” as output. After running the code for the first time, as mentioned in the problem statement, it went into an infinite loop. 

I realized that we did not have a memory to keep track of the visited nodes so that we do not visit them again and again, which was causing the problem of the infinite loop. For this task, I created a new `set()` and assigned it the name `visited`. This variable would keep track of visited nodes so that we don’t visit them again.

Looking at the problem statement provided, I noticed that we had to return -1 if we didn’t find the path and in case if we successfully found the path then we had to return two variables, (1) The total distance taken to reach the destination and (2) The path taken ( using ‘U’, ‘D’, ‘L’, ‘R’). I noticed that we already had a variable provided in the fringe named curr_dist which was calculating the distance but we did not have any variable for keeping track of the path we are taking from start to end. Hence, I added an empty string in the `fringe` which would keep track of the path the program takes.
I created a new function named `find_path` to know whether we are going up, down, left, or right and then return this value which will be added to the current path that we are traversing.

The code that we were given uses a Depth First Search (DFS) Technique, but instead I decided to use **Breadth First Search (BFS) Technique** because it gives optimal answers unlike DFS. In this problem provided, the valid states are either places marked with ‘.’ or the end goal marked with ‘@’ which are not already in the visited set. Here, the **initial state** is the place on the 2x2 matrix from where we begin our search which is the same as the cell in the matrix which contains ‘p’. The **goal state** is the cell in the matrix marked by ‘@’. We need to find a path from the initial state to the goal state and return -1 if the path does not exist. Here, the **successor function** is that we must move to the connected cells in such that we can only move on the cells marked as ‘.’ or ‘@’ and not on the cells marked as ‘X’ which denotes a wall here. The **cost function** here will be the amount of time taken to travel from the initial state to the goal state which is the same as the number of moves made before we reach our destination ‘@’.

<br/>

### Part - 2 Arrange Pichus:

#### The Problem:
The second problem of “arranging pichus” is similar to that of the n-queens problem discussed in the course module. We are given ‘k’ agents who do not like to see each other. These agents are able to see one another only if they are in the same row, column, or diagonal and there is no wall between them that is marked by ‘X’.

#### My Solution:
First of all, I noticed that the code provided to us did give an output unlike in Part -1. But the problem is the answer it outputs is not correct and the pichus can clearly see one another. After going through the code and understanding the entire code I soon figured out that there is **no function to set the rules for positioning** the pichus in the house. Thus, I created a new function and named it “valid_move()” which takes in three arguments, house_map, row, and col. This function then checks for a particular cell that whether any pichus are visible from there following the rules or not? This function returns True if the cell is safe and it can not see any pichus whether in the same row, column, or diagonally if there is no wall in-between. If it sees any other pichu then it returns False signaling that this cell is not safe for placing the pichu.

I passed this new function as a condition in ‘successors()’ function and hence the new successor function would only return places if they are following all the required rules. Here, the **initial state** is the provided map with just 1 pichu. The **state-space** here is all the possible moves (iterations) on the given map between placing 1 and k pichus. The **goal state** is the state where no pichu can see the other pichu meaning there is no pichu on the same row, column, or diagonal of the current pichu if there is no wall in between them. The **successor function** here returns the possible places that the new pichu can be placed such that no pichu can see each other. The **cost function** here is irrelevant as it does not matter where we place the pichus as long as they can not see one another.