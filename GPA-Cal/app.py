import tkinter as tk
from tkinter import messagebox, ttk

class GPACalculator:
    def __init__(self):
        self.semesters = {semester: [] for semester in range(1, 9)}
        self.grade_point_mapping = {
            "A+": 4.0,
            "A": 4.0,
            "A-": 3.7,
            "B+": 3.3,
            "B": 3.0,
            "B-": 2.7,
            "C+": 2.3,
            "C": 2.0,
            "C-": 1.7,
            "D+": 1.3,
            "D": 1.0,
            "E": 0.0
        }

    def add_course(self, semester, subject, grade, credit):
        if semester not in self.semesters:
            return f"Invalid semester '{semester}'. Please choose a semester between 1 and 8."

        if len(self.semesters[semester]) >= 10:
            return f"Semester {semester} already has 10 courses. No more courses can be added."

        if grade.upper() not in self.grade_point_mapping:
            return f"Invalid grade '{grade}'. Please use a valid grade (e.g., A+, A, A-, B+, etc.)."

        try:
            credit = float(credit)
            if credit <= 0:
                return "Credit hours must be a positive number."

            self.semesters[semester].append({
                "subject": subject,
                "grade": grade.upper(),
                "credit": credit
            })
            return "Course added successfully."
        except ValueError:
            return "Invalid credit value. Please enter a valid number."

    def calculate_gpa(self):
        total_points = 0
        total_credits = 0

        for semester in self.semesters.values():
            for course in semester:
                grade_point = self.grade_point_mapping[course["grade"]]
                credit = course["credit"]

                total_points += grade_point * credit
                total_credits += credit

        if total_credits == 0:
            return 0.0

        return total_points / total_credits

    def display_courses(self):
        result = "Courses by Semester:\n"
        for semester, courses in self.semesters.items():
            result += f"Semester {semester}:\n"
            if not courses:
                result += "  No courses added.\n"
            for course in courses:
                result += f"  {course['subject']} - Grade: {course['grade']}, Credit: {course['credit']}\n"
        return result

class GPAApp:
    def __init__(self, root):
        self.calculator = GPACalculator()
        self.root = root
        self.root.title("GPA Calculator")
        self.root.geometry("385x340")  # Adjust the window size to better fit the content

        # Semester Input
        tk.Label(root, text="Semester (1-8):", font=("Arial", 12)).grid(row=0, column=0, padx=15, pady=15, sticky="w")
        self.semester_entry = tk.Entry(root, font=("Arial", 12))
        self.semester_entry.grid(row=0, column=1, padx=15, pady=15, sticky="w")

        # Subject Input
        tk.Label(root, text="Subject:", font=("Arial", 12)).grid(row=1, column=0, padx=15, pady=15, sticky="w")
        self.subject_entry = tk.Entry(root, font=("Arial", 12))
        self.subject_entry.grid(row=1, column=1, padx=15, pady=15, sticky="w")

        # Grade Input
        tk.Label(root, text="Grade:", font=("Arial", 12)).grid(row=2, column=0, padx=15, pady=15, sticky="w")
        self.grade_combobox = ttk.Combobox(root, values=["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "E"], state="readonly", font=("Arial", 12))
        self.grade_combobox.grid(row=2, column=1, padx=15, pady=15, sticky="w")

        # Credit Input
        tk.Label(root, text="No. of Credits:", font=("Arial", 12)).grid(row=3, column=0, padx=15, pady=15, sticky="w")
        self.credit_entry = tk.Entry(root, font=("Arial", 12))
        self.credit_entry.grid(row=3, column=1, padx=15, pady=15, sticky="w")

        # Buttons
        tk.Button(root, text="Add Module", command=self.add_course, font=("Arial", 12)).grid(row=4, column=0, padx=15, pady=15, sticky="w")
        tk.Button(root, text="Calculate GPA", command=self.calculate_gpa, font=("Arial", 12)).grid(row=4, column=1, padx=105, pady=15, sticky="w")
        tk.Button(root, text="Summary", command=self.view_courses, font=("Arial", 12)).grid(row=5, column=0, columnspan=2, padx=(15, 110), pady=15)

    def add_course(self):
        try:
            semester = int(self.semester_entry.get())
            subject = self.subject_entry.get()
            grade = self.grade_combobox.get()
            credit = self.credit_entry.get()

            message = self.calculator.add_course(semester, subject, grade, credit)
            messagebox.showinfo("Add Course", message)
        except ValueError:
            messagebox.showerror("Error", "Invalid semester. Please enter a number between 1 and 8.")

    def calculate_gpa(self):
        gpa = self.calculator.calculate_gpa()
        messagebox.showinfo("GPA", f"Your cumulative GPA is: {gpa:.2f}")

    def view_courses(self):
        courses = self.calculator.display_courses()
        messagebox.showinfo("Courses", courses)

if __name__ == "__main__":
    root = tk.Tk()
    app = GPAApp(root)
    root.mainloop()
