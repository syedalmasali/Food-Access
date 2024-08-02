"""
SEARCH FOOD PROGRAMS
Program which will allow the user to search through this dataset 
and find particular information they are looking for. In this case,
they are looking for data on food deserts around America.
"""


#START OF PROGRAM

# import the library for this lab
from food_access_lab import FoodAccessRecord
from food_access_lab import lookForwardBackward
from food_access_lab import lookForwardBackward



def statesearch(thelist):
  '''
  Searches for the data with respect to the state. Prints
  all the data the user wants within this function. Asks
  for the input within this function. Does not take into account
  if the state is acronym or capitalized because the lab
  did not require it
  Parameters: 
    thelist (list)- list of objects
  Returns: Nothing
  Side Effects: Prints some statements based on results of input
                Asks the user for input
                Displays the data the user wants
  '''
  #Intialize variables
  states= []
  indices=[]
  #Make a list of states
  for x in range(len(thelist)):
    line = thelist[x]
    state = line.get_state()
    states.append(state)
  #Ask for an input
  whatstate= input("What is the name of the state? ")
  #Make a list of indexes based on the input
  for i in range(len(states)):
    check= states[i]
    if check.startswith(whatstate):
      indices.append(i)
  #Foundational print statement
  print("================================================================================")
  print("| %15s | %12s |%9s| %7s| %6s | %6s | %7s|" % ( "County", "State", \
        "Total Pop", "LFA Pop", "Income", "Senior", "Vehicle" ) )
  print("--------------------------------------------------------------------------------")
  #Print the data based on the list indexes
  for y in range(len(indices)):
    variable= indices[y]
    temp= thelist[variable]
    print("| %15s | %12s |%9s| %7s| %6s | %6s | %7s|"%(temp.get_county()[:15],\
        temp.get_state()[:12], temp.get_population(), temp.get_people(1), \
        temp.get_low_income(1),temp.get_seniors(1),temp.get_vehicle_access(1)))
    print("--------------------------------------------------------------------------------")



def validchoiceforpop(minreq):
  '''
  Checks if the input was a digit for the populationsearch
  Takes in the input and checks the requirements and returns
  fixed version of the number.
  Parameter:
    minreq (str)= the input of the population
  Returns:
    minreq (str)= fixed population requirement
  Side Effects: Prints some statements based on input
  '''
  #If the min population is 0
  if minreq == 0:
    return 0
  #Check if the input is a number
  while not ((minreq.isdigit()) and (minreq => 0)) :
    print("Value must be an integer.")
    minreq = input ("What is the minimum population? ")
  #Return a string
  return minreq

 

def populationsearch(thelist):
  '''
  Threshold Search
  Searches the list for any population greater than the user input.
  If so, appends the indices and prints the results the user
  was looking for. Takes in the original list of objects,
  but does not return anything. 
  Parameters: 
    thelist (list)- list of objects
  Returns: Nothing
  Side Effects: Prints some statements based on results of input
                Prints the data the user wants
                Calls the validchoiceforpop function
  '''
  #Initialize variables
  popul= []
  indices= []
  #Make a list of population
  for x in range(len(thelist)):
    line = thelist[x]
    pop = line.get_population()
    popul.append(pop)
  #Ask for the min population
  minreq = input("What is the minimum population? ")
  #Special circumstances for input
  if (minreq == "") or (minreq == " "):
    minreq = 0
  #Call the validchoiceforpop function
  minreq = validchoiceforpop(minreq)
  #Make a list of indexes where pop is greater than the input
  for i in range(len(popul)):
    if int(minreq) < popul[i]:
      indices.append(i)
  #Do this when there is nothing in the index list
  if indices == []:
    print("NO RECORDS FOUND")
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
      print("| %15s | %12s |%9s| %7s| %6s | %6s | %7s|"%(temp.get_county()[:15],\
          temp.get_state()[:12], temp.get_population(), temp.get_people(1), \
          temp.get_low_income(1),temp.get_seniors(1),temp.get_vehicle_access(1)))
      print("--------------------------------------------------------------------------------")



def countysearch(thelist):
  '''
  The binary search that locates the first match of the prefix in the
  list of data. Takes in the official list and converts it to get
  only the counties. If it is not found, returns -1 as the index
  which indicates the prefix was not in the list.
  Parameters: 
    thelist (list)- list of objects
  Returns: 
    (list of various of types)
    index (int)- returns the index where the first match was
    wcounty (str)- the input the user typed in
    temp (str)- the original capitalized county found
    newcounts (list)- list of the capitalized counties
  Side Effects: Prints some statements based on results of input
                Asks for the input form the user
                Takes into account if the input was lowercase
  '''
  #Initializes variables
  counties= []
  index= -1
  #Gets the counties and makes a list of it in lower case
  for i in range(len(thelist)):
    line = thelist[i]
    county = line.get_county()
    county = county.lower()
    counties.append(county)
  #Gets the lower case input
  wcounty= input("What is name of the county (or starts with)? ")
  wcounty= wcounty.lower()
  #Initializes variables
  lower= 0
  upper= len(counties)-1
  #Binary search for the prefix
  mycondition = False
  while mycondition == False:
    mid = (lower+upper)//2
    temp= counties[mid]
    modstring= temp[:len(wcounty)]
    if (mid == lower) or (mid == upper):
      break
    if temp.startswith(wcounty):
      index=mid
      mycondition = True
    elif wcounty <= modstring:
      upper = mid-1
    elif wcounty >= modstring:
      lower = mid+1
  #Makes a list of counties that are capitalized
  newcounts= []
  for i in range(len(thelist)):
    line = thelist[i]
    county = line.get_county()
    newcounts.append(county)
  temp = newcounts[index]
  #Returns a list
  return [index,wcounty,temp,newcounts]



def printdata(counties, list1, thelist):
  '''
  Prints the offciial data from the original list of objects.
  Takes in the lists from playsearch to output all the data
  the user wants based on the county they chose.
  Parameters: 
    counties (list)= list of counties that have the prefix
    list1 (list)= the capitalized list of counties from countysearch
    thelist (list)= the original list with the methods  
  Returns: Nothing
  Side Effects: Prints statements of all the data the user wants
  '''
  #Initializes variable
  empt= []
  #Foundational print statement
  print("================================================================================")
  print("| %15s | %12s |%9s| %7s| %6s | %6s | %7s|" % ( "County", "State", \
        "Total Pop", "LFA Pop", "Income", "Senior", "Vehicle" ) )
  print("--------------------------------------------------------------------------------")

  #Makes a list of indexes
  for i in range(len(counties)):
      x= list1.index(counties[i])
      empt.append(x)
  #Prints the data based on the relative indexes
  for y in range(len(empt)):
    variable= empt[y]
    temp= thelist[variable]
    print("| %15s | %12s |%9s| %7s| %6s | %6s | %7s|"%(temp.get_county()[:15],\
        temp.get_state()[:12], temp.get_population(), temp.get_people(1), \
        temp.get_low_income(1),temp.get_seniors(1),temp.get_vehicle_access(1)))
    print("--------------------------------------------------------------------------------")



def validchoice(choice):
  '''
  Checks if the choices are 0, 1, 2, 3 which are the valid inputs.
  Parameters: choice (str) = the input of the user
  Returns: choice (str) = fixed choice
  Side Effects: Prints some statements based on results of input
  '''
  #Checks the conditions of input and constantly prompts the user
  while (choice != "1")and(choice != "2")and(choice != "3")and(choice != "0"):
    print("Input must be valid")
    print("Please select one of the following choices: \n"
          "1. Search by county \n"
          "2. Search by state \n"
          "3. Search by population \n"
          "0. Quit ")
    choice = input("Enter selection: ")
  #Returns a string
  return choice



def playsearch(thelist):
  '''
  Function that asks the input question that runs the other functions.
  Give them the list of choices and do the things according to the
  input. Takes in the objects list gotten from main function.
  Parameters: 
    thelist (list)- list of objects
  Returns: 
    Nothing
  Side Effects: Prints some statements based on results of input
                Calls the countysearch function
                Calls the validchoice function
                Calls the lookForwardBackward function
                Calls the printdata function
                calls the statesearch function
                Calls the populationsearch

  '''
  #Big original loop for input until 0 is input
  condition = False
  while condition == False:
    print("Please select one of the following choices: \n"
          "1. Search by county \n"
          "2. Search by state \n"
          "3. Search by population \n"
          "0. Quit ")
    choice = input("Enter selection: ")
    #Checks if choice is valid
    choice = validchoice(choice)
    #Do this if 1 is picked (County)
    if choice == "1":
      #Call the countysearch function
      mlist = countysearch(thelist)
      start = mlist[0]
      #Conditon if input not in the list
      if start == -1:
        print("No Records Found")
      #Use the tools from the countysearch function
      else:
        match = mlist[1]
        counties = [mlist[2]]
        #Find the counties left of the first found
        backward = lookForwardBackward(thelist, start, match, -1)
        for y in range(len(backward)):
          line = backward[0]
          county = line.get_county()
          counties.append(county)
        #Find the counties right of the first found
        forward = lookForwardBackward(thelist, start, match, 1)
        for x in range(len(forward)):
          line = forward[x]
          county = line.get_county()
          counties.append(county)
        #Call the printdata function
        printdata(counties, mlist[3], thelist)
    #Do this if 2 is picked (State)
    elif choice == "2":
      statesearch(thelist)
    #Do this if 3 is picked (Pop)
    elif choice == "3":
      populationsearch(thelist)
    #Do this if 0 is picked (Exit)
    else:
      print("Goodbye!")
      condition = True
  


def main():
  '''
  Takes in the text data and converts it to a list of object.
  It is then passed into the playsearch function, where the actual
  search goes on.
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
  #Call the playsearchfunction
  playsearch(mylist)
main()
