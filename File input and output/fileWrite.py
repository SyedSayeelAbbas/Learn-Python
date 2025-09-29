# r = read only (file must exist)
with open("demo.txt", "r") as f:
    print("Reading with r:")
    print(f.read())

# r+ = read + write (file must exist)
with open("demo.txt", "r+") as f:
    print("\nReading with r+:")
    print(f.read())
    f.seek(0)  # move cursor to start
    f.write("NEW DATA - ")  # overwrites from start
    f.seek(0)
    print("After writing with r+:")
    print(f.read())

# w = write only (overwrite). Previous content is removed!
with open("demo.txt", "w") as f:
    f.write("Hello Everyone, my name is Syed Sayeel Abbas\nand I am learning Python")
print("\nAfter w mode: file is overwritten.")

# w+ = write + read (overwrite). Clears file before writing.
with open("demo.txt", "w+") as f:
    f.write("This is written with w+ mode")
    f.seek(0)  # move to start for reading
    print("\nReading with w+:")
    print(f.read())

# a = append only (write at end). Keeps old data.
with open("demo.txt", "a") as f:
    f.write("\nIt’s nice to learn Python")
print("\nAfter a mode: data was appended.")

# a+ = append + read (write at end + can read). Creates file if not exist.
with open("demo.txt", "a+") as f:
    f.write("\nAdding this line using a+ mode")
    f.seek(0)
    print("\nReading with a+:")
    print(f.read())

# Creating a new file (if not exists) with w
with open("demo1.txt", "w") as f:
    f.write("Hello, I just created this file demo1 by this step.")
print("\nNew file demo1.txt created.")
