# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use input to read a string and float() to convert the string to a number.
hrs = input("Enter Hours:")
fhrs = float(hrs)
rate_ph = input("Enter rate per hour")
frate_ph = float(rate_ph)
gross_pay = fhrs * frate_ph
print("Pay:", gross_pay)