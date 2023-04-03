from logo import logo
from dict import resources, MENU


def welcome_screen():
    """Prints the coffee logo and asks for a request, which is passed back to main"""
    print(logo)
    reqeust = input("welcome to the coffe shop, What would you like? (espresso/latte/cappuccino): ")
    return reqeust


def process_request(request):
    """Here we determine what the machine should do, either order report or shutdown.
    If none is found it will return to welcome screen after notifying the user that no option was found """
    for i in options:
        if i == request:
            return options[i]()
    print("The option you selected wasn't found")


def order():
    print("order")


def report():
    print("report")


def shutdown():
    print("shutdown")


options = {
    "espresso": order,
    "latte": order,
    "cappuccino": order,
    "report": report,
    "off": shutdown
}

if __name__ == '__main__':
    global_request = welcome_screen()
    process_request(global_request.lower())
