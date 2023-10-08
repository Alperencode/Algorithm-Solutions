def to_weird_case(words):
    words = words.split(" ")
    for i in range(len(words)):
        words[i] = "".join([x.upper() if j % 2 == 0 else x.lower() for j, x in enumerate(words[i])])

    return " ".join(words)

# Testcases
# to_weird_case("This is a test")

# Status - Passed
