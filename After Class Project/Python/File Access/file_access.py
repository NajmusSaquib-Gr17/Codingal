# Read mode
f = open("After Class Project\Python\File Access\Sample_File.txt", "r")           # Read file
print(f.read())
f.close()

# Write mode
f = open("After Class Project\Python\File Access\Sample_File.txt", "w")           # Overwrite intro
f.write("I'm Najmus Saquib. I love coding.\n")
f.close()

# Append mode
f = open("After Class Project\Python\File Access\Sample_File.txt", "a")           # Add subject
f.write("Favorite subject: Computer Science.\n")
f.close()
