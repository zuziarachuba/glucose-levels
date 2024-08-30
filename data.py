import csv
from datetime import datetime
today = datetime.today().strftime('%Y-%m-%d')
file_name = f"glukose_levels_{today}.csv"

fasting = int(input("What was your fasting blood glucose level today? "))
after_breakfast = int(input("Input your glucose level 2 hours after breakfast: "))
before_lunch = int(input("Input your glucose level before lunch: "))
after_lunch = int(input("Input your glucose level 2 hours after lunch: "))
before_dinner = int(input("Input your glucose level before dinner: "))
after_dinner = int(input("Input your glucose level 2 hours after dinner: "))

with open(file_name, "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Fasting", "After breakfast", "Before lunch", "After lunch", "Before dinner", "After dinner"])
    writer.writerow([fasting, after_breakfast, before_lunch, after_lunch, before_dinner, after_dinner])

print() 

print(f"Your data from today has been saved to {file_name}")

print()
print("Thank you for your data!")

print("What would you like to know? Here are your options: ")
print("- Average glucose level - write 'avg'")
print("- Time in range - write 'tir")
print("- Posibble A1C level - write 'A1C'")

choice = input()

if choice == "avg":
    avg = (fasting + after_breakfast + before_dinner + before_lunch + after_dinner + after_lunch)/6
    avg_rounded = round(avg, 1)
    print(str(avg_rounded) + "mg/dL")
elif choice == "tir":
    values = [fasting, after_breakfast, before_lunch, after_lunch, before_dinner, after_dinner]
    not_in_range = [] 

    for levels in values:
        if levels > 180:
            not_in_range.append(levels)  
        elif levels < 70:
            not_in_range.append(levels)

    print("You were out of range " + str(len(not_in_range)) + " times today")
    if len(not_in_range) < 3:
        print("You did great!")

elif choice == 'A1C':
    print("I need at least 3 days of data to predict the A1C level. ")
