"""
You look at the clock and see that it is currently 14.00h. You set an alarm to
go off 535 hours later. At what time will the alarm go off? Write a program that prints the
answer. Hint: for the best solution, you will need the modulo operator.
"""

print(str((14 + 535) % 24) + ".00")