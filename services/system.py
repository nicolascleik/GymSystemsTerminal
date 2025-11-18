from models.student import Student
from models.reservation import Reservation
from services.persistence import save_data, load_data

# GymSystemsTerminal - manages objects from previous classes

class GymSystemsTerminal:
    """
    Main class that manages all gym operations.
    Manages Student and Reservation objects and applies business rules.
    """

    def __init__(self):
        """
        Constructor. Loads saved data (students and reservations) from .txt files when starting the system.
        """
        self.students, self.reservations = load_data()
        print(f"[Info] System started. {len(self.students)} students and {len(self.reservations)} reservations loaded.")

    def _auto_save(self):
        """
        Private helper method. Calls the persistence function
        to save the current state of student and reservation lists.
        """
        save_data(self.students, self.reservations)

    def register_student(self, name, cpf, age, plan):
        """
        Registers a new student in the system.
        Includes validation to prevent duplicate CPFs/IDs.

        Args:
            name (str): Student's name.
            cpf (str): Student's CPF/ID.
            age (int): Student's age.
            plan (str): Student's plan.

        Returns:
            Student: The created Student object, or None if registration fails.
        """

        if self.find_student_by_cpf(cpf):
            print(f"\n[Error] A student with CPF/ID {cpf} is already registered.")
            return None

        if not name or not cpf or age <= 0:
            print("\n[Error] Invalid student data (Name, CPF/ID or Age).")
            return None

        new_student = Student(name, cpf, age, plan)
        self.students.append(new_student)

        self._auto_save()
        print(f"\n[Success] Student '{name}' registered.")
        return new_student

    def find_student_by_cpf(self, cpf):
        """Finds a student in the list by CPF/ID."""
        for student in self.students:
            if student.cpf == cpf:
                return student
        return None

    def add_reservation(self, student_cpf, activity, date, time):
        """Creates a new Reservation and adds it to the list."""

        found_student = self.find_student_by_cpf(student_cpf)

        if not found_student:
            print(f"\n[Error] Student with CPF/ID {student_cpf} not found. Reservation not made.")
            return None

        if not activity or not date or not time:
            print(f"\n[Error] Invalid reservation data (Activity, Date or Time).")
            return None

        new_reservation = Reservation(found_student, activity, date, time)
        self.reservations.append(new_reservation)

        self._auto_save()

        print(f"\n[Success] Reservation for '{activity}' under '{found_student.name}' made.")
        return new_reservation

    def list_reservations(self):
        """Returns the list of all registered reservations."""
        return self.reservations

    def search_reservations_by_cpf(self, cpf):
        """Returns all reservations for a specific student."""
        student_reservations = []
        for res in self.reservations:
            if res.student.cpf == cpf:
                student_reservations.append(res)
        return student_reservations

    def update_reservation_status(self, reservation: Reservation, new_status: str):
        """Updates the status of a Reservation object."""
        valid_statuses = ["Reserved", "Confirmed", "Completed", "Cancelled"]

        if new_status in valid_statuses:
            reservation.status = new_status
            self._auto_save()
            print(
                f"\n[Success] Reservation status ({reservation.activity} on {reservation.date}) updated to '{new_status}'.")
            return True
        else:
            print(f"\n[Error] Status '{new_status}' is invalid. Valid options: {valid_statuses}")
            return False

    def generate_count_report(self):
        """Adds reservation count per student."""

        if not self.students:
            return {}

        count_report = {student.name: 0 for student in self.students}

        for reservation in self.reservations:
            # We check against the English terms now
            if reservation.status != "Cancelled" and reservation.status != "Completed":
                student_name = reservation.student.name
                if student_name in count_report:
                    count_report[student_name] += 1

        return count_report