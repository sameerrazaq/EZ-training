#!/usr/bin/env python
# coding: utf-8

# In[4]:





# In[ ]:


class SportsEquipment:
    def _init_(self, equipment_id, name, quantity, condition="Good"):
        self.equipment_id = equipment_id
        self.name = name
        self.quantity = quantity
        self.condition = condition

class Student:
    def _init_(self, usn, name, id):
        self.usn = usn
        self.name = name
        self.id = id

class EquipmentRentalSystem:
    def _init_(self):
        self.equipment_list = []
        self.students = {}

    def add_student(self, usn, name, id):
        self.students[usn] = Student(usn, name, id)
        print(f"Student {name} added successfully.")

    def add_equipment(self, equipment_id, name, quantity, condition="Good"):
        self.equipment_list.append(SportsEquipment(equipment_id, name, quantity, condition))
        print(f"{name} added to the inventory.")

    def rent_sports_equipment(self, equipment_id, usn):
        student = self.students.get(usn)
        if student:
            for equipment in self.equipment_list:
                if equipment.equipment_id == equipment_id:
                    if equipment.quantity > 0:
                        equipment.quantity -= 1
                        print(f"{equipment.name} rented successfully by {student.name}.")
                    else:
                        print("Sorry, this equipment is currently out of stock.")
                    return
            print("Equipment not found.")
        else:
            print("Student not found.")

    def track_equipment_return(self, return_id):
        for equipment in self.equipment_list:
            if equipment.equipment_id == return_id:
                equipment.quantity += 1
                equipment.condition = input("Enter the condition of the returned equipment: ")
                print(f"{equipment.name} returned successfully.")
                return
        print("Equipment not found.")

    def display_inventory(self):
        print("Current Inventory:")
        for equipment in self.equipment_list:
            print(f"ID: {equipment.equipment_id}, Name: {equipment.name}, Quantity: {equipment.quantity}, Condition: {equipment.condition}")

    def display_students(self):
        print("Registered Students:")
        for student in self.students.values():
            print(f"USN: {student.usn}, Name: {student.name}, ID: {student.id}")


# Main program
if __name__ == "__main__":
    rental_system = EquipmentRentalSystem()

    while True:
        print("\nOptions:")
        print("1. Add Student")
        print("2. Add Equipment")
        print("3. Rent Equipment")
        print("4. Return Equipment")
        print("5. Display Inventory")
        print("6. Display Students")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            usn = input("Enter student USN: ")
            name = input("Enter student name: ")
            id = input("Enter student ID: ")
            rental_system.add_student(usn, name, id)

        elif choice == "2":
            equipment_id = input("Enter equipment ID: ")
            name = input("Enter equipment name: ")
            quantity = int(input("Enter quantity: "))
            rental_system.add_equipment(equipment_id, name, quantity)

        elif choice == "3":
            equipment_id = input("Enter equipment ID to rent: ")
            usn = input("Enter student USN: ")
            rental_system.rent_sports_equipment(equipment_id, usn)

        elif choice == "4":
            return_id = input("Enter equipment ID to return: ")
            rental_system.track_equipment_return(return_id)

        elif choice == "5":
            rental_system.display_inventory()

        elif choice == "6":
            rental_system.display_students()

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


# In[ ]:


import json

class SportsEquipment:
    def __init__(self, equipment_id, name, quantity, condition="Good"):
        self.equipment_id = equipment_id
        self.name = name
        self.quantity = quantity
        self.condition = condition

    def to_dict(self):
        return {
            "equipment_id": self.equipment_id,
            "name": self.name,
            "quantity": self.quantity,
            "condition": self.condition
        }

    @staticmethod
    def from_dict(data):
        return SportsEquipment(data["equipment_id"], data["name"], data["quantity"], data["condition"])


class Student:
    def __init__(self, usn, name, id):
        self.usn = usn
        self.name = name
        self.id = id

    def to_dict(self):
        return {
            "usn": self.usn,
            "name": self.name,
            "id": self.id
        }

    @staticmethod
    def from_dict(data):
        return Student(data["usn"], data["name"], data["id"])


class EquipmentRentalSystem:
    def __init__(self):
        self.equipment_list = []
        self.students = {}
        self.load_data()

    def add_student(self, usn, name, id):
        self.students[usn] = Student(usn, name, id)
        self.save_data()
        print(f"Student {name} added successfully.")

    def add_equipment(self, equipment_id, name, quantity, condition="Good"):
        self.equipment_list.append(SportsEquipment(equipment_id, name, quantity, condition))
        self.save_data()
        print(f"{name} added to the inventory.")

    def rent_sports_equipment(self, equipment_id, usn):
        student = self.students.get(usn)
        if student:
            for equipment in self.equipment_list:
                if equipment.equipment_id == equipment_id:
                    if equipment.quantity > 0:
                        equipment.quantity -= 1
                        self.save_data()
                        print(f"{equipment.name} rented successfully by {student.name}.")
                    else:
                        print("Sorry, this equipment is currently out of stock.")
                    return
            print("Equipment not found.")
        else:
            print("Student not found.")

    def track_equipment_return(self, return_id):
        for equipment in self.equipment_list:
            if equipment.equipment_id == return_id:
                equipment.quantity += 1
                equipment.condition = input("Enter the condition of the returned equipment: ")
                self.save_data()
                print(f"{equipment.name} returned successfully.")
                return
        print("Equipment not found.")

    def display_inventory(self):
        print("Current Inventory:")
        for equipment in self.equipment_list:
            print(f"ID: {equipment.equipment_id}, Name: {equipment.name}, Quantity: {equipment.quantity}, Condition: {equipment.condition}")

    def display_students(self):
        print("Registered Students:")
        for student in self.students.values():
            print(f"USN: {student.usn}, Name: {student.name}, ID: {student.id}")

    def save_data(self):
        with open("equipment_data.json", "w") as equipment_file:
            json.dump([equipment.to_dict() for equipment in self.equipment_list], equipment_file)
        with open("students_data.json", "w") as students_file:
            json.dump({usn: student.to_dict() for usn, student in self.students.items()}, students_file)

    def load_data(self):
        try:
            with open("equipment_data.json", "r") as equipment_file:
                equipment_data = json.load(equipment_file)
                self.equipment_list = [SportsEquipment.from_dict(e) for e in equipment_data]
        except FileNotFoundError:
            self.equipment_list = []

        try:
            with open("students_data.json", "r") as students_file:
                students_data = json.load(students_file)
                self.students = {usn: Student.from_dict(s) for usn, s in students_data.items()}
        except FileNotFoundError:
            self.students = {}


# Main program
if __name__ == "__main__":
    rental_system = EquipmentRentalSystem()

    while True:
        print("\nOptions:")
        print("1. Add Student")
        print("2. Add Equipment")
        print("3. Rent Equipment")
        print("4. Return Equipment")
        print("5. Display Inventory")
        print("6. Display Students")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            usn = input("Enter student USN: ")
            name = input("Enter student name: ")
            id = input("Enter student ID: ")
            rental_system.add_student(usn, name, id)

        elif choice == "2":
            equipment_id = input("Enter equipment ID: ")
            name = input("Enter equipment name: ")
            quantity = int(input("Enter quantity: "))
            rental_system.add_equipment(equipment_id, name, quantity)

        elif choice == "3":
            equipment_id = input("Enter equipment ID to rent: ")
            usn = input("Enter student USN: ")
            rental_system.rent_sports_equipment(equipment_id, usn)

        elif choice == "4":
            return_id = input("Enter equipment ID to return: ")
            rental_system.track_equipment_return(return_id)

        elif choice == "5":
            rental_system.display_inventory()

        elif choice == "6":
            rental_system.display_students()

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


# In[ ]:


class EV:
    def __init__(self, candidates):
        self.candidates = candidates
        self.votes = {candidate: [] for candidate in candidates}
        
    def cast_vote(self, voter_id, candidate):
        if candidate in self.votes:
            self.votes[candidate].append(voter_id)
            print(f"Vote cast successfully for {candidate}.")
        else:
            print("Invalid candidate.")
    
    def count_votes(self):
        vote_count = {candidate: len(voters) for candidate, voters in self.votes.items()}
        return vote_count
    
    def find_winner(self):
        vote_count = self.count_votes()
        max_votes = max(vote_count.values())
        winners = [candidate for candidate, votes in vote_count.items() if votes == max_votes]
        
        if len(winners) > 1:
            print("It's a tie between:", ", ".join(winners))
        else:
            print(f"The winner is: {winners[0]}")
        return winners
if __name__ == "__main__":
    candidates = ["sam", "abhi", "goutham"]
    evm = EV(candidates)
    
    while True:
        print("\nOptions:")
        print("1. Cast Vote")
        print("2. Count Votes")
        print("3. Find Winner")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            voter_id = input("Enter your voter ID: ")
            candidate = input("Enter the candidate's name: ")
            evm.cast_vote(voter_id, candidate)
        
        elif choice == "2":
            vote_count = evm.count_votes()
            print("Current Vote Count:")
            for candidate, votes in vote_count.items():
                print(f"{candidate}: {votes} votes")
        
        elif choice == "3":
            evm.find_winner()
        
        elif choice == "4":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")


# In[ ]:


class EV:
    def __init__(self, candidates):
        self.candidates = candidates
        self.votes = {candidate: [] for candidate in candidates}
        
    def cast_vote(self, voter_id, candidate):
        if candidate in self.candidates:
            self.votes[candidate].append(voter_id)
            print(f"Vote cast successfully for {candidate}.")
        else:
            print("Invalid candidate.")
    
    def count_votes(self):
        vote_count = {candidate: len(voters) for candidate, voters in self.votes.items()}
        return vote_count
    
    def find_winner(self):
        vote_count = self.count_votes()
        max_votes = max(vote_count.values())
        winners = [candidate for candidate, votes in vote_count.items() if votes == max_votes]
        
        if len(winners) > 1:
            print("It's a tie between:", ", ".join(winners))
        else:
            print(f"The winner is: {winners[0]}")
        return winners
if __name__ == "__main_":
    candidates = ["Sam", "Abhi", "Goutham"]
    evm = EV(candidates)
    
    while True:
        print("\nOptions:")
        print("1. Cast Vote")
        print("2. Count Votes")
        print("3. Find Winner")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            voter_id = input("Enter your voter ID: ")
            candidate = input("Enter the candidate's name: ")
            evm.cast_vote(voter_id, candidate)
        
        elif choice == "2":
            vote_count = evm.count_votes()
            print("Current Vote Count:")
            for candidate, votes in vote_count.items():
                print(f"{candidate}: {votes} votes")
        
        elif choice == "3":
            evm.find_winner()
        
        elif choice == "4":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")


# In[ ]:


class EV:
    def __init__(self, candidates):
        self.candidates = candidates
        self.votes = {candidate: [] for candidate in candidates}
        
    def cast_vote(self, voter_id, candidate):
        if candidate in self.candidates:
            self.votes[candidate].append(voter_id)
            print(f"Vote cast successfully for {candidate}.")
        else:
            print("Invalid candidate.")
    
    def count_votes(self):
        vote_count = {candidate: len(voters) for candidate, voters in self.votes.items()}
        return vote_count
    
    def find_winner(self):
        vote_count = self.count_votes()
        max_votes = max(vote_count.values())
        winners = [candidate for candidate, votes in vote_count.items() if votes == max_votes]


# In[ ]:


nocan=5
novot=5
dict={
    1:1,
    2:2,
    3:3,
    4:4,
    5:5
}

def candidates():
    print("1->BJP\n2->Congress\n3->Jantadal\n4->Samajwadi party\n5->RSS")
def evm():
    candidate()
    v=int(print("Enter the party number to vote"))
    if n not in dict:
        print("Sorry wrong party number")
        


# In[ ]:


vote= list(map(int, input("Enter the vote").split(" ")))
count = [0]*6 

for i in vote:
    count[i-1]=count[i-1]+1
    print(i,count)
print("Final count = " , count)


# In[ ]:


votes = list(map(int, input("Enter the votes (space-separated): ").split()))

count = [0] * 6

for vote in votes:
    if 1 <= vote <= 6:
        count[vote - 1] += 1
    else:
        print(f"Invalid vote: {vote}")
for i in range(6):
    print(f"Candidate {i + 1}: {count[i]} votes")
max_votes = max(count)
winners = [i + 1 for i, votes in enumerate(count) if votes == max_votes]
print("Final count =", count)
if len(winners) > 1:
    print("It's a tie between candidates:", ", ".join(map(str, winners)))
else:
    print(f"The winner is candidate {winners[0]}")


# In[ ]:


def min_key_presses(s):
    target = int(s)
    current_number = 0
    presses = 0

    while current_number != target:
        if current_number * 100 <= target:
            current_number *= 100
            presses += 1
        else:
            digit = int(s[len(str(current_number))])
            current_number = current_number * 10 + digit
            presses += 1

    return presses

# Example usage:
s = "543210"
print(min_key_presses(s))  # Output: 3


# In[ ]:


text = """Hello! My name is Sameer.
currently I'm pursuing my engineering in BITM Bellary."""
with open("sameer.txt", "w") as file:
    file.write(text)

print("Introduction written to sameer.txt\n")
with open("sameer.txt", 'r') as f:
    print("Initial content of the file:")
    print(f.read())
text = text.replace("Bellary", "Ballari")
with open("sameer.txt", "w") as file:
    file.write(text)
with open("sameer.txt", 'r') as f:
    print("Updated content of the file:")
    print(f.read())


# In[ ]:


class int:
    if sys.version_info ›= (3, 12):
        def is_ integer(self) -› Literal[True]: ...
            def_add
_(self, value: int, /) -› int: ...
def
-sub
_(self, value: int, /) -› int: 1..
def
(self, value: int, /) -> int: ...
def
floordiv_(self, value: int, /) -› int: ...
def
truediv_(self, value: int, /) -> float: ...
def
_mod
(self, value: int, /) -› int: ...
def
divmod (self. value: int. /) -> tuplefint. intl:


# In[3]:


class Student:
    def __init__(self, name, usn, marks):
        self.name = name
        self.usn = usn
        self.marks = marks
        self.percentage = 0
        self.grade = ''
    
    def calculate_percentage(self):
        total_marks = sum(self.marks)
        self.percentage = (total_marks / 500) * 100
    
    def calculate_grade(self):
        if self.percentage >= 90:
            self.grade = 'A+'
        elif 80 <= self.percentage < 90:
            self.grade = 'A'
        elif 70 <= self.percentage < 80:
            self.grade = 'B'
        elif 60 <= self.percentage < 70:
            self.grade = 'C'
        elif 50 <= self.percentage < 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

# Create 5 student objects
students = []
for i in range(5):
    print(f"\nEnter details for Student {i+1}:")
    name = input("Enter student's name: ")
    usn = input("Enter student's USN: ")
    marks = []
    print(f"Enter marks for {name}: ")
    for j in range(5):
        while True:
            subject_marks = int(input(f"Enter marks for subject {j+1}: "))
            if subject_marks <= 100:
                break
            else:
                print("Marks should be maximum 100. Please enter again.")
        marks.append(subject_marks)
    student = Student(name, usn, marks)
    student.calculate_percentage()
    student.calculate_grade()
    students.append(student)

# Displaying data for each student
print("\nStudent Details:")
for student in students:
    print("\nStudent Name:", student.name)
    print("USN:", student.usn)
    print("Marks:", student.marks)
    print("Percentage:", student.percentage)
    print("Grade:", student.grade)


# In[4]:


class A:
    def __init__(self,name,age):
        self.name= name
        self.age = age
    def display(self):
        print(f"name:{self.name} and age:{self.age}")

class B(A):
    def __init__(self,name,age,sem):
        super().__init__(name,age)
        self.sem = sem
    def display(self):
        super().display()
        print(f"sem:{self.sem}")
b=B('sameer',20,6)
b.display()


# In[ ]:




