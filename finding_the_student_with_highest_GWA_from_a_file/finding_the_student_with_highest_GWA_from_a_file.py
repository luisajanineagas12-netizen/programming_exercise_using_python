class HighestGWAFinder:
    def __init__(self, filename: str = "gwa.txt"):
        self.filename = filename

    def find_highest_gwa(self):
        try:
            with open(self.filename, "r") as file:
                highest_student = None
                highest_gwa = None

                for line in file:
                    parts = line.strip().split()
                    if len(parts) < 2:
                        continue  # skip malformed lines

                    # Last part is assumed to be the GWA, rest is the name
                    name = " ".join(parts[:-1])
                    try:
                        gwa = float(parts[-1])
                    except ValueError:
                        print(f"Skipping invalid GWA for {name}")
                        continue

                    if highest_gwa is None or gwa > highest_gwa:
                        highest_gwa = gwa
                        highest_student = name

            if highest_student is not None:
                print(f"Highest GWA: {highest_student} ({highest_gwa})")
            else:
                print("No valid student data found.")

        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' was not found.")
        except PermissionError:
            print("Error: Permission denied. Close the file if it is open elsewhere.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    finder = HighestGWAFinder("gwa.txt")
    finder.find_highest_gwa()
