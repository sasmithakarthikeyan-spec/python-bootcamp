'''import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Mark"])
    writer.writerow(["Arun", 20, 85])
    writer.writerow(["Priya", 21, 92])

import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["Mark"]) > 80:
            print(row["Name"])

import json
data = {
    "name": "Arun",
    "age": 20,
    "skills": ["Python", "HTML", "CSS"]
}

json_data = json.dumps(data)

print(json_data)

json_data = '{"name": "Arun", "age": 20}'
data = json.loads(json_data)

print(data)
print(data["name"])'''

#mini project-5

import csv
import json

files = []


def add_file():
    filename = input("Enter file name: ")

    if "." in filename:
        extension = filename.split(".")[-1].lower()
    else:
        extension = "unknown"

    if extension in ["jpg", "png", "jpeg"]:
        category = "Image"

    elif extension in ["pdf", "docx", "txt"]:
        category = "Document"

    elif extension in ["mp3", "wav"]:
        category = "Audio"

    elif extension in ["mp4", "mkv"]:
        category = "Video"

    elif extension == "py":
        category = "Python"

    else:
        category = "Other"

    file_info = {
        "filename": filename,
        "extension": extension,
        "category": category
    }

    files.append(file_info)

    print("File added successfully!")


def save_csv():
    with open("files.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["filename", "extension", "category"]
        )

        writer.writeheader()
        writer.writerows(files)

    print("Data saved to CSV!")


def save_json():
    with open("files.json", "w") as file:
        json.dump(files, file, indent=4)

    print("Data saved to JSON!")


while True:

    print("\n--- FILE ORGANIZER ---")
    print("1. Add File")
    print("2. Save as CSV")
    print("3. Save as JSON")
    print("4. Show Files")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_file()

    elif choice == "2":
        save_csv()

    elif choice == "3":
        save_json()

    elif choice == "4":
        for file in files:
            print(file)

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice!")