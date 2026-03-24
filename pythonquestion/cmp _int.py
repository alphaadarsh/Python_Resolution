"""
Amount = p (1 + r/100) ** t  

ci = Amount - p
"""

p =float(input("Enter the principal amount: "))
r =float(input("Enter the rate of interest: "))
t =float(input("Enter the time period in years: "))

Amount =  p * (1  + r/100) ** t 

ci = Amount - p  

print("The ci is:" ,  ci)