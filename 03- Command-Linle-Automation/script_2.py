import sys

def greeting(greet):
    message = f"{greet}"
    print(message)

if __name__ == "__main__":
    greeting(sys.argv[1])