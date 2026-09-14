def main():
    #print_column(3)
    #print_row(4)
    print_square(3)

def print_column(height):
    #for _ in range(height):
    #    print("#")
    print("#\n" * height, end="")

def print_row(width):
    print("#" * width)

def print_square(size):
    """ Option 1:
    for i in range(size):
        for j in range(size):
            # Print brick
            print("#", end="")
        # Print a new line
        print("")"""
    """ Option 2
    for i in range(size):
        print("#"*size)"""
    for i in range(size):
        print_row(size)
main()