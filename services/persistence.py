from models.student import Student
from models.reservation import Reservation
import os  # We will use 'os' to ensure the 'data' folder exists

# Add simple persistence (.txt file).

# File paths
DATA_DIR = "data"
STUDENTS_FILE = os.path.join(DATA_DIR, "students.txt")
RESERVATIONS_FILE = os.path.join(DATA_DIR, "reservations.txt")


def _ensure_data_folder():
    """
    Internal helper function (private).
    Checks if the 'data' directory exists. If not, attempts to create it.
    Raises an exception (stops the program) if creation fails.
    """
    if not os.path.exists(DATA_DIR):
        try:
            os.makedirs(DATA_DIR)
            print(f"[Info] Folder '{DATA_DIR}' created.")
        except IOError as e:
            print(f"[Fatal Error] Could not create folder '{DATA_DIR}': {e}")
            raise


def save_data(student_list, reservation_list):
    """
    Saves the current state of student and reservation lists to .txt files.
    Implement simple file persistence.

    Student Format: name;cpf;age;plan
    Reservation Format: student_cpf;activity;date;time;status
    The CPF/ID is used to save the association.

    Args:
        student_list (list[Student]): The list of Student objects to save.
        reservation_list (list[Reservation]): The list of Reservation objects to save.
    """
    _ensure_data_folder()  # Ensures the folder exists before saving

    # --- Save Students ---
    try:
        with open(STUDENTS_FILE, "w", encoding="utf-8") as f:
            for student in student_list:
                f.write(f"{student.name};{student.cpf};{student.age};{student.plan}\n")
    except IOError as e:
        print(f"[Error] Failed to save students: {e}")

    # --- Save Reservations ---
    try:
        with open(RESERVATIONS_FILE, "w", encoding="utf-8") as f:
            for res in reservation_list:
                # We save the CPF to maintain the association
                f.write(f"{res.student.cpf};{res.activity};{res.date};{res.time};{res.status}\n")
    except IOError as e:
        print(f"[Error] Failed to save reservations: {e}")


def load_data():
    """
    Loads data from .txt files and recreates objects in memory.
    Implements persistence reading.

    The logic reconstructs the association by loading
    students first, and then linking reservations to them
    via CPF (using a map/dictionary).

    Returns:
        tuple: A tuple containing (loaded_students_list, loaded_reservations_list).
               Returns empty lists if files do not exist or an error occurs.
    """
    _ensure_data_folder()  # Ensures the folder exists before reading

    loaded_students = []
    student_map_by_cpf = {}    # Map to recreate the association

    # --- Load Students ---
    try:
        with open(STUDENTS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip(): continue  # Ignore empty lines
                name, cpf, age_str, plan = line.strip().split(';')
                new_student = Student(name, cpf, int(age_str), plan)

                loaded_students.append(new_student)
                student_map_by_cpf[cpf] = new_student   # Store in map

    except FileNotFoundError:
        print("[Info] 'students.txt' not found. Starting with empty list.")
    except IOError as e:
        print(f"[Error] Failed to load students: {e}")
    except ValueError as e:
        print(f"[Error] Invalid data format in 'students.txt': {e}")

    loaded_reservations = []

    # --- Load Reservations ---
    try:
        with open(RESERVATIONS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip(): continue  # Ignore empty lines
                cpf, activity, date, time, status = line.strip().split(';')

                # Use the map to recreate the association
                student_obj = student_map_by_cpf.get(cpf)

                if student_obj:
                    new_reservation = Reservation(student_obj, activity, date, time)
                    new_reservation.status = status # Restore saved status
                    loaded_reservations.append(new_reservation)
                else:
                    # This can happen if a student is removed but the reservation remains
                    print(f"[Warning] Reservation for CPF/ID {cpf} ignored (student not found).")

    except FileNotFoundError:
        print("[Info] 'reservations.txt' not found. Starting with empty list.")
    except IOError as e:
        print(f"[Error] Failed to load reservations: {e}")
    except ValueError as e:
        print(f"[Error] Invalid data format in 'reservations.txt': {e}")

    return loaded_students, loaded_reservations