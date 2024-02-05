from pathlib import Path
from datetime import date

print(Path(__file__).parent)
diary_folder = Path(__file__).parent / "Diary"
diary_folder.mkdir(exist_ok=True)

while True:
    user_input = input("type 'Write' to add a an intry, type 'Read' to see the list of entries: ")
    if user_input.lower() in ["quit", "q"]:
        break

    if user_input.lower() in ["write", "w"]:
        entry_text = input("Please write your entry: \n")
        entry_date = date.today().strftime("%Y-%m-%d")
        entry_file = diary_folder / f"{entry_date}.txt"

        if not entry_file.exists():
            with open(diary_folder / "diary_log.txt", "a") as file:
                file.write(f"{entry_date}\n")
        
        with open(entry_file, "a") as file:
            file.write(entry_text + "\n")
        
    elif user_input.lower() in ["read", "r"]:
        try:
            with open(diary_folder / "diary_log.txt", "r") as file:
                entries = file.readlines()
                print("Available Entries")
                for entry in entries:
                    print(entry.strip())
        except FileNotFoundError as e:
            print("There are currently no entries on your diary.")

        entry_date = input("Please provide an entry date (YYYY-MM-DD):\n")
        entry_file = diary_folder / f"{entry_date}.txt"

        try:
            with open(entry_file, "r") as file:
                print(f"Entry for {entry_date}:\n{file.read()}")
        except FileNotFoundError as e:
            print(f"Entry: '{entry_date}' do not exist.")

    else:
        print("Error: Invalid command. Please use 'Write', 'Read', or 'Quit'.")
