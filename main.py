import json
import getpass
import joblib
import numpy as np
import re

class HealthcareSystem:
    def __init__(self):
        self.users = self.load_users()
        self.model = joblib.load("healthcare_model.pkl")  # Load ML model

    def load_users(self):
        """Load user credentials from a file."""
        try:
            with open("users.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_users(self):
        """Save user credentials to a file."""
        with open("users.json", "w") as file:
            json.dump(self.users, file, indent=4)

    def register(self):
        """Handles user registration."""
        username = input("Enter a username: ")
        if username in self.users:
            print("Username already exists. Please log in.")
            return

        password = getpass.getpass("Enter a password: ")
        confirm_password = getpass.getpass("Confirm your password: ")

        if password != confirm_password:
            print("Passwords do not match. Try again.")
            return
        
        self.users[username] = password
        self.save_users()
        print("✅ Registration successful! You can now log in.")

    def login(self):
        """Handles user login."""
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")

        if self.users.get(username) == password:
            print("✅ Login successful!")
            return True
        print("❌ Invalid credentials. Please try again or register.")
        return False

    def first_aid(self):
        print("🩹 First aid instructions provided.")

    def identify_problem(self):
        """Ask the user about their problem and determine severity."""
        print("🩺 Describe your problem in a few words (e.g., 'I have chest pain and difficulty breathing').")
        
        user_input = input("Your response: ").strip().lower()

        # Keywords indicating a serious condition
        serious_keywords = [
            "chest pain", "difficulty breathing", "severe headache",
            "unconscious", "bleeding heavily", "high fever", "vomiting blood"
        ]

        # Keywords indicating a mild condition
        mild_keywords = [
            "cough", "mild fever", "stomach pain", "headache", 
            "fatigue", "runny nose", "body pain"
        ]
        
        # Check if the problem matches serious or mild conditions
        if any(re.search(rf"\b{kw}\b", user_input) for kw in serious_keywords):
            print("⚠️ Your symptoms suggest a serious condition.")
            self.handle_serious_case()
        elif any(re.search(rf"\b{kw}\b", user_input) for kw in mild_keywords):
            print("ℹ️ Your symptoms seem mild. Let's proceed with self-care or a doctor’s appointment.")
            self.handle_non_serious_case()
        else:
            print("🤖 Unable to determine severity. Proceeding with general recommendations.")
            self.handle_non_serious_case()

    def handle_serious_case(self):
        while True:
            action = input("Choose: (1) Emergency Services, (2) Doctor Consultation: ")
            if action == "1":
                print("🚑 Contacting emergency services...")
                break
            elif action == "2":
                print("👨‍⚕️ Consulting a doctor...")
                break
            else:
                print("❌ Invalid option. Please choose 1 or 2.")

    def handle_non_serious_case(self):
        while True:
            action = input("Choose: (1) Doctor Appointment, (2) Follow Recommendations: ")
            if action == "1":
                print("📅 Booking a doctor appointment...")
                break
            elif action == "2":
                print("💊 Providing further actions and recommended medication...")
                break
            else:
                print("❌ Invalid option. Please choose 1 or 2.")

    def enquiry(self):
        print("📞 Handling enquiry...")

    def database(self):
        print("📂 Accessing problem database...")

    def predict_disease(self):
        """AI-based disease prediction."""
        print("\n🧠 AI Symptom Checker: Answer Yes(1) or No(0)")

        try:
            fever = int(input("Do you have a fever? (1 for Yes, 0 for No): "))
            cough = int(input("Do you have a cough? (1 for Yes, 0 for No): "))
            fatigue = int(input("Do you feel fatigued? (1 for Yes, 0 for No): "))
            body_pain = int(input("Do you have body pain? (1 for Yes, 0 for No): "))
            sore_throat = int(input("Do you have a sore throat? (1 for Yes, 0 for No): "))
            runny_nose = int(input("Do you have a runny nose? (1 for Yes, 0 for No): "))

            symptoms = np.array([[fever, cough, fatigue, body_pain, sore_throat, runny_nose]])  # Prepare data
            prediction = self.model.predict(symptoms)[0]  # Predict disease

            print(f"\n⚕️ Based on your symptoms, you might have: **{prediction}**")
        except ValueError:
            print("❌ Invalid input. Please enter 1 or 0.")

    def main_menu(self):
        """Main menu after login."""
        while True:
            print("\n🏥 Main Menu:")
            print("1. First Aid")
            print("2. Problem Identification")
            print("3. Enquiry")
            print("4. AI Symptom Checker 🤖")
            print("5. Access Database")
            print("6. Logout")

            choice = input("Choose an option: ").strip()
            if choice == "1":
                self.first_aid()
            elif choice == "2":
                self.identify_problem()
            elif choice == "3":
                self.enquiry()
            elif choice == "4":
                self.predict_disease()  # Call AI Symptom Checker
            elif choice == "5":
                self.database()
            elif choice == "6":
                print("👋 Logging out...")
                break
            else:
                print("❌ Invalid option. Please try again.")

    def start(self):
        """Starting point of the healthcare system."""
        while True:
            print("\n🌟 Welcome to the AI Healthcare System")
            print("1. Login")
            print("2. Register")
            print("3. Exit")

            choice = input("Choose an option: ").strip()
            if choice == "1":
                if self.login():
                    self.main_menu()
            elif choice == "2":
                self.register()
            elif choice == "3":
                print("👋 Goodbye! Stay healthy!")
                break
            else:
                print("❌ Invalid option. Please try again.")

# Run the system
if __name__ == "__main__":
    healthcare_system = HealthcareSystem()
    healthcare_system.start()
