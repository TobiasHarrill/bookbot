print("ligmar")

with open("books/frank.txt") as f:
    
    content = f.read()
    words = content.split()
    
    letters = {x : content.count(x) for x in sorted(set(content.lower()))}

    print("the file has " + str(len(words)) + " words")
    print()
    # print("here is some letters: " + str(letters))

    def sort_on(dict):
        return dict[num]

    for char, count in letters.items():
        print("letter {0} found {1} times".format(char, count))

    print("python my balls")