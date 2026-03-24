"""
Simple interest calculator 
  SI  = (P x R x T) / 100 
Where: p =  Principal amount  r = Rate of interest  t = Time period in years

"""

p =float(input("Enter the principal amount: "))
r =float(input("Enter the rate of interest: "))
t =float(input("Enter the time period in years: "))

si = (p * r * t) / 100 

print("The simple interest is:", si)