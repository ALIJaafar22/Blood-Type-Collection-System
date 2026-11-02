# Phase 1: User Identification & Welcome Message
user = input("Enter your username: ")
print("Welcome, ", user)

# Phase 2: Conditional Question
x = input("Are you a donor? (yes or no): ")

# Phase 3: Logic and Blood Type Selection
if x.lower() == "yes":
    pass  # Terminate if the user answers yes
else:
    # Prompt for blood type if the answer is no or any other input
    y = input("Select your blood type (O+, O-, A+, A-, B+, B-, AB+, AB-): ")
    print("Thanks for your time and cooperation!")
