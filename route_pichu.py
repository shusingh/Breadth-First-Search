#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : Shubham Kumar Singh - shusingh
#
# Based on skeleton code provided in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
        moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))
        # Return only moves that are within the house_map and legal (i.e. go through open space ".")
        return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)
def search(house_map):
        # Find pichu start position
        pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        
        # added an empty string here in fringe to keep track of path we are taking
        fringe=[(pichu_loc,0,'')]
        
        # creating a set to keep track of visited nodes
        visited = set()

        # function to get the next step we are taking
        def find_path(prev, curr):
                if prev[0] - curr[0] == 1:
                        return 'U'
                elif prev[0] - curr[0] == -1:
                        return 'D'
                elif prev[1] - curr[1] == 1:
                        return 'L'
                elif prev[1] - curr[1] == -1:
                        return 'R'

        # instead of DFS which was previously being used
        # we would use BFS 
        while fringe:
                # As we are using BFS, we pop the first element from fringe instead of last
                (curr_move, curr_dist, path)=fringe.pop(0)
                # adding the current node to visited (so that we don't visit it again)
                visited.add(curr_move)

                for move in moves(house_map, *curr_move):
                        # condition to check if we have reached the goal (destination)
                        if house_map[move[0]][move[1]]=="@":
                                # we add this move too, which leads to destination
                                fringe.append((move, curr_dist + 1, path+find_path(curr_move, move)))
                                return (fringe[-1][1], fringe[-1][2])  # return the answer
                        
                        # we only append new moves if we haven't visited them already
                        if move not in visited:
                                fringe.append((move, curr_dist + 1, path+find_path(curr_move, move)))
        
        # if we didn't find the answer then return -1
        return -1 


# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        solution = search(house_map)

        # here we can get two types of values
        # the first one could be answer which contains two differnt values
        # and second if we don't get answer then we get -1
        if solution == -1:
                print("Here's the solution I found:")
                print(solution)
        else:
                print("Here's the solution I found:")
                print(str(solution[0]) + " " + solution[1])

