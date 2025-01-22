class HealthcareSystem:
    def _init_(self):
        self.users = {}  # Store user credentials

    def register(self):
        username = input("Enter a username: ")
        if username in self.users:
            print("Username already exists. Please log in.")
            return
        password = input("Enter a password: ")
        self.users[username] = password
        print("Registration successful! Please log in.")

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if self.users.get(username) == password:
            print("Login successful!")
            return True
        print("Invalid credentials. Please try again or register.")
        return False

    def first_aid(self):
        print("First aid instructions provided.")

    def identify_problem(self):
        print("Identifying problem...")
        severity = input("Is the problem serious? (yes/no): ").lower()
        if severity == "yes":
            self.handle_serious_case()
        else:
            self.handle_non_serious_case()

    def handle_serious_case(self):
        action = input("Quick reaction needed. Choose: (1) Emergency Services, (2) Doctor Consultation: ")
        if action == "1":
            print("Contacting emergency services...")
        elif action == "2":
            print("Consulting a doctor...")
        else:
            print("Invalid option.")

    def handle_non_serious_case(self):
        action = input("Choose: (1) Doctor Appointment, (2) Follow Recommendations: ")
        if action == "1":
            print("Booking a doctor appointment...")
        elif action == "2":
            print("Providing further actions and recommended medication...")
        else:
            print("Invalid option.")

    def enquiry(self):
        print("Handling enquiry...")

    def database(self):
        print("Accessing problem database...")

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. First Aid")
            print("2. Problem Identification")
            print("3. Enquiry")
            print("4. Access Database")
            print("5. Exit")

            choice = input("Choose an option: ")
            if choice == "1":
                self.first_aid()
            elif choice == "2":
                self.identify_problem()
            elif choice == "3":
                self.enquiry()
            elif choice == "4":
                self.database()
            elif choice == "5":
                print("Exiting the system. Stay healthy!")
                break
            else:
                print("Invalid option. Please try again.")

    def start(self):
        while True:
            print("\nWelcome to the Healthcare System")
            print("1. Login")
            print("2. Register")
            print("3. Exit")

            choice = input("Choose an option: ")
            if choice == "1":
                if self.login():
                    self.main_menu()
            elif choice == "2":
                self.register()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

# Run the system
healthcare_system = HealthcareSystem()
healthcare_system.start()