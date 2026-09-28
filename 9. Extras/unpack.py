#first, _ = input("What's your name? ").split(" ")
#print(f"hello, {first}")

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]
coinsD = {"galleons": 100, "sickles":50, "knuts":25}

# Unpack a list: use *
#print(total(*coins), "Knuts")
# Unpack a Dictionary: use **
#print(total(**coinsD), "Knuts")

def f(*args, **kwargs):
    #print("Positional:", args)
    print("Positional:", kwargs)

#f(100, 50, 25)
f(galleons= 100, sickles=50, knuts=25)