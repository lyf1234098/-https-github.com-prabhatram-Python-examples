def replace_word(text):
    count = 1
    words = text.split()
    for i in range(len(words)):
        if words[i] == "terrible":
            count += 1
            if count % 2 == 0:
                words[i] = "pathetic"
            else:
                words[i] = "marvellous"
    return " ".join(words), count

# Read the file
with open("file_to_read.txt", "r") as file:
    content = file.read()

# Replace the word and get the count
new_content, count = replace_word(content)

# Display the count
print("Total occurrences of 'terrible':", count)

# Write the modified text to a new file
with open("result.txt", "w") as file:
    file.write(new_content)

print("Modified text has been written to 'result.txt'")


