def separate_even_and_odd(input_file="numbers.txt",
                          even_file="even.txt",
                          odd_file="odd.txt"):
    try:
        # Read integers from the source file
        with open(input_file, "r") as file:
            numbers = [int(line.strip()) for line in file if line.strip()]

        # Separate and write to files
        with open(even_file, "w") as even_out, open(odd_file, "w") as odd_out:
            for num in numbers:
                if num % 2 == 0:
                    even_out.write(f"{num}\n")
                else:
                    odd_out.write(f"{num}\n")

        print("✅ Separation complete. Check even.txt and odd.txt.")

    except FileNotFoundError:
        print(f"❌ Error: The source file '{input_file}' was not found.")
    except ValueError:
        print("❌ Error: The file contains non-integer data. Please clean 'numbers.txt'.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


# Run the program
if __name__ == "__main__":
    separate_even_and_odd()
