from models.student import Student

# Reservation - attributes: activity, date, time, status

class Reservation:
    """
    Represents an activity reservation for a student.
    Attributes: activity, date, time, status.
    Implements the association between Reservation and Student.
    """

    def __init__(self, student: Student, activity: str, date: str, time: str):
        """
        Constructor for the Reservation class.

        Args:
            student (Student): The Student object making the reservation.
            activity (str): The reserved activity (e.g., Weight Training).
            date (str): The reservation date (format DD/MM/YYYY).
            time (str): The reservation time (format HH:MM).
        """
        # This is the association
        self.student = student

        self.activity = activity
        self.date = date
        self.time = time

        # The default initial status will be "Reserved"
        self.status = "Reserved"

    def __repr__(self):
        """Returns a string representation of the Reservation object."""
        return f"Reservation(student='{self.student.name}', activity='{self.activity}', date='{self.date}')"