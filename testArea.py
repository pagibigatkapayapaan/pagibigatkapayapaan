file = open(f"files/{'essay.txt'}", 'r')

contents = file.readlines()
for content in contents:
    print(content.title())
file.close()

#%%
file = open(f"files/{'essay.txt'}", 'r')
contents = file.readlines()
count = 0
for items in contents:
    for item in items:
        count += 1
print(count)

#%%
# Coding Exercise 5
new_member = input("Add a new member: -> ") + "\n"
file = open('members.txt', 'r')
files = file.readlines()
file.close()

files.append(new_member)

file = open('members.txt', 'w')
member = file.writelines(files)
file.close()

#%%
# Coding Exercise 6
# Not solved

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    f = open(filename, 'w')
    f.write("Hello")
    f.close()

print("Done")


















