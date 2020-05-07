"""Print out all the melons in our inventory."""


from melons import melon_names, melon_seedlessness, melon_prices, melon_flesh_colors, melon_weights, melon_rind_colors


# def print_melon(name, seedless, price):
#     """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])


melons_info = {}   # Created empty dictionary
melons_attributes = {}

melons = list(melon_names.values()) # list values from melon dictionary 
pricelist = list(melon_prices.values()) # list values from price dictionary
seedless_value = list(melon_seedlessness.values())
flesh_color = list(melon_flesh_colors.values())
weights = list(melon_weights.values())
rinds = list(melon_rind_colors.values())

# for melon in melons:    
#     melons_info[melon] = melons_info.get(melon, 0)   #ask why this works
#     # this is how I can dump the nested dictionary under melon
# print(melons_info)

for price in pricelist:
    melon_price = {"price": price}

for value in seedless_value:
    value = {"seedless": value}

for flesh in flesh_color:
    flesh = {"flesh_color": flesh}

for weight in weights:
    weight = {"weight": weight}

for rind in rinds:
    rind = {"rind": rind}


melons_attributes.update(melon_price)
melons_attributes.update(value)
melons_attributes.update(flesh)
melons_attributes.update(weight)
melons_attributes.update(rind)

for melon in melons:    
    melons_info[melon] = melons_info.get(melon, melons_attributes)   #ask why this works
    # this is how I can dump the nested dictionary under melon
print(melons_info)

# return melons_info



# melons_attributes = 
# melons_info[melon] = 



# for price in pricelist:
#     melon_attributes[price] = melon_attributes.get(price, 0)






