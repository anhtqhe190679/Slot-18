class Student:
    id_counter = 1

    def __init__(self, name, gender, age, math_score, physics_score, chemistry_score):
        self.id = Student.id_counter
        self.name = name
        self.gender = gender
        self.age = age
        self.math_score = math_score
        self.physics_score = physics_score
        self.chemistry_score = chemistry_score
        self.average_score = (math_score + physics_score + chemistry_score) / 3
        self.academic_performance = self.calculate_academic_performance()
        Student.id_counter += 1

    def calculate_academic_performance(self):
        if self.average_score >= 8:
            return "Giỏi"
        elif 6.5 <= self.average_score < 8:
            return "Khá"
        elif 5 <= self.average_score < 6.5:
            return "Trung Bình"
        else:
            return "Yếu"

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def update_student(self, student_id, **kwargs):
        for student in self.students:
            if student.id == student_id:
                for key, value in kwargs.items():
                    setattr(student, key, value)
                student.average_score = (student.math_score + student.physics_score + student.chemistry_score) / 3
                student.academic_performance = student.calculate_academic_performance()
                return True
        return False

    def delete_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                return True
        return False

    def search_student_by_name(self, name):
        found_students = []
        for student in self.students:
            if student.name.lower() == name.lower():
                found_students.append(student)
        return found_students

    def sort_students_by_gpa(self):
        return sorted(self.students, key=lambda x: x.average_score, reverse=True)

    def sort_students_by_name(self):
        return sorted(self.students, key=lambda x: x.name)

    def sort_students_by_id(self):
        return sorted(self.students, key=lambda x: x.id)

    def display_students(self):
        for student in self.students:
            print(f"ID: {student.id}, Name: {student.name}, Gender: {student.gender}, Age: {student.age}, "
                  f"Math Score: {student.math_score}, Physics Score: {student.physics_score}, "
                  f"Chemistry Score: {student.chemistry_score}, Average Score: {student.average_score}, "
                  f"Academic Performance: {student.academic_performance}")


def menu():
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Update Student Information by ID")
    print("3. Delete Student by ID")
    print("4. Search Student by Name")
    print("5. Sort Students by GPA")
    print("6. Sort Students by Name")
    print("7. Sort Students by ID")
    print("8. Display Student List")
    print("9. Exit")
    choice = input("Enter your choice: ")
    return choice


def main():
    student_manager = StudentManager()

    while True:
        choice = menu()
        if choice == "1":
            name = input("Enter student name: ")
            gender = input("Enter student gender: ")
            age = int(input("Enter student age: "))
            math_score = float(input("Enter math score: "))
            physics_score = float(input("Enter physics score: "))
            chemistry_score = float(input("Enter chemistry score: "))
            student = Student(name, gender, age, math_score, physics_score, chemistry_score)
            student_manager.add_student(student)
            print("Student added successfully.")
        elif choice == "2":
            student_id = int(input("Enter student ID to update: "))
            attribute = input("Enter attribute to update (name, gender, age, math_score, physics_score, "
                              "chemistry_score): ")
            new_value = input("Enter new value: ")
            if student_manager.update_student(student_id, **{attribute: new_value}):
                print("Student information updated successfully.")
            else:
                print("Student not found.")
        elif choice == "3":
            student_id = int(input("Enter student ID to delete: "))
            if student_manager.delete_student(student_id):
                print("Student deleted successfully.")
            else:
                print("Student not found.")
        elif choice == "4":
            name = input("Enter student name to search: ")
            found_students = student_manager.search_student_by_name(name)
            if found_students:
                print("Found students:")
                for student in found_students:
                    print(f"ID: {student.id}, Name: {student.name}")
            else:
                print("No student found with that name.")
        elif choice == "5":
            sorted_students = student_manager.sort_students_by_gpa()
            print("Sorted Students by GPA:")
            student_manager.display_students()
        elif choice == "6":
            sorted_students = student_manager.sort_students_by_name()
            print("Sorted Students by Name:")
            student_manager.display_students()
        elif choice == "7":
            sorted_students = student_manager.sort_students_by_id()
            print("Sorted Students by ID:")
            student_manager.display_students()
        elif choice == "8":
            print("Student List:")
            student_manager.display_students()
        elif choice == "9":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
