
def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Hello, this is my first line of text.\n")
            file.write("The second line contains a number: 42.\n")
            file.write("Here's the third line with some more text.\n")
        print("File created and initial content written successfully.")
    except (PermissionError, IOError) as e:
        print(f"Error while creating the file: {e}")
    finally:
        print("Finished creating the file.")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            contents = file.read()
            print("Contents of 'my_file.txt':")
            print(contents)
    except FileNotFoundError as e:
        print(f"Error: The file was not found. {e}")
    except (PermissionError, IOError) as e:
        print(f"Error while reading the file: {e}")
    finally:
        print("Finished reading the file.")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("This is the fourth line being appended.\n")
            file.write("The fifth line adds another number: 100.\n")
            file.write("Finally, the sixth line is here!\n")
        print("Additional content appended successfully.")
    except (PermissionError, IOError) as e:
        print(f"Error while appending to the file: {e}")
    finally:
        print("Finished appending to the file.")

create_file()
read_file()
append_to_file()
read_file() 
