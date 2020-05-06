"""Generate sales report showing total melons each salesperson sold."""


salespeople = []    # Creates an empty list of salespeople
melons_sold = []    # Creates empty list of melons sold

f = open('sales-report.txt')    # opens file data
for line in f:                  #loops over each line in file data
    line = line.rstrip()        # strips trailing whitespace
    entries = line.split('|')   # tokenizes data by pipeline, saves to variable

    salesperson = entries[0]    # saves salesperson name at entries index 0 to variable 
    melons = int(entries[2])    # saves melons sold at entries index 2 to variable, converts to integer 

    if salesperson in salespeople:  #if saleperson in empty list of salespeople
        position = salespeople.index(salesperson)   #searches through salespeople, returns
                                                    # earliest index at which the salesperson
                                                    # names appears, saves to position variable

        melons_sold[position] += melons # adds the number of melons sold to the index of
                                        # the salesperson's position in list 
    else:
        salespeople.append(salesperson) # if the salesperson isn't in the salespeople list,
        melons_sold.append(melons)     # add their name and their melons sold


for i in range(len(salespeople)):       # for the index in the range of the length of the salespeople list,
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') # print the salesperson at i with their melons sold


# erroneous information in txt file in the middle, is there a future use?
# Convert data file to dictionary instead by salesperson name to find their spec data, 
# will allow easy modification and quick lookup
# Could clean up the whole code with a function instead that prints the same statement

def sales_data(filename):
    """Returns report of melons sold by salesperson."""

    datafile = open(filename)

    for line in datafile:
        line = line.rstrip()
        sales_data = line.split("|")
        print(sales_data)

        name, sales, melons_sold = sales_data
        name = name.title()
        melons_sold = int(melons_sold)

        print(f"{name} sold {melons_sold} melons.")
 
 
sales_data("sales-report.txt")