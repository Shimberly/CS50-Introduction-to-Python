def main():
    hello()
    name = input("What's your name? ")
    hello(name)

def hello(name="Kitty"):
    name = name.strip().title()
    print(f"Hello, {name}")

main()