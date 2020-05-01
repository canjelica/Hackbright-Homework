def get_customer_invoice_balance(path):    
    """Show how much customers have paid and how much money is owed.

    This function accesses accounting records and generates information showing 
    customer name, how many melons they bought, how much money in $ they owe, 
    and how much they have paid. 
    """
    
    melon_cost = 1.00                   #Defines melon cost as global variable since this is independent of accounting records
    accounting_records = open(path)     #Opens passed-in argument as accounting txt file
    
    for line in accounting_records:         #Begins for loop to look over every line in argument
        words = line.rstrip()                   #Strips trailing whitespace from line if any
        words = line.split("|")             #Tokenizes each item in argument by line

        line_number = words[0]              #these create variables pointing to indices in each line
        customer_name = words[1]
        melons_bought = float(words[2])
        total_paid = float(words[3])
        expected_payment = melons_bought * melon_cost           #This calculates how much customer owes
    
        if expected_payment != total_paid:
            print(f"Ref line {line_number}, {customer_name} paid ${total_paid}", f"expected ${expected_payment}.")
        
            #This compares amount owed to how much was paid and prints a summary of information from the function.
    
    accounting_records.close()      #this closes file opened by the argument

get_customer_invoice_balance("customer-orders.txt")     #This tests the function with provided accounting record


