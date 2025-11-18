# 🏋️‍♂️ Gym Reservation System (Python CLI)

This is an academic project simulating a gym management system, developed entirely in Python and running in the terminal (CLI).

The main objective is to apply **Object-Oriented Programming (OOP)** and **Agile Methodologies** concepts in an incremental development process, focusing on software maintenance and evolution.

## ✨ OOP Concepts Applied

The project was structured following the pillars of OOP:
* **Classes and Objects:** `Student` and `Reservation` are the system's "models".
* **Encapsulation:** Business logic is managed by the `GymSystem` class, acting as the "brain" and protecting data.
* **Association:** The `Reservation` class is directly associated with a `Student` object, demonstrating a "one-to-many" relationship.

## 🚀 Features (Iterations 1 and 2)

The terminal system implements the following features:

* **Student Management:** Register new students.
* **Validation:** The system prevents registration of students with duplicate CPF/IDs.
* **Reservation Management:** Add and list all reservations.
* **Reservation Maintenance:** Update reservation status (e.g., Reserved, Confirmed, Cancelled).
* **Reports:** Generate a simple report counting active reservations per student.
* **Data Persistence:** The system automatically saves and loads all data (students and reservations) from `.txt` files, ensuring data isn't lost when closing the program.

## 📂 Modular Project Structure

To facilitate maintenance and follow agile principles, the code was modularized as follows:

* **`GymSystemsTerminal/`** (Project root)
    * **`models/`**: Contains data classes ("models").
        * `student.py`: Defines the `Student` class.
        * `reservation.py`: Defines the `Reservation` class.
    * **`services/`**: Contains logic and service classes (the "brain").
        * `system.py`: Defines the `GymSystem` class, which manages the system.
        * `persistence.py`: Defines the logic to save/load `.txt` files.
    * **`data/`**: Folder automatically created to store persistence data.
        * `students.txt`
        * `reservations.txt`
    * **`main.py`**: Application entry point and responsible for the terminal menu.
    * **`__init__.py`** (inside `models` and `services`): Empty files signaling to Python that the folders are "packages".

## ▶️ How to Run

1.  Clone this repository.
2.  Ensure **Python 3** is installed.
3.  Navigate to the project root folder in your terminal.
4.  Execute the main menu:

    ```bash
    python main.py
    ```
5.  On the first run, the `/data` folder and files with dummy data will be created automatically.