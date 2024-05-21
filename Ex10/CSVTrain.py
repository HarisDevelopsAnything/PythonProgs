import csv
def addTrain(details):
    with open('trains.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(details)
def findTrain(source, destination, date):
    with open('trains.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[3] == source or row[4] == destination or row[2] == date:
                print("-"*20)
                print("Train No:", row[0])
                print("Train Name:", row[1])
                print("Date:", row[2])
                print("From:", row[3])
                print("To:", row[4])
                print("Cost:", row[5])
                print("-"*20)
while True:
    print("1. Add Train Details")
    print("2. Search Train")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        tno = input("Enter Train No: ")
        tname = input("Enter Train Name: ")
        date = input("Enter Date (DD-MM-YYYY): ")
        source = input("Enter Source: ")
        destination = input("Enter Destination: ")
        cost = input("Enter Cost: ")
        details = [tno, tname, date, source, destination, cost]
        addTrain(details)
        print("Train details added successfully!\n")
    elif choice == '2':
        ch = input("Search by:\n1. Source and Destination\n2. Date\nEnter your choice: ")
        if ch == '1':
            source = input("Enter Source: ")
            destination = input("Enter Destination: ")
            findTrain(source, destination, "")
        elif ch == '2':
            date = input("Enter Date (DD-MM-YYYY): ")
            findTrain("", "", date)
        else:
            print("Invalid choice!\n")
    elif choice == '3':
        print("Exiting program...")
        break
    else:
        print("Invalid choice!\n")