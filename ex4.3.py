"""
Exercise 4.3 Write code that classifies a given amount of money (which you store in a
variable named amount), specified in cents, as greater monetary units. Your code lists the
monetary equivalent in dollars (100 ct), quarters (25 ct), dimes (10 ct), nickels (5 ct), and
pennies (1 ct). Your program should report the maximum number of dollars that fit in the
amount, then the maximum number of quarters that fit in the remainder after you subtract
the dollars, then the maximum number of dimes that fit in the remainder after you subtract
the dollars and quarters, and so on for nickels and pennies. The result is that you express
the amount as the minimum number of coins needed.
"""
CENTS_IN_DOLLARS = 100
CENTS_IN_QUARTERS = 25
CENTS_IN_DIMES = 10
CENTS_IN_NICKELS = 5
CENTS_IN_PENNIES = 1

amount = 19880711

cents = amount
dollars = int(cents / CENTS_IN_DOLLARS)
cents -= dollars * CENTS_IN_DOLLARS

quarts = int(cents / CENTS_IN_QUARTERS)
cents -= quarts * CENTS_IN_QUARTERS

dimes = int(cents / CENTS_IN_DIMES)
cents -= cents * CENTS_IN_DIMES

nickels = int(cents / CENTS_IN_NICKELS)
cents -= nickels * CENTS_IN_NICKELS

cents = int(cents)

print(amount / CENTS_IN_DOLLARS, "Consist of:")
print("Dollars:", dollars)
print("Quarts:", quarts)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", cents)
