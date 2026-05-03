class IntegerProcessor:
    def __init__(self, filename: str = "integers.txt"):
        self.filename = filename
        self.even_square_file = "double.txt"
        self.odd_cube_file = "triple.txt"

    def process_numbers(self):
        try:
            # Read integers from the source file
            with open(self.filename, "r") as file:
                numbers = [int(line.strip()) for line in file if line.strip()]

            # Open output files
            with open(self.even_square_file, "w") as square_file, \
                 open(self.odd_cube_file, "w") as cube_file:

                for num in numbers:
                    if num % 2 == 0:  # Even → square
                        square_file.write(f"{num ** 2}\n")
                    else:             # Odd → cube
                        cube_file.write(f"{num ** 3}\n")

            print("✅ Processing complete. Check double.txt and triple.txt.")

        except FileNotFoundError:
            print(f"❌ Error: The source file '{self.filename}' was not found.")
        except ValueError:
            print("❌ Error: The file contains non-integer data. Please clean 'integers.txt'.")
        except PermissionError:
            print("❌ Error: Permission denied. Close the files if they are open elsewhere.")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    processor = IntegerProcessor()
    processor.process_numbers()
