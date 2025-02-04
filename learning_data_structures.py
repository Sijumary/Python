missions = []
mission_details = {}

def add_mission(missions, mission_details, name, details):
    if name in mission_details:
        print("Mission already exists!")
        return
    missions.append(name)
    mission_details[name] = details
    print("\nMission added successfully")

    

def update_mission(mission_details, name, key, value):
    if name not in mission_details:
        print("\nMission not found")
        return

    if key not in mission_details[name]:
        print("\nInvalid detail key! Use Destination, Launch Date, or Crew.")
        return
    mission_details[name][key] = value
    print("\nMission updated successfully!")

def display_missions(missions, mission_details):
    if not missions:
        print("\nNo missions available.")
        return

    print("\nAll Missions:")
    for i, mission in enumerate(missions, 1):
        details = mission_details[mission]
        print(f"{i}. {mission}")
        print(f"   Destination: {details['Destination']}")
        print(f"   Launch Date: {details['Launch Date']}")
        print(f"   Crew: {details['Crew']}")

def list_astronauts(mission_details):
     astronauts = set()
     for details in mission_details.values():
        crew_members = details["Crew"].split(", ")  # Split crew names by comma
        astronauts.update(crew_members)
        return astronauts

# Main menu loop
while True:
    print("\nSpace Mission Management System")
    print("1. Add Mission")
    print("2. Update Mission")
    print("3. Display Missions")
    print("4. List Astronauts")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        name = input("Enter mission name: ")
        destination = input("Enter destination: ")
        launch_date = input("Enter launch date: ")
        crew = input("Enter crew members (comma-separated): ")
        details = {
            "Destination": destination,
            "Launch Date": launch_date,
            "Crew": crew
        }
        add_mission(missions, mission_details, name, details)

    elif choice == '2':
        name = input("Enter mission name to update: ")
        key = input("Enter detail to update (Destination/Launch Date/Crew): ")
        value = input(f"Enter new value for {key}: ")
        update_mission(mission_details, name, key, value)

    elif choice == '3':
        display_missions(missions, mission_details)

    elif choice == '4':
        astronauts = list_astronauts(mission_details)
        print("\nAll Astronauts:")
        for astronaut in astronauts:
            print(f"- {astronaut}")

    elif choice == '5':
        print("Exiting Space Mission Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
