input = input("This is a place where you can monitor your blood sugar levels everyday. \nThis program will collect your data, and give you your average blood glucose level, and after 3 days - posibble A1C level. \nIf you don't know where to start, write 'help' ")
if input == "help":
    print("Enter your blood glucose levels daily. You can check your average glucose level, time in range, and after 3 days, view your predicted A1C level — a crucial measure in diabetes management.")
else:
    print("Let's get started! ")