from logo import logo
from dict import resources, MENU, money_bag


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
            return options[i](request)
    print("The option you selected wasn't found")
    return {"state": True}


def order(request):
    order_dict = MENU[request]
    order_dict["state"]=True
    return order_dict


def report(request):
    for i in resources:
        print(f"{i} at {current_resources[i]}")
    return {"state": True}


def shutdown(request):
    shutdown_dict = {}
    shutdown_dict["state"] = False
    return shutdown_dict


def coin_counter(counter_coin):

    if counter_coin in money_bag:
        return money_bag[counter_coin]
    else:
        print("that's not a real coin...")
        return 0


def ask_for_payment(payment_dict, payment_resources):
    coins=[]
    payment_amount = payment_dict["cost"]*100
    while sum(coins) < payment_amount:
        print(f"I need {payment_amount-sum(coins)} cent(s)")
        new_coin = input("What coin are you inserting")
        coins.append(coin_counter(new_coin))
    print("payment complete")


def enough_supply(supply_dict, supply_resources):
    for i in supply_dict["ingredients"]:
        if supply_resources[i] < supply_dict["ingredients"][i]:
            print("out of stock")
            return False
    return True

options = {
    "espresso": order,
    "latte": order,
    "cappuccino": order,
    "report": report,
    "off": shutdown
}

return_dict = {
    "state": True
}

if __name__ == '__main__':

    current_resources = resources
    while return_dict["state"]:
        global_request = welcome_screen()
        return_dict = process_request(global_request.lower())
        if 'ingredients' in return_dict:
            if enough_supply(return_dict, current_resources):
                current_resources = ask_for_payment(return_dict, current_resources)
                current_resources = prepare_coffe(return_dict, current_resources)