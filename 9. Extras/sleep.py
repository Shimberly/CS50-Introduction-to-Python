def main():
    n = int(input("What's n? "))
    #for i in range(n):
    #    print(sheep(i))
    for s in sheep(n):
        print(s)

def sheep(n):
    #return ("🧚‍♀️"*n) 
    """
    flock = []
    for i in range(n):
        flock.append("🧚‍♀️"*i)
    return flock
    """

    # Using GENERATORS: yield
    for i in range(n):
        #yield instead of return: this return a bit of data at a time
        #
        yield "🧚‍♀️"*i


if __name__ == "__main__":
    main()