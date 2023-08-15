import json

class AppointmentScheduler:
    def __init__(self):
        self.appointments = {}

    def book_appointment(self, name, date_time):
        if date_time in self.appointments:
            print("You can't book at this time.")
        else:
            self.appointments[date_time] = date_time
            self.appointments[name] = name
            print("Appointment booked successfully.")

    def show_appointments(self):
        print("Booked Appointments:")
        for date_time, name in self.appointments.items():
            print(f"{name}: {date_time}")
    
    def save_appointments(self):
        with open("appointments.json", "a") as file:
            for a in self.appointments:
                json.dump(a, file, indent=2)

def main():
    scheduler = AppointmentScheduler()

    while True:
        print("1. Book Appointment")
        print("2. Show Appointments")
        print("3. Quit")
        choice = int(input("Select an option: "))

        if choice == 1:
            name = input("Enter your name: ")
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM): ")
            scheduler.book_appointment(name, date_time)
        elif choice == 2:
            scheduler.show_appointments()
        elif choice == 3:
            print("Exiting the program.")
            scheduler.save_appointments()
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
