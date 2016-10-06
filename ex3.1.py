"""
The cover price of a book is $24.95, but bookstores get a 40 percent discount.
Shipping costs $3 for the first copy and 75 cents for each additional copy.
Calculate the total wholesale costs for 60 copies.
"""
cost_book = 24.95
discount = 0.6  # Discount 40 percent
cost_shipping = 3  # Only for first copy
cost_shipping_addition = 75 / 78  # 78 cent is 1 dollar. convert to dollar unit

# Calculate 60 copies
sixty_copies_cost = (1 * (cost_book * discount)) + cost_shipping + (
                    59 * ((cost_book * discount) + cost_shipping_addition))

print("This is cost 60 copies: %s dollar" % (sixty_copies_cost))
