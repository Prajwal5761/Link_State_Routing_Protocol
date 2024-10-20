
# Link-State Routing Protocol Simulator

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Program](#running-the-program)
- [Input File Format](#input-file-format)
  - [Example Input File](#example-input-file)
- [Usage](#usage)
- [Dijkstra’s Algorithm](#dijkstra’s-algorithm)
- [Error Handling](#error-handling)
- [Contributing](#contributing)


## Introduction
This project simulates a **Link-State Routing Protocol** using **Dijkstra's Algorithm** to find the shortest path between routers in a network. The program reads a network topology from a file, processes the network's cost matrix, and builds the shortest path tree. The user can view the connection table and calculate the shortest path from a source router to any destination.

This is useful for simulating and studying how **Link-State Routing** protocols (like OSPF - Open Shortest Path First) work in computer networks.

## Features
- Input a network topology from a file.
- Display the original topology matrix.
- Build a connection table for a given source router.
- Find the shortest path between two routers using Dijkstra’s algorithm.
- Display the total cost of the shortest path.
- Comprehensive error handling for invalid inputs and network scenarios.
  
## Project Structure
```
├── Link_state_RT.py        # Main Python script
├── topology.txt          # Sample input file containing NxN matrix of network topology
├── README.md             # Project documentation (this file)
```

## Getting Started

### Prerequisites
- **Python 3.x** installed on your system.
- Basic knowledge of graph theory and Dijkstra's algorithm.
- Familiarity with command-line usage.

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/link-state-routing-simulator.git
   cd link-state-routing-simulator
   ```

2. **Install Python**:
   If you don't have Python installed, download and install it from the [official Python website](https://www.python.org/downloads/).

3. **Prepare the input file**:
   Make sure you have your network topology ready in the form of a NxN cost matrix. You can use the provided `topology.txt` as a reference.

### Running the Program
1. Navigate to the directory where `Link_state_RT.py` is located.
2. Run the program using the following command:
   ```bash
   python Link_state_RT.py
   ```

3. Follow the on-screen prompts to input the network topology and calculate shortest paths.

## Input File Format
The input file should contain a **NxN matrix** representing the costs of links between routers. Each line in the file corresponds to a row in the matrix:
- A value of `0` represents a self-loop (router connected to itself).
- A value of `-1` represents no direct link between two routers.
- Positive integers represent the cost of the link between two routers.

### Example Input File
Save the following data as `topology.txt`:
```
0 1 3 -1
1 0 1 4
3 1 0 2
-1 4 2 0
```
This matrix represents a network with 4 routers, where:
- Router 1 is connected to Router 2 with a cost of 1 and Router 3 with a cost of 3. It has no direct connection to Router 4.
- Router 2 is connected to Routers 1, 3, and 4 with respective costs of 1, 1, and 4.
- Router 3 is connected to Router 1 with a cost of 3, Router 2 with a cost of 1, and Router 4 with a cost of 2.
- Router 4 is connected to Router 2 and Router 3 with respective costs of 4 and 2.

## Usage
Once the program is running, it will present you with several options:

1. **Input Network Topology File**:  
   Upload the NxN cost matrix by entering the path to your topology file (e.g., `topology.txt`).

2. **Build a Connection Table**:  
   Enter the source router, and the program will build the connection table using Dijkstra's algorithm.

3. **Find the Shortest Path to Destination Router**:  
   After selecting the source router, input the destination router to see the shortest path and its total cost.

4. **Exit**:  
   Exits the program.

### Example Output
After selecting options 2 or 3, the program might return output similar to the following:
```
The shortest path from Router 1 to Router 4 is:
1 -> 2 -> 3 -> 4

The total cost is 6.
```

## Dijkstra’s Algorithm
This project implements **Dijkstra's Algorithm** to compute the shortest paths between routers. Here’s a brief overview:
1. Initialize distances from the source to all nodes as infinity, except for the source node (distance 0).
2. For the current node, calculate the distance to its neighbors. If a shorter path is found, update the distance.
3. Mark the current node as visited and move to the unvisited node with the smallest distance.
4. Repeat steps 2-3 until all nodes are visited.

This ensures that the shortest path to all nodes is found efficiently.

## Error Handling
The program includes robust error handling for scenarios such as:
- Invalid or missing input files.
- Invalid source or destination router numbers.
- Cases where no path exists between the source and destination.
- Handling of self-loops and no-link scenarios (`-1` values).

## Contributing
Contributions are welcome! Feel free to fork this project, submit issues, or create pull requests.

### To Contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.



