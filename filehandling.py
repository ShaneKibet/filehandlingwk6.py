# File Creation
try:
    # Create a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text to the file
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line with some text and numbers: 98765\n")
        print("File created and initial content written successfully.")
except PermissionError as e:
    print(f"Error: {e}. Check file permissions.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File creation process completed.\n")

# File Reading and Display
try:
    # Open "my_file.txt" in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read and display the contents of the file
        file_contents = file.read()
        print("Contents of my_file.txt:")
        print(file_contents)
except FileNotFoundError as e:
    print(f"Error: {e}. File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File reading and display process completed.\n")

# File Appending
try:
    # Open "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the existing content
        file.write("Appending line 1\n")
        file.write("Appending line 2\n")
        file.write("Appending line 3\n")
    print("File appended successfully.")
except PermissionError as e:
    print(f"Error: {e}. Check file permissions.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File appending process completed.\n")

# Error Handling with try-except blocks
try:
    # Attempt to open a non-existent file in read mode
    with open("nonexistent_file.txt", "r") as file:
        file_contents = file.read()
        print(file_contents)
except FileNotFoundError as e:
    print(f"Error: {e}. File not found.")
except PermissionError as e:
    print(f"Error: {e}. Check file permissions.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Error handling example completed.")
