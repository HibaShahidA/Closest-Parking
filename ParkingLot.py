## HELPER FUNCTIONS
def addNodes(graph, nodes):
  for i in nodes:
    graph[i] = []
  return graph

def addEdges(graph, edges, directed = False):
  for i in edges:
    if directed == False:
      graph[i[1]].append((i[0], i[2]))
    graph[i[0]].append((i[1], i[2]))
  return graph

def listOfNodes(graph):
  keys = [i for i in graph.keys()]
  return keys


## SEGMENT 1 DATA SET CREATION
#this is made in the form of a dictionary to find an empty spot in a given section
#dictionary format => {key:value} => {section: [[spot, spot's occupy status] of every spot]}
#named the spots as numbers starting from 1
##example format: CarParking = {'A': [[1,None],[2,None],[3,None],[4,None]], 'B': [[1,None],[2,None],[3,None]], 'C':[[1,None],[2,None],[3,None],[4,None],[5,None]]}
# sections = ['A','B','C']
# distances = [('A','A',0),('A','B',1),('A','C',0)]

CarSection = ['A','B','C','D','E','F','G','H']
BikeSection = ['a','b','c','d','e','f']

CarParking = {}
BikeParking = {}

CarSectionSpace = [('A',8),('B',8),('C',6),('D',8),('E',17),('F',8),('G',15),('H',15)]
BikeSectionSpace = [('a',70),('b',70),('c',50),('d',50),('e',50),('f',50)]

CarDistances =[
              ('A','A',0),('A','B',2),('A','C',2),('A','D',4),('A','E',4),('A','F',6),('A','G',8),('A','H',8),
              ('B','B',0),('B','C',0),('B','D',2),('B','E',3),('B','F',4),('B','G',5),('B','H',5),
              ('C','C',0),('C','D',0),('C','E',1),('C','F',2),('C','G',2),('C','H',3),
              ('D','D',0),('D','E',1),('D','F',1),('D','G',1),('D','H',4),
              ('E','E',0),('E','F',0),('E','G',1),('E','H',2),
              ('F','F',0),('F','G',1),('F','H',2),
              ('G','G',0),('G','H',1),
              ('H','H',0),]
BikeDistances=[
              ('a','a',0),('a','b',1),('a','c',2),('a','d',3),('a','e',4),('a','f',5),
              ('b','b',0),('b','c',1),('b','d',2),('b','e',3),('b','f',4),
              ('c','c',0),('c','d',1),('c','e',2),('c','f',3),
              ('d','d',0),('d','e',1),('d','f',2),
              ('e','e',0),('e','f',1),
              ('f','f',0),]

directed = False
plates = []

car_lot = {}
car_lot = addNodes(car_lot, CarSection)
car_lot = addEdges(car_lot,CarDistances,directed)

bike_lot = {}
bike_lot = addNodes(bike_lot, BikeSection)
bike_lot = addEdges(bike_lot,BikeDistances,directed)

def createspace(dictionary, data):
  for element in data:
    section = element[0]
    spaces = element[1]
    value = []
    for space in range(1, spaces+1):
      value.append([space, None])
    dictionary[section] = value
  return dictionary


CarParking = createspace(CarParking, CarSectionSpace)
BikeParking = createspace(BikeParking, BikeSectionSpace)
##visualisation of the dictionaries after
# CarParking = {
#  'A': [[1, None], [2, None], [3, None], [4, None], [5, None], [6, None], [7, None], [8, None]],
#  'B': [[1, None], [2, None], [3, None], [4, None], [5, None], [6, None], [7, None], [8, None]],
#  'C': [[1, None], [2, None], [3, None], [4, None], [5, None], [6, None]],
#  'D': [[1, None], [2, None], [3, None], [4, None], [5, None], [6, None], [7, None], [8, None]],
#  'E': [[1, None], [2, None], [3, None], [4, None], [5, None], [6, None], [7, None], [8, None], [9, None], [10, None], [11, None], [12, None], [13, None], [14, None], [15, None], [16, None], [17, None]],
#  'F': [[1, None], [2, None], [3, None], [4, None], [5, None], [6, None], [7, None], [8, None]],
#  'G': [[1, None], [2, None], [3, None], [4, None], [5, None], [6, None], [7, None], [8, None], [9, None], [10, None], [11, None], [12, None], [13, None], [14, None], [15, None]],
#  'H': [[1, None], [2, None], [3, None], [4, None], [5, None], [6, None], [7, None], [8, None], [9, None], [10, None], [11, None], [12, None], [13, None], [14, None], [15, None]]
#  }

# BikeParking = {
#  'a': [[1, None], [2, None], [3, None], ..., [69, None], [70, None]],
#  'b': [[1, None], [2, None], [3, None], ..., [69, None], [70, None]],
#  'c': [[1, None], [2, None], [3, None], ..., [48, None], [49, None], [50, None]],
#  'd': [[1, None], [2, None], [3, None], ..., [48, None], [49, None], [50, None]],
#  'e': [[1, None], [2, None], [3, None], ..., [48, None], [49, None], [50, None]],
#  'f': [[1, None], [2, None], [3, None], ..., [48, None], [49, None], [50, None]]
#  }





## SEGMENT 2 FREE SPOTS  
#place in a free spot
def putFreeSpot(parking, section, plate):
    space = parking[section][0][1]
    spot = parking[section][0][0]
    if space == None:
      parking[section][0][1] = plate
      return spot
    else:
        return None


## SEGMENT 3 DATA SORTING
#this sorting pushes all full spots to the end of the list and the empty spots to the front
def sortSpaces(parking, section):
  non_none = []
  nones = []
  for value in parking[section]:
    if None in value:
      nones.append(value)
    else:
      non_none.append(value)
  
  #insertion sort
  for i in range(1, len(nones)):
    key = nones[i]
    j = i-1
    while j >=0 and nones[j][0] > key[0]:
      nones[j+1] = nones[j]
      j -= 1
    nones[j+1] = key
  final = nones + non_none
  return final


## SEGMENT 4 CLOSEST SECTION/SPOT
import math

def closestParking(parkingLot, plate, parking):
  sections = listOfNodes(parkingLot)
  ind = 0
  sec = []
  while ind != len(sections):
    section = sections[ind]
    minDistance = math.inf
    minSection = ''
    for close in parkingLot[section]:
      if close[1]<minDistance and close[0] not in sec:
        minDistance = close[1]
        minSection = close[0]
    ind = sections.index(minSection)
    spot = putFreeSpot(parking,minSection,plate)
    if spot != None:
      parking[minSection][0][1] = plate
      return (minSection, spot)
    else:
      sec.append(minSection)


## PARTIAL SEGMENT: FIND PARKED VEHICLE
#finds and returns location of a vehicle if it is parked, otherwise returns None
def findParked(parking, plate):
  for element in parking:
    spots = parking[element]
    l = len(spots)-1
    while l >= 0 and spots[l][1] != None:
      if spots[l][1] == plate:
        return (element, spots[l][0], l)
  return None
    

## MAIN SEGMENT INPUT
def main():
  global parking, plate, lot
  
  vehicle_type = input('Please enter 1 if your vehicle is a car or 0 if it is a motorcyle:')
  #In case people enter other than 0/1, repeated prompt will be given to enter the correct number
  while not(vehicle_type == '0' or vehicle_type == '1'):
    print('Please only choose 0 or 1')
    vehicle_type = input('Please enter 1 if your vehicle is a car or 0 if it is a motorcyle:')
  if vehicle_type == '0':
    parking = BikeParking
    lot = bike_lot
  elif vehicle_type == '1':
    parking = CarParking
    lot = car_lot

  plate = input('Please enter your plate number: ')
  while len(plate) != 6 or not(plate[:2].isalpha() and all(char.isdigit() for char in plate[2:]) or plate[:3].isalpha() and all(char.isdigit() for char in plate[3:])):
    plate = input('Please enter the correct plate number using only alphabets or numbers: ')

  if ready.lower() == 'y':
    if plate in plates:
      section, spot, l = findParked(parking, plate)
      print('You are already parked at', section + str(spot))
    else:
      toPark(parking)
      plates.append(plate)
  elif ready.lower() == 'n':
    toLeave(parking)

#toPark() will find an empty spot and return that as the parking location
def toPark(parking):
  spot = closestParking(lot, plate, parking)
  print('You will find your parking at ', spot[0]+str(spot[1]))

  parking[spot[0]] = sortSpaces(parking, spot[0])

#toLeave() removes the vehicle plate from the spot it was previously in
#prints a message if plate does not exist - this is in case someone accidentally inserts the wrong command
def toLeave(parking):
  if plate in plates:
    print('Have a nice day!')
    section, spot, l = findParked(parking, plate)
    parking[section][l] = [spot, None]
    parking[section] = sortSpaces(parking, section) 
    plates.remove(plate)      
  else:
    print('You have not parked yet')

#initialise the program by calling the main function and marking possible parking spots as free (True)
PossiblePark = True

#will keep adding vehicles as long as there is space. If PossiblePark is False, this means all spaces are full
while True:
  ready = input('Enter Y if you are ready to park. \nEnter N if you are ready to leave.')
  while not (ready.lower() == 'y' or ready.lower() == 'n'):
    print('Please enter a valid response')
    ready = input('Enter Y if you are ready to park. \nEnter N if you are ready to leave.')
  
  if PossiblePark:
    main()
    
    PossiblePark = False
    for element in parking:
      if parking[element][0][1] == None:
        PossiblePark = True
  if not PossiblePark and ready == 'N':
    main()
  elif not PossiblePark:
    #once no more spaces are free, print this 
    print('Unfortunately, the parking lot is full.')
