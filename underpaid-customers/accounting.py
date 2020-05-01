def get_customer_invoice_balance(path):    
    """Show how much customers have paid and how much money is owed.

    This function accesses accounting records and generates information showing 
    customer name, how many melons they bought, how much money in $ they owe, 
    and how much they have paid. 
    """
    
    melon_cost = 1.00
    accounting_records = open(path)
    
    for line in accounting_records:
        words = line.rstrip()
        words = line.split("|")

        line_number = words[0]
        customer_name = words[1]
        melons_bought = float(words[2])
        total_paid = float(words[3])
        expected_payment = melons_bought * melon_cost
    
        if expected_payment != total_paid:
            print(f"Ref line {line_number}, {customer_name} paid ${total_paid}", f"expected ${expected_payment}.")
        
    
    accounting_records.close()

get_customer_invoice_balance("customer-orders.txt")


