import csv
import os
from datetime import datetime
today = datetime.today().strftime('%Y-%m-%d')
file_name = f"glukose_levels_{today}.csv"

fasting = int(input("What was your fasting blood glucose level today? "))
after_breakfast = int(input("Input your glucose level 2 hours after breakfast: "))
before_lunch = int(input("Input your glucose level before lunch: "))
after_lunch = int(input("Input your glucose level 2 hours after lunch: "))
before_dinner = int(input("Input your glucose level before dinner: "))
after_dinner = int(input("Input your glucose level 2 hours after dinner: "))

print() 
print(f"Your data from today has been saved to {file_name}")

def get_latest_files():
    files = [f for f in os.listdir() if f.startswith('glukose_levels_') and f.endswith('.csv')]
    files.sort(reverse=True)
    return files[:3]

def calculate_avg(file_name):
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        next(reader)
        row = next(reader)
        values = [int(value) for value in row]
        return sum(values)/len(values)


with open(file_name, "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Fasting", "After breakfast", "Before lunch", "After lunch", "Before dinner", "After dinner"])
    writer.writerow([fasting, after_breakfast, before_lunch, after_lunch, before_dinner, after_dinner])

choice = "null"


print()
print("- Average glucose level - write 'avg'")
print("- Time in range - write 'tir")
print("- Posibble A1C level - write 'a1c'")
print(" - Exit program - write 'exit'")


# possible_choices = {
#     'avg': fun,
#     'exit': exit
# }


# user_input = 'avg'
# possible_choices[user_input]()

while choice != "exit":
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

    elif choice == 'a1c':
        latest_files = get_latest_files()
        if len(latest_files) < 3:
            print("Not enough data. You need data from at least 3 days")
        else:
            averages = [calculate_avg(file) for file in latest_files]
            three_days_avg = sum(averages)/len(averages)
            a1c = (int(three_days_avg) + 46.7)/28.7
            a1c_rounded = round(a1c, 1)
            print("Your A1C level is: " + str(a1c_rounded) + "%")
            print()
            if a1c_rounded < 5.7:
                print("Your A1C level is normal")
            if a1c_rounded > 5.7 and a1c_rounded < 6.4:
                print("Consider action")
            else:
                print("You should see a doctor")
    
    choice = input("What would you like to know?: ")

        
