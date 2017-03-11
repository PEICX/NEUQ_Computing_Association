import random, string

forSelect = string.ascii_letters + "0123456789"

def generate(count, length):
    # count = 200
    # length = 20

    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        print(Re)

if __name__ == "__main__":
    generate(200, 20)