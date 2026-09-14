def main():
    #x = float(input("Whats x? "))
    #y = float(input("Whats y? "))
    n= int(input("Whats n? "))

    #z = round(x + y, 1) #Rounding to 1 decimal
    #d = x / y

    # Formatting
    #print(f"{z:,}") #Use comma as a thousand separator
    #print(f"{d:.2f}") #Defining 2 decimals
    print(f"{n} squared is {square(n)}")

def square(n):
    return pow(n,2)

main()