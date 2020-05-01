def get_customer_invoice_balance(path):
    
    melon_cost = 1.00
    accounting_records = open(path)
    
    for line in accounting_records:
        words = line.rstrip()
        words = line.split("|")

        customer_name = words[1]
        melons_bought = float(words[2])
        total_paid = float(words[3])
        expected_payment = melons_bought * melon_cost
    
        if expected_payment != total_paid:
            print(f"{customer_name} paid ${total_paid}", f"expected ${expected_payment.}.")
        
    accounting_records.close()

get_customer_invoice_balance("customer-orders.txt")


