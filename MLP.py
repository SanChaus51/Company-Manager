shop_stock = {
    "mouse": {"price": 600, "count": 5},
    "iphone": {"price": 45000, "count": 2},
    "gta": {"price": 1200, "count": 10},
}

user_balance = 2000
shopping_cart = []

print("--- Welcome to Call-center shop! ---")


while True:
    print(f"\n 💵 your balance: {user_balance} grn")
    print("menu team:")
    print("1 - show asort")
    print("2 - buy asort")
    print("3 - add money")
    print("4 - end work and take chek")

    choice = input("> Text number team: <")


    if choice == "1":
        print("\n open asort in storage")

        for name, info in shop_stock.items():
            print(f" - {name.upper()}: price: {info['price']} grn | ostatok: {info['count']} sht.")



    elif choice == "2":
        item_name = input("text name lower words:")


        if item_name in shop_stock:
            product = shop_stock[item_name]


            if product['count'] > 0:

                if user_balance >= product['price']:

                    product["count"] -= 1
                    user_balance -= product["price"]
                    shopping_cart.append(item_name)
                    print(f" you buy this asort {item_name}!")
                else:
                    print("X no money, go bank")
            else:
                print("X this asort doesn't in storage")
        else:
            print("X no item in asort shop.")

    elif choice == "3":

        money_input = input("text money add in card?:")
        if money_input.isdigit():
            user_balance += int(money_input)
            print(" balance succseful updated")
        else:
            print("X eror: need text number!")

    elif choice == "4":

        print("\n --- YOUR FINAL CHECK ---")
        if len(shopping_cart) > 0:
            print("You buy this item:")
            for item in shopping_cart:
                print(f"* {item}")
        else:
            print("X back is empty, you nothing buy.")
        print(f"last money in cart: ${user_balance} grn")
        print("thanks, for used us poslygi! Bye.")
        break
    else:
        print("X IDK this comand! try again")