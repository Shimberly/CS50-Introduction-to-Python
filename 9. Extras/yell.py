def main():
    #yell(["This","is","CS50"])
    yell("This", "is", "CS50")

def yell(*words):
    """ #Example 1 
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)
    """

    # Using MAP function. 
    # uppercased= map(str.upper, words)

    # List Comprehension
    uppercased = [word.upper() for word in words]

    print(*uppercased)

if __name__ == "__main__":
    main()