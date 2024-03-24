# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this

monthly_expense: list[list[float]] = [["January","Feb","March","April","May"],[2200, 2350, 2600, 2130, 2190]]
print(f"In Feb you spent {monthly_expense[1][1] - monthly_expense[1][0]}$ more than Jan") if monthly_expense[1][1] > monthly_expense[1][0] else print("In Feb your expense was lower than January")

expense_first_quarter = monthly_expense[1][0] + monthly_expense[1][1] + monthly_expense[1][2]
print(f"First quarter expense was {expense_first_quarter}$")

print(f"You have spent 2000 in some month") if 2000 in monthly_expense[1] else print("You haven't spent exactly 2000 in any month")

monthly_expense[0].append("June")
monthly_expense[1].append(1980)
print(f"Updated Expense {monthly_expense}")

monthly_expense[1][3] -= 200
print(f"Your expense in april month was {monthly_expense[1][3]}")


# You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros=['spider man','thor','hulk','iron man','captain america']
print(f"Length of Hero List is {len(heros)}")

heros.append("black panther")
print(f"Updated List is {heros}")

heros.pop()
heros.insert(3, "black panther")
print(f"Updated List is {heros}")

heros[1:3] = ["doctor strange"]
print(f"Updated List is {heros}")

heros.sort()
print(f"Updated List is {heros}")

try:
    userInput = int(input("Please enter number: "))
except:
    print("Invalid Input")
else:
    odd_numbers = [i for i in range(userInput+1) if i % 2 != 0]
    print(f"Odd Numbers are {odd_numbers}")