#J/eYHa7B9lIwc8JRl+F+yDA8zovrbNawE7BsVnzP1AF3yXNUkNNkNkftwZYb/xmN2OS16kOsIX/AvunHJD/XcthgH+dPRcwjjAY55U93TZ0d3m7DJdH59iAVYsyOIYLdc148m8I9IfxqFrMMVJS4Yx4m+w86S78cfLf/0l8vi2LyMB7X1glgAML5GMlUMA6nDNhs5XckvfUsdKZtYjoPY8rdUnN/VG2a9er2Vc+myNZOMuRBmcvO5QMA3HmGP3g3b++l5jyPOfXSnLJnNwpu18MuV9FJ5IaaKjBvehLS9pmcHibDW2iv+xkYjQzRC4wcDXs0+Q0lwpvjkYk5G4wYP1tATKjzhY/SE8CCr5tZuU6AHG5R7HdoTEHfBwsECfJ1AHiPBiZVrfd5IQwvyhSisFO5TRs36Ee/WD3gQk8X/WkQhJ8+lxROBONvev+gAbR+VvAb5oPO1KXITjd7vw90ojmTEs03IdAX5/Gj9OtRzUtfUvmoId+A9is332dT7FpY4lP+QqLxDTt6FIEktfR7T4+lcvlavVF7mfyEZi2WJVBxYui4ZPKOUPHJ5KBEYyBrLKvJDV2uzmvG73lMPh9ZymilFnCEwVcqpMb3vly53GPI+43qbSBg1KDIeG5Tndn83EG12o1wI87h7JtkaX8g1P2y/epe9BUqLZ+VMbm3Q/sFNGB4rzZm22s6KCqMkN1SHhGWvZm9qQWr1g1/2W9zV4kAaJ98upQo1HiXovw1UNPUGQxGAUexsrQnQ7JkWZI0
def Money_capital(months_needed, salary, spend, increase):
    debt = 0 #debt without capital
    months = 0
    while True:
        months += 1
        if months == 1:
            debt = abs(salary - spend) # Spend without increase
        else:
            spend = spend + spend // 100 * increase # Increas of prices
            debt = debt + abs(salary - spend) ## Spend with increase
        capital = debt
        if months == months_needed: # End in 10 months
            break
    return capital

salary = 15000  # Salary in rub
spend = 20000   # Spent money in rub
increase = 5    # Price increase in percents
months = 10
data = [
    "Your salary is", str(salary) + " rub",
    "Your spend is", str(spend) + " rub",
    "Increase of prices is ", str(increase) + "%",
    "And you need to live", str(months)+" months without debs?\nHmm, let me think"]
print("---------------------------------")
for i, val in enumerate(data):
    if i % 2 == 0:
        print(data[i], data[i + 1])
print("---------------------------------")
print("Wow! You need more then",
      Money_capital(months, salary, spend, increase),
      " rub to live without debs",
      months, "month(s).")
print("---------------------------------")
