# Compounded interest formula

originalPrincipalSum = 88000  # € 80.000
compoundingFrequency = 12  #n months
nominalAnnualInterestRate = 7.24  #r interest rate

#t = int(input("Overall lenght of time the interes is applied > "))
t = 10

newPrincipalSum = originalPrincipalSum * (
    1 + nominalAnnualInterestRate / compoundingFrequency)**(
        compoundingFrequency * t)

#print("Final amount after ", t, " years is ", newPrincipalSum)

# Example solution from the book


def final_amt(p, r, n, t):
  a = p * (1 + r / n)**(n * t)
  return a


#toInvest = float(input("How much do you want to invest? "))
toInvest = 88000
fnl = final_amt(
    toInvest, 0.0724 / 12, 12,
    15.5)  # for 7.24% interest, compounded 12 times per year, for 15.5 years
print("At the end of the period you'll have ", fnl)

# A few more examples from the book


def final_amt_v2(principalAmount, nominalPercentageRate, numTimesPerYear,
                 years):
  a = principalAmount * (1 + nominalPercentageRate / numTimesPerYear)**(
      numTimesPerYear * years)
  return a


def final_amt_v3(amt, rate, compounded, years):
  a = amt * (1 + rate / compounded)**(compounded * years)
  return a
