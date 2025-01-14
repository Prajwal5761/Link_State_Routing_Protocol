#!/usr/bin/env python

import csv
import sys
import os

######################################################################################################################################
# Information
######################################################################################################################################

# Author :
"""
    Name : Prajwal Thakare - 612203180
    Course : Computer Network Lab
    Project : Simulation of Link-State Routing Protocol
    """

######################################################################################################################################
# Program Starts
######################################################################################################################################

#----------------------------------------------------------------------------#
# Functions Implementation
#----------------------------------------------------------------------------#

# Initialization of all the variables.

router_matrix = []
matrix_set = 0
nodes = []
distances = {}
unvisited = {}
previous = {}
visited = {}
interface = {}
path = []
start = 0
end = 0

# Function to print the choices when the program starts.

def print_choices():

    print("######################################################")
    print("\nLink State Routing Simulator\n")
    print("(1) Input Network Topology File")
    print("(2) Build a Connection Table")
    print("(3) Shortest Path to Destination Router")
    print("(4) Exit")
    print("\n######################################################\n")


# Function to check if the entered command is valid or not - i.e. :
# 1: Should be a digit.
# 2: Should be from the range of given choices.

def check_choices(command):
    
    if not command.isdigit():
        print("Please enter a number as command from given choices..")
        return -1
    else:
        command = int(command)
        
        if command > 4 or command < 1:
            print("Please enter a valid command from given choices..")
            return -1
        else:
            return command


# Function to process the given input file.

def process_file(fname):
    
    global matrix_set
    global router_matrix
    matrix_set = 0
    router_matrix = []

    with open(fname) as f:
        router_matrix = [list(map(int, x.split())) for x in f]  # Data from input file is stored in a two-dimensional list(array).
    matrix_set = 1

    print("\nReview original topology matrix:\n")
    for line in router_matrix:
        for item in line:
            print(item, end=" ")
        print()
    print()

    set_distances(router_matrix)  # Distances are stored in a dictionary with source router as key and distances as value.


# Function to store the distances in dictionary format.

def set_distances(router_matrix):

    global distances
    global nodes
    
    distances = {}
    nodes = []

    num_nodes = len(router_matrix)

    for i in range(num_nodes):
        tempdict = {}
        for j in range(num_nodes):
            if i != j and router_matrix[i][j] != -1:
                tempdict[j+1] = router_matrix[i][j]
        distances[i+1] = tempdict
        nodes.append(i+1)


def dijkstra(start):

    global distances
    global nodes
    global unvisited
    global previous
    global visited
    global interface

    # Initialize values to None.
    
    unvisited = {node: None for node in nodes}
    previous = {node: None for node in nodes}
    interface = {node: None for node in nodes}
    visited = {node: None for node in nodes}

    current = int(start)
    currentDist = 0
    unvisited[current] = currentDist

    while True:
        for next, distance in distances[current].items():

            if next not in unvisited: 
                continue
            
            newDist = currentDist + distance

            if unvisited[next] is None or unvisited[next] > newDist:
                unvisited[next] = newDist
                previous[next] = current

                if not interface[current]:
                    interface[next] = next
                else:
                    interface[next] = interface[current]
                    
        visited[current] = currentDist
        del unvisited[current]
        
        if not unvisited:
            break

        elements = [(node, dist) for node, dist in unvisited.items() if dist is not None]

        if not elements:
            break

        current, currentDist = sorted(elements, key=lambda x: x[1])[0]


# Function to generate the shortest path using the parent table generated by the Dijkstra function.

def shortest_path(start, end):
    
    global path

    path = []
    dest = int(end)
    src = int(start)
    path.append(dest)

    while dest != src:
        path.append(previous[dest])
        dest = previous[dest]

    path.reverse()

#----------------------------------------------------------------------------#
# Actual Program Starts
#----------------------------------------------------------------------------#

print_choices()

command = 0


# Run till the user wants to exit.

while command != 4:

    command = check_choices(input("\nCommand: "))
    
    # Accept the topology file.
    
    if command == 1:
        
        if matrix_set == 1:
            answer = input("\nThe network topology is already uploaded. Do you want to overwrite? (Y/N): ")

        if matrix_set == 0 or answer.lower() == 'y':
        
            filename = input("\nInput original network topology matrix data file [NxN distance matrix. (value: -1 for no link, 0 for self loop)]: ")

            if os.path.isfile(filename):
                process_file(filename)
                start = 0
                end = 0
            else:
                print("\nThe file does not exist. Please try again.")

    # Accept the source router and display the connection table.

    elif command == 2:
        
        if matrix_set == 1:
            
            start = input("\nSelect a source router: ")

            if start.isdigit() and int(start) > 0 and int(start) <= len(router_matrix):
                dijkstra(start)
                print("\nDestination\tInterface")
                for key in interface:
                    print(f"{key}\t\t{interface[key]}")
            else:
                start = 0
                print("\nPlease enter a valid source router.")

        else:
            print("\nNo network topology matrix exists. Please upload the data file first.. ")

    # Accept the destination router and display the shortest path and cost.

    elif command == 3:
    
        if matrix_set == 1:

            end = input("\nSelect a destination router: ")
            
            if end.isdigit() and int(end) > 0 and int(end) <= len(router_matrix):
                if int(start) == 0:
                    print("\nNo source router selected yet. Please select a source router using choice: 2.")
                elif int(start) == int(end):
                    print("\nSource and Destination routers are the same. Please select a different destination router.")
                elif previous[int(end)] is None:
                    print(f"\nNo route from Router {start} to Router {end}.")
                else:
                    shortest_path(start, end)
                    print(f"\nThe shortest path from Router {start} to Router {end} is:\n")
                    print(" -> ".join(map(str, path)))
                    print(f"\nThe total cost is {visited[int(end)]}.\n")
            else:
                print("\nPlease enter a valid destination router..")
        
        else:
            print("\nNo network topology matrix exists. Please upload the data file first.. ")

    elif command == 4:
        print("\nExit. Thanks you\n")
