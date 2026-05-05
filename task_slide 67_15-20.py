# TASK 15: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:  https://apps.wingubox.com/best-paye-tax-calculator-for-kenya
# Write a normal program but use functions if you feel comfortable.

# calculate gross salary
def calc_gross(basic, benefits):
    gross = basic + benefits
    return gross

basic_salary = float(input("Enter basic salary: "))
benefits = float((input("Enter benefit: ")))

gross_salary=calc_gross(basic_salary,benefits)
print(f"Gross salary is {gross_salary}.")

# calculate nhif
def find_nhif(my_gross):
    if my_gross <= 5999:
        nhif = 150
    elif my_gross >= 6000 and my_gross <= 7999:
        nhif = 300
    elif my_gross >= 6000 and my_gross <= 7999:
        nhif = 300
    elif my_gross >= 6000 and my_gross <= 7999:
        nhif = 300
    elif my_gross >= 6000 and my_gross <= 7999:
        nhif = 300
    elif my_gross >= 6000 and my_gross <= 7999:
        nhif = 300
    elif my_gross >= 6000 and my_gross <= 7999:
        nhif = 300
    elif my_gross >= 6000 and my_gross <= 7999:
        nhif = 300
    elif my_gross >= 6000 and my_gross <= 7999:
        nhif = 300
    elif my_gross >= 6000 and my_gross <= 7999:
        nhif = 300
    elif my_gross >= 6000 and my_gross <= 7999:
        nhif = 300
    elif my_gross >= 6000 and my_gross <= 7999:
        nhif = 300
    elif my_gross >= 6000 and my_gross <= 7999:
        nhif = 300
    elif my_gross >= 6000 and my_gross <= 7999:
        nhif = 300
    else:
        nhif = 1700
    
    return nhif

nhif_contribution = find_nhif(gross_salary)
print(f"NHIF contribution is {nhif_contribution}.")

# TASK 16: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF. 
# Write a normal program but use functions if you feel comfortable.

# calculate nssf
def find_nssf(my_gross):
    if my_gross >= 18000:
        nssf = my_gross * 0.06
    else:
        nssf = 0
    
    return nssf

nssf_contribution = find_nssf(gross_salary)
print(f"NSSF contribution is {nssf_contribution}.")

# Task 17: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015
# Write a normal program but use functions if you feel comfortable.
def find_nhdf(my_gross):
    nhdf = my_gross * 0.015
    
    return nhdf

nhdf_contribution = find_nhdf(gross_salary)
print(f"NHDF contribution is {nhdf_contribution}.")

# Task 18: Using Python or PHP or Java or Ruby or JavaScript
# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF + NHIF) 
# Write a normal program but use functions if you feel comfortable.
def find_taxable_income(my_gross,nssf,nhdf,nhif):
    taxable_income = my_gross - (nssf + nhdf +nhif)
    
    return taxable_income

taxable_income = find_taxable_income(gross_salary,nssf_contribution,nhdf_contribution,nhif_contribution)
print(f"Taxable income is {taxable_income}.")

# TASK 19: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and find the person's PAYEE using the taxable income above.
# Find the Kenya PAYEE Tax Rate using THIS LINK
# Write a normal program but use functions if you feel comfortable.
def find_paye(taxable_income):
    if taxable_income <= 24000:
        tax = taxable_income * 0.1
    elif taxable_income > 24000 and taxable_income <= 32333:
        tax = (taxable_income - 24000) * 0.25 + 2400
    elif taxable_income > 32333 and taxable_income <= 500000:
        tax = (taxable_income - 32333) * 0.3 + 2400 + 2083.25
    elif taxable_income > 500000 and taxable_income <= 800000:
        tax = (taxable_income - 500000) * 0.325 + 2400 + 2083.25 + 140300.1
    else:
        tax = (taxable_income - 800000) * 0.35 + 2400 + 2083.25 + 140300.1 + 97500
    
    return tax

tax = find_paye(taxable_income)
print(f"Tax is {tax}.")

# Task 20: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee)
def find_net_salary(taxable_income,tax):
    net_salary = taxable_income - tax
    
    return net_salary

net_salary = find_net_salary(taxable_income,tax)
print(f"Net salary is {net_salary}.")

