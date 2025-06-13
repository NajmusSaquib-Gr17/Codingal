f = open("After Class Project\Python\File Handling Operation - Part 1\Sample_File.txt", "r")

print(f.read())                # Full content

f.seek(0)
print(f.read(10))              # First 10 chars

f.seek(0)
print(f.readline())            # First line

f.seek(0)
for i in range(4):             # First 4 lines
    print(f.readline(), end='')

f.seek(0)
for line in f:                 # All lines
    print(line, end='')

f.close()
