# Student - attributes: name, cpf, age, plan

class Student:
    """
    Represents a gym student.
    Attributes: name, cpf, age, plan.
    """
    def __init__(self, name, cpf, age, plan):
        """
        Constructor for the Student class.

        Args:
            name (str): The student's full name.
            cpf (str): The student's CPF/ID (used as identifier).
            age (int): The student's age.
            plan (str): The plan type (e.g., Monthly, Quarterly).
        """
        self.name = name
        self.cpf = cpf
        self.age = age
        self.plan = plan

    def __repr__(self):
        """Returns a string representation of the Student object."""
        return f"Student(name='{self.name}', cpf='{self.cpf}')"