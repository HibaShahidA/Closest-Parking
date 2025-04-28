# Closest-Parking

An algorithm to maintain and manage a parking lot by providing tickets to the closest available parking spots. This system uses Dijkstra's algorithm for optimal parking spot allocation.

## Folder Structure

- `BikeDistances.csv`  
  Contains distance data related to bike parking spots in the parking lot. This file helps in calculating the closest available spot for bikes using Dijkstra's algorithm.

- `BikeSectionSpace.csv`  
  Contains information about available and occupied spaces for bikes in the parking lot. Empty slots are unmarked, while taken spots contain the vehicle's number plate.

- `CarDistances.csv`  
  Contains distance data related to car parking spots in the parking lot. This file is used to compute the closest available spots for cars.

- `CarSectionSpace.csv`  
  Contains information about available and occupied spaces for cars in the parking lot. Similar to `BikeSectionSpace.csv`, it marks empty spots and records taken spots with the vehicle number plate.

- `ParkingLot.py`  
  The main Python script that runs the parking lot system. This script uses Dijkstra's algorithm to find and allocate the closest available parking spot for cars and bikes.

- `README.md`  
  Documentation file that explains how the system works, setup instructions, and how to run the program.

- `project_proposal.pdf`  
  A proposal document outlining the details of the project, objectives, and implementation approach.

## How to Run

To run the program, simply execute the following command in your terminal:
```bash
python3 ParkingLot.py
```
This will start the parking lot management system, and it will allocate the closest parking spot to incoming vehicles based on the availability and distance data.
