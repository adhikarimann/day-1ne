name = input("enter your name: ")
subject = input("What are you studying today? ")
hours = int(input("How many hours will you study? "))

print(f"\nWelcome {name}")
print(f"Today's subject: {subject}")
print(f"Planned study hours: {hours}")

if hours >= 5:
    print("Strong study day! ")
else :
    print("Try increasing focus time!")