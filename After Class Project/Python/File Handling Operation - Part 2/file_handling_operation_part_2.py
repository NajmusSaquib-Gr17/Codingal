import os

with open("After Class Project\Python\File Handling Operation - Part 2\Sample_File.txt", "w") as f:     # Write intro
    f.write("My name is Najmus Saquib. I love programming and technology.\n")

with open("After Class Project\Python\File Handling Operation - Part 2\Sample_File.txt", "r") as f:     # Print words
    print(f.read().split())

if not os.path.exists("D:\Codingal\After Class Project\Python\File Handling Operation - Part 2\My_File.txt"):       # Create if not exists
    with open("D:\Codingal\After Class Project\Python\File Handling Operation - Part 2\My_File.txt", "w") as f:
        f.write("My name is Najmus Saquib. I love programming and technology.\n")

if os.path.exists("D:\Codingal\After Class Project\Python\File Handling Operation - Part 2\Sample_File.txt"):            # Delete file
    os.remove("D:\Codingal\After Class Project\Python\File Handling Operation - Part 2\Sample_File.txt")
