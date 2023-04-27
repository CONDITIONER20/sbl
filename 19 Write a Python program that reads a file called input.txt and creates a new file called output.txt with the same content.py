# open input file in read mode
with open("input.txt", "r") as input_file:
    # read contents of input file and remove vowels
    contents = input_file.read()
    contents_without_vowels = ""
    for char in contents:
        if char.lower() not in "aeiou":
            contents_without_vowels += char
    
    # open output file in write mode and write modified contents
    with open("output.txt", "w") as output_file:
        output_file.write(contents_without_vowels)
