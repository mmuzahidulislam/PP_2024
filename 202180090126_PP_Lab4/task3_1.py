import csv

filename = 'grades-126.csv'
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['firstname', 'lastname', 'exam1', 'exam2', 'exam3'])

# I take input only for 3 student, but it can take upto 20 student exam's result data
    for _ in range(1,21):
        print(f"Enter data for Student {_}:")
        firstname = input("First Name: ")
        lastname = input("Last Name: ")
        exam1 = int(input("Exam 01 Grade: "))
        exam2 = int(input("Exam 02 Grade: "))
        exam3 = int(input("Exam 03 Grade: "))

        writer.writerow([firstname, lastname, exam1, exam2, exam3])

print(f"Data successfully saved to {filename}.")
