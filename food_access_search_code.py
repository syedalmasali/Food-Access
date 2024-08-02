"""
Code for Sort on Food Access around the US
"""

# import the library for this lab
from food_access_lab import FoodAccessRecord



def filstatename(thelist):
  '''
  Filter through the list based on the user's input.
  Does not take into account case sensitivity because
  the lab did not require it. Makes some lists to make it
  easier to get the indexes and a list of states.
  Professor Rich there is a faster way, but since this works
  I left it this way
  Parameters: 
    thelist- (list) the list of records as object
  Return:
    indices- (list) the case where the list is empty
    newlist- (list) Makes a new list of what the user wanted
  Side Effects: Prints some statements based on user input
                Makes some list to find indexes and find states
  '''
  states=[]
  indices= []
  newlist= []
  whatstate = input("What is the name of the state? ")
  #Make a list of states
  for x in range(len(thelist)):
    line = thelist[x]
    state = line.get_state()
    states.append(state)
  #Make a list of indexes based on the input
  for i in range(len(states)):
    check= states[i]
    if check.startswith(whatstate):
      indices.append(i)
  #This is what happens if there is no list
  if indices == []:
    print("No records found!")  
    print("")
    return indices
  #Foundational print statement
  print("================================================================================")
  print("| %15s | %12s |%9s| %7s| %6s | %6s | %7s|" % ( "County", "State", \
        "Total Pop", "LFA Pop", "Income", "Senior", "Vehicle" ) )
  print("--------------------------------------------------------------------------------")
  #Print the data based on the list indexes and makes a new list 
  #to be passed back into the options
  for y in range(len(indices)):
    variable= indices[y]
    temp= thelist[variable]
    newlist.append(temp)
    print("| %15s | %12s |%9s| %7s| %6s | %6s | %7s|"%(temp.get_county()[:15],\
        temp.get_state()[:12], temp.get_population(), temp.get_people(1), \
        temp.get_low_income(1),temp.get_seniors(1),temp.get_vehicle_access(1)))
    print("--------------------------------------------------------------------------------")
  #Return the new list with only the objects that match the state name
  return newlist



def minvalidchoiceforpop(minreq):
  '''
  Check if the minimum population is ok. 
  Makes sure it is a positive integer and is greater
  than 0.
  Parameters: 
    minreq (str)- smalled pop
  Returns: 
    0 (int)- Return this if the maxpop is 0
    minreq (str)- bigger pop corrected
  Side Effects: Prints some statements based on results of input
  '''
  if minreq == 0:
    return 0
  #Check if the input is a number
  while not ((minreq.isdigit()) and (int(minreq) >= 0)) :
    print("Value must be an integer.")
    minreq = input ("What is the minimum population? ")
  #Return a string
  return minreq



def maxvalidchoiceforpop(maxreq, minreq):
  '''
  Check if the maximum population is ok. 
  Makes sure it is a positive integer and is greater
  than the min population
  Parameters: 
    minreq (str)- smalled pop
    maxreq (str)- bigger pop
  Returns: 
    0 (int)- Return this if the maxpop is 0
    maxreq (str)- bigger pop corrected
  Side Effects: Prints some statements based on results of input
  '''
  if maxreq == 0:
    return 0
  #Check if the input is a number
  while not ((maxreq.isdigit()) and (int(minreq) <= int(maxreq))) :
    print("Value must be an integer higher than minimum.")
    maxreq = input ("What is the maximum population? ")
  #Return a string
  return maxreq



def filtpop(thelist):
  '''
  Min and Max search of population. 
  Basically goes through the list and gets the population.
  If the poulation is within the bound, print the information.
  If list is empty, return empty list.
  Professor Rich there is a faster way, but since this works
  I left it this way.
  Parameters: 
    alist (list)- list of objects
  Returns: 
    newlist (list)- Fixed list based on sortstate
    indices (list)- Empty list for no records case
  Side Effects: Prints some statements based on results of input
                Prints the data the user wants
                Calls the validchoice function (both min and max)
  '''
  #Initialize variables
  popul= []
  indices= []
  newlist = []
  #Make a list of population
  for x in range(len(thelist)):
    line = thelist[x]
    pop = line.get_population()
    popul.append(pop)
  #Ask for the min and maxpopulation
  minreq = input("What is the minimum population? ")
  minreq = minvalidchoiceforpop(minreq)
  maxreq = input("What is the maximum population? ")
  maxreq = maxvalidchoiceforpop(maxreq, minreq)
  #Make a list of indexes where pop is greater than the input
  for i in range(len(popul)):
    if int(minreq) < popul[i] and popul[i] < int(maxreq):
      indices.append(i)
  #This is what happens if there is no list
  if indices ==[]:
    print("No records found!")  
    print("")
    return indices
  #Print all the data based on the indexes
  else:
    print("================================================================================")
    print("| %15s | %12s |%9s| %7s| %6s | %6s | %7s|" % ( "County", "State", \
          "Total Pop", "LFA Pop", "Income", "Senior", "Vehicle" ) )
    print("--------------------------------------------------------------------------------")
    #Print the data based on the list indexes
    for y in range(len(indices)):
      variable= indices[y]
      temp= thelist[variable]
      newlist.append(temp)
      print("| %15s | %12s |%9s| %7s| %6s | %6s | %7s|"%(temp.get_county()[:15],\
          temp.get_state()[:12], temp.get_population(), temp.get_people(1), \
          temp.get_low_income(1),temp.get_seniors(1),temp.get_vehicle_access(1)))
      print("--------------------------------------------------------------------------------")
  #Return the new list with only the objects that match the pop requirements
  return newlist



def sortstate(alist):
  '''
  SELECTION SORT FIXED
  Esentially goes through the list and picks out the state name.
  Depending if the name  of certain index is bgger than the next,
  it will adjust to make the list in order. If empty, return empty list.
  Parameters: 
    alist (list)- list of objects
  Returns: 
    alist (list)- Fixed list based on sortstate
  Side Effects: Prints some statements based on results of input
                Prints the data the user wants
  '''
  #This is what happens if there is no list
  if alist ==[]:
    print("No records found!")  
    print("")
    return alist
  #Foundational print statement
  print("================================================================================")
  print("| %15s | %12s |%9s| %7s| %6s | %6s | %7s|" % ( "County", "State", \
        "Total Pop", "LFA Pop", "Income", "Senior", "Vehicle" ) )
  print("--------------------------------------------------------------------------------")
  #Go through the list and do the SELECTION sort for state
  for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location].get_state()>alist[positionOfMax].get_state():
               positionOfMax = location

       temp1 = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp1
  #Go through the list and print the data for each state
  for y in range(len(alist)):
    temp= alist[y]
    print("| %15s | %12s |%9s| %7s| %6s | %6s | %7s|"%(temp.get_county()[:15],\
        temp.get_state()[:12], temp.get_population(), temp.get_people(1), \
        temp.get_low_income(1),temp.get_seniors(1),temp.get_vehicle_access(1)))
    print("--------------------------------------------------------------------------------")
  #return the list with sorted states
  return alist



def sortpop(alist):
  '''
  INSERTION SORT FIXED
  Esentially goes through the list and picks out the population.
  Depending if the population of certain index is bgger than the next,
  it will adjust to make the list in order. If empty, return empty list.
  Parameters: 
    alist (list)- list of objects
  Returns: 
    alist (list)- Fixed list based on sortpop
  Side Effects: Prints some statements based on results of input
                Prints the data the user wants
  '''
  #This is what happens if there is no list
  if alist ==[]:
    print("No records found!")  
    print("")
    return alist
  #Foundational print statement
  print("================================================================================")
  print("| %15s | %12s |%9s| %7s| %6s | %6s | %7s|" % ( "County", "State", \
        "Total Pop", "LFA Pop", "Income", "Senior", "Vehicle" ) )
  print("--------------------------------------------------------------------------------")
  #Go through the list and do the SELECTION sort for pop
  for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index
     while position>0 and alist[position-1].get_population() > \
     currentvalue.get_population():
        alist[position]=alist[position-1]
        position = position-1
     alist[position]=currentvalue
  #Go through the list and print the data for each state
  for y in range(len(alist)):
    temp= alist[y]
    print("| %15s | %12s |%9s| %7s| %6s | %6s | %7s|"%(temp.get_county()[:15],\
        temp.get_state()[:12], temp.get_population(), temp.get_people(1), \
        temp.get_low_income(1),temp.get_seniors(1),temp.get_vehicle_access(1)))
    print("--------------------------------------------------------------------------------")
  #return the list with sorted pop
  return alist
  


def validchoice(choice):
  '''
  Checks if the choices are 0, 1, 2, 3, 4, 5 which are the valid inputs.
  Parameters: 
    choice (str) = the input of the user
  Returns: 
    choice (str) = fixed choice
  Side Effects: Prints some statements based on results of input
  '''
  #Checks the conditions of input and constantly prompts the user
  while (choice != "1")and(choice != "2")and(choice != "3") \
  and (choice != "4")and (choice != "5") and(choice != "0"):
    print("Input must be valid")
    print("1. Filter records by state name \n"
          "2. Filter records by total population \n"
          "3. Sort by state name \n"
          "4. Sort by total population \n"
          "5. Reset list to all records \n"
          "0. Quit \n")
    choice = input("Enter selection: ")
  #Returns a string
  return choice



def options(mylist):
  '''The main function that calls all the other functions. It just 
  asks the options. It makes a copy of the original list for option 5.
  Parameter:
    mylist: (list) Original list of record objects
  Return:
    Nothing
  Side Effects: Calls the other main functions
              validchoice
              filstatename
              filtpop
              sortstate
              sortpop
  '''
  #Make a copy of the list
  copylist= mylist.copy()
  #Initialize the condition
  condition = False
  #Repeatedly ask the options
  while condition == False:
    print("1. Filter records by state name \n"
          "2. Filter records by total population \n"
          "3. Sort by state name \n"
          "4. Sort by total population \n"
          "5. Reset list to all records \n"
          "0. Quit \n")
    choice = input("Enter selection: ")
    #Check if the choice is valid
    choice = validchoice(choice)
    #Do this if choice is 1
    if choice == "1":
      adaptlist = filstatename(mylist)
      mylist = adaptlist
    #Do this if choice is 2
    elif choice == "2":
      adaptlist = filtpop(mylist)
      mylist = adaptlist
    #Do this if choice is 3
    elif choice == "3":
      adaptlist = sortstate(mylist)
      mylist = adaptlist
    #Do this if choice is 4
    elif choice == "4":
      adaptlist = sortpop(mylist)
      mylist = adaptlist
    #Do this if choice is 5
    elif choice == "5":
      print("Resetting to original data.")
      mylist= copylist
    #Do this if choice is 0
    elif choice == "0":
      print("Goodbye!")
      condition = True



def main():
  '''
  The main function to be passed into the options function.
  Takes in the text data and converts it to a list of record objects.
  Parameters:
    Nothing
  Returns:
    Nothing
  Side Effects: Highly dependent on the text file and the FoodAccessRecord
  '''
  #Make a list of data
  mylist= []
  file_obj = open("/data/cs21/food_access/food_access.csv", "r")
  raw_data = file_obj.read()
  lines = raw_data.splitlines()
  #Make a list of objects
  for i in range(len(lines)):
    line= lines[i]
    record = FoodAccessRecord(line)
    mylist.append(record)
  #Call the options function
  options(mylist)
main()
