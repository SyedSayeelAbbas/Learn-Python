# Read entire file
with open("demo.txt", "r") as f:
    data = f.read()
    print("Whole file:")
    print(data)

# Read first 4 characters
with open("demo.txt", "r") as f:
    data = f.read(4)
    print("First 4 characters:")
    print(data)

# Read first line and then the next
with open("demo.txt", "r") as f:
    data = f.readline()
    print("First line:")
    print(data)

    data = f.readline()
    print("Second line:")
    print(data)

# Using r+ (read and write)
with open("demo.txt", "r+") as f:
    print("Reading with r+:")
    data = f.read()
    print(data)

    # Move cursor back to start and write something
    f.seek(0)
    f.write("NEW START - ")

    # Move again to start to see updated content
    f.seek(0)
    print("After writing with r+:")
    print(f.read())
