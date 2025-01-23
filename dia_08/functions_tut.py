def greet():
    print("Hello")
    print("I hope you are having a nice day")
    print("Lock in for this 2025")

greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Lock in {name}")

greet_with_name("Santiago")

# functions with more than 1 input
def greet_with(name, location):
    print(f"Hi {name}")
    print(f"How's the weather in {location}?")

greet_with(location="Paris", name="Santiago")