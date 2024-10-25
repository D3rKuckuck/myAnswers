#xwnpebHkCcoc5xqaH5kq/4iC0t6KFuGy6tYdos+r73QF2h5KGzYOleUl9/dH5E4KPwC3lZ4ygCt6t6eKjDx5v246AihZC6eyTZK3PgVb+vaNLe6qNSg8G2Cmuk27RIeWZf5thBONXkT3geQ8fh6o7wPqhtA0CsUwnr4T9FeZZf7U6r6ry03v18acoMAjYqAbVzrelQ74dx00ajSlRp4ur4xsq4YXHxuO9Bh3XnWGAzqbCpuq8l9uB+bxzs5Q9cN4LnoL6DBdRXnp4vZXL6PeY8brKpsZpJHUmkzRDXVpteCp5WKXHHVVqazbqS0SXcTKorXqh5D+M0H8Vl2BvEfHs9JdbPkfc+7ofR6mXGf5o/1xq6/ipqs8IX+x4jFRgoVLrabrWF42ewdjIBbGuw+xFFOgzYPWGlwGiAgp7rO4jYs2I+QR56IRLKC/NuzG3GszF1GGKNTkukoK9qsoqudPofrqu5Kyq05YgRESQjTs2+p803L/XfVEeL7QHKk3NiViCvaACuV5e3QOkmFEFUJPoHypCozt5jA7OihQDYOd7kT820+urGI4yPSQHys3E7TDEWN+Ztvt5szOsehDc6NCWT79EPzZImQHW83sAqv8yQioa8XYZcR9HJYvP5H+6GMZkbEnezvw+cyp6pnu87pY8g==

def months_without_debts(capital, salary, spend, increase):
    rest = 0 # rest of money
    months = 0 # months without debs
    while True:
        if spend > capital + salary: # Criterion of the life without debs
            break
        months += 1
        if months == 1:
            rest = capital + salary - spend # Spend without increase
            if spend > salary:
                capital = capital - abs(salary - spend) # Reduction of capital
        else:
            spend = spend + spend // 100 * increase # Increas of prices
            rest = capital + salary - spend ## Spend with increase
            if spend > salary:
                capital = capital - abs(salary - spend) # Reduction of capital
    return months

money_capital = 60000   # Capital pillow in rub
salary = 15000  # Salary in rub
spend = 20000   # Spent money in rub
increase = 5    # Price increase in percents
data = [
    "Money capital is ", str(money_capital) + " rub",
    "Your salary is ", str(salary) + " rub",
    "Your spend is ", str(spend) + " rub",
    "Increase of prices is ", str(increase) + "%"]

for i, val in enumerate(data):
    if i % 2 == 0:
        print(data[i], data[i + 1])

print("You can live ",
      months_without_debts(money_capital, salary, spend, increase),
      " month(s) without debs. Good!")

