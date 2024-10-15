#LTlfeF4OCuC3QR8b3GHZnJoCXdARk1GYnbCqBGC+94zbe3576rq+x6WTSywpYiLsY8RzHvQHziKAFvBFuBDBwOcBnA9yGHUjWbIg9vWcSUn6IRHmT+qMla3cX193RKlpb621fEh6Ce5oSG6wsnI+KvGzgWO+qTfzAPFDgycmF1Y0mjPmJeu0rR6lDkTcuqaNI879cjFGLvn26HUIfgJZS7eRwHvatVgfMIeYB6hLeL+7SE/MHxt6PSZkYtvOD6DvUNbAvA7r4sNEelrBDA07ytE+GjBk7rFbLu2zYkTZs12G1rBPGMkV9mKNGkILtgaN7/xUKnUosABGehqnPqvnyGopvZ1mqG26mwpPStiZhoujK7liIk8bIYQvvoWR6pV4
#Let's make a function to answer on this task
def FindNone(list_):

    #We need to find None index at first
    Missed = list_.index(None)

    #let's find sum and length of list
    summa = sum(num for num in list_ if num is not None)
    count = len(list_)-1 #count of numbers

    #Change missed number
    list_[Missed] = summa/count

    return list_

#Let's make some list
list_ = [123, 83245, 123, None, 0, 435]
print("Oringinal list is ", list_)
list_ = FindNone(list_)
print("Changed list is ", list_)
