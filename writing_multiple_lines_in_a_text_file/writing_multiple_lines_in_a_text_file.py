def write_user_lines_to_file(filename: str = "mylife.txt"):

    try:
        number_of_lines = int(input("How many lines would you like to write? "))

        with open(filename, "w") as file:
            for i in range(1, number_of_lines + 1):
                user_line = input(f"Enter line {i}: ")
                file.write(user_line + "\n")

        print(f"All {number_of_lines} lines have been written to {filename} successfully!")

    except ValueError:
        print("Invalid input. Please enter a valid number for the lines.")


# Run the method
write_user_lines_to_file()
