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

    def add_course(self, semester, subject, grade):
        if semester not in self.semesters:
            return f"Invalid semester '{semester}'. Please choose a semester between 1 and 8."

        if len(self.semesters[semester]) >= 10:
            return f"Semester {semester} already has 10 courses. No more courses can be added."

        if grade.upper() not in self.grade_point_mapping:
            return f"Invalid grade '{grade}'. Please use a valid grade (e.g., A+, A, A-, B+, etc.)."

        self.semesters[semester].append({
            "subject": subject,
            "grade": grade.upper(),
        })
        return "Course added successfully."

    def calculate_gpa(self):
        total_points = 0
        total_credits = 0

        for semester in self.semesters.values():
            for course in semester:
                grade_point = self.grade_point_mapping[course["grade"]]
                total_points += grade_point
                total_credits += 1  # each course has a default credit of 1

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
                result += f"  {course['subject']} - Grade: {course['grade']}\n"
        return result


class GPAApp:
    def __init__(self, root):
        self.calculator = GPACalculator()
        self.root = root
        self.root.title("GPA Calculator")
        self.root.geometry("600x450")  # Adjusted to fit more content

        # Semester Input
        tk.Label(root, text="Semester (1-8):", font=("Arial", 12)).grid(row=0, column=0, padx=15, pady=15, sticky="w")
        self.semester_entry = tk.Entry(root, font=("Arial", 12))
        self.semester_entry.grid(row=0, column=1, padx=5, pady=15, sticky="w")

        # 10 Input Fields for Modules and Dropdowns for Grades
        self.module_entries = []
        self.grade_comboboxes = []

        for i in range(10):
            tk.Label(root, text=f"Module {i + 1}:", font=("Arial", 12)).grid(row=3 + i, column=0, padx=15, pady=5, sticky="w")
            module_entry = tk.Entry(root, font=("Arial", 12))
            module_entry.grid(row=3 + i, column=1, padx=15, pady=5, sticky="w")
            self.module_entries.append(module_entry)

            grade_combobox = ttk.Combobox(root,
                                          values=["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "E"],
                                          state="readonly", font=("Arial", 12))
            grade_combobox.grid(row=3 + i, column=2, padx=15, pady=5, sticky="w")
            self.grade_comboboxes.append(grade_combobox)

        # Buttons arranged in one row
        tk.Button(root, text="Add Course", command=self.add_course, font=("Arial", 12)).grid(row=13, column=0, padx=15, pady=15, sticky="w")
        tk.Button(root, text="Calculate GPA", command=self.calculate_gpa, font=("Arial", 12)).grid(row=13, column=1, padx=15, pady=15, sticky="w")
        tk.Button(root, text="View Courses", command=self.view_courses, font=("Arial", 12)).grid(row=13, column=2, padx=15, pady=15, sticky="w")

    def add_course(self):
        try:
            semester = int(self.semester_entry.get())

            for i in range(10):
                module = self.module_entries[i].get()
                grade = self.grade_comboboxes[i].get()

                if module and grade:
                    message = self.calculator.add_course(semester, module, grade)
                    messagebox.showinfo("Add Course", message)
                elif module or grade:
                    messagebox.showerror("Error", f"Please fill both module and grade for Module {i + 1}")
                    return

            # Optionally clear the inputs after adding the course
            self.semester_entry.delete(0, tk.END)
            for entry in self.module_entries:
                entry.delete(0, tk.END)
            for combobox in self.grade_comboboxes:
                combobox.set('')

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
