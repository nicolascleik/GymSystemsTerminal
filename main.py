from services.system import GymSystemsTerminal

def initial_load(system):
    """Adds dummy data ONLY on the first execution."""
    print("[Info] First use detected. Loading dummy data...")

    student1 = system.register_student("Raposo Cleik", "111.111.111-11", 25, "Monthly")
    student2 = system.register_student("Floquinho Carvalho", "222.222.222-22", 30, "Quarterly")

    if student1 and student2:
        system.add_reservation(student1.cpf, "Weight Training", "20/11/2025", "18:00")
        system.add_reservation(student2.cpf, "Spinning", "21/11/2025", "09:00")

    print("-" * 30)


def display_menu():
    """Displays options to the user."""
    print("\n--- WELCOME TO THE GYM SYSTEM ---")
    print("1. Register New Student")
    print("2. Make New Reservation")
    print("3. List All Reservations")
    print("4. Update Reservation Status")
    print("5. View Reservation Report by Student")
    print("0. Exit")


def main():
    """Main function that runs the menu loop."""

    # 1. Creates the instance (which now LOADS data from .txt)
    system = GymSystemsTerminal()

    # 2. Checks if initial load is needed
    if not system.students:  # If the student list is empty
        initial_load(system)

    # 3. Main menu loop
    while True:
        display_menu()

        option = input("\nChoose an option: ")

        if option == '1':
            # --- Register Student ---
            print("\n--- Student Registration ---")
            name = input("Full Name: ")
            cpf = input("CPF/ID (e.g., 123.456.789-00): ")

            # Age validation
            try:
                age = int(input("Age: "))
            except ValueError:
                print("\n[Error] Invalid age. Must be a number.")
                continue  # Returns to menu

            plan = input("Plan (Monthly, Quarterly, etc.): ")

            system.register_student(name, cpf, age, plan)

        elif option == '2':
            # --- Add Reservation ---
            print("\n--- New Class Reservation ---")
            cpf = input("Enter Student CPF/ID: ")
            activity = input("Activity (e.g., Weight Training, Swimming): ")
            data = input("Date (DD/MM/YYYY): ")
            time = input("Time (HH:MM): ")

            system.add_reservation(cpf, activity, data, time)

        elif option == '3':
            # --- List Reservations ---
            print("\n--- Current Reservations ---")
            reservations = system.list_reservations()

            if not reservations:
                print("[Info] No reservations registered at the moment.")
            else:
                for res in reservations:
                    # Accessing attributes in English (student, activity, date, status)
                    print(f"- Student: {res.student.name} | Activity: {res.activity} | Date: {res.date} | Status: {res.status}")

        elif option == '4':
            # --- Update Reservation Status ---
            print("\n--- Update Reservation Status ---")
            cpf = input("Enter Student CPF/ID to view reservations: ")

            found_reservations = system.search_reservations_by_cpf(cpf)

            if not found_reservations:
                print("\n[Info] No reservations found for this CPF/ID.")
                continue

            print("\nReservations found for this student:")
            for index, res in enumerate(found_reservations):
                print(f"  {index + 1}. Activity: {res.activity} | Date: {res.date} | Current Status: {res.status}")

            try:
                choice_str = input("\nEnter the number of the reservation to change (or 0 to cancel): ")
                choice = int(choice_str)

                if choice == 0:
                    continue  # Returns to menu

                chosen_reservation = found_reservations[choice - 1]
            except (ValueError, IndexError):
                print("\n[Error] Invalid choice.")
                continue

            new_status = input("Enter new status (Reserved, Confirmed, Completed, Cancelled): ").capitalize()

            system.update_reservation_status(chosen_reservation, new_status)

        elif option == '5':
            # --- Count Report ---
            print("\n--- Report: Active Reservations by Student ---")

            report = system.generate_count_report()

            if not report:
                print("[Info] No students registered to generate report.")
            else:
                for name, count in report.items():
                    print(f"- {name}: {count} reservations")

        elif option == '0':
            print("\n[Info] Thank you for using the system. Goodbye!")
            break

        else:
            print("\n[Error] Invalid option! Please try again.")


# -----------------------------------------------------------------
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[FATAL ERROR] The program encountered an unexpected error: {e}")
        input("Press ENTER to exit.")