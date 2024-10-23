try:
    # Open both files for reading
    with open("C:\\Users\\Admin\\Documents\\ism\\week7\\file1.txt", "r") as f1, open("C:\\Users\\Admin\\Documents\\ism\\week7\\file2.txt", "r") as f2:
        f1_lines = f1.readlines()
        f2_lines = f2.readlines()

    # Check if files have enough lines
    if not f1_lines or not f2_lines:
        print("One of the files is empty.")
    else:
        # Get the middle line of file1 and the last line of file2
        f1_midline = f1_lines[len(f1_lines) // 2]
        f2_lastline = f2_lines[-1]

        # Print the lines to be swapped
        print(f"Middle line from file1.txt: {f1_midline.strip()}")
        print(f"Last line from file2.txt: {f2_lastline.strip()}")

        # Swap the lines
        f1_lines[len(f1_lines) // 2] = f2_lastline
        f2_lines[-1] = f1_midline

        # Open both files for writing
        with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
            f1.writelines(f1_lines)
            f2.writelines(f2_lines)

        # Display the updated files
        print("\nUpdated File1:")
        with open("file1.txt", "r") as f1:
            print(f1.read(), end="")

        print("\nUpdated File2:")
        with open("file2.txt", "r") as f2:
            print(f2.read(), end="")

except FileNotFoundError:
    print("One or both files do not exist.")
except Exception as e:
    print(f"An error occurred: {e}")