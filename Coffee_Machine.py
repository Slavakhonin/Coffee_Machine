class Coffee_Machine():  
    
    def __init__(self):
        self.current_water = 400
        self.current_milk = 540
        self.current_beans = 120
        self.current_cups = 9
        self.current_money = 550

    
    def status(self):
        print("The coffee machine has:")
        print(str(self.current_water) + " of water")
        print(str(self.current_milk) + " of milk")
        print(str(self.current_beans) + " of coffee beans")
        print(str(self.current_cups) + " of disposable cups")
        print(str(self.current_money) + " of money")


    def take(self):
        #global self.current_money
        print("I gave you $" + str(self.current_money))
        self.current_money = 0



    def fill(self):
        #global current_water
        #global current_milk
        #global current_beans
        #global current_cups
        print("Write how many ml of water do you want to add:")
        water = input()
        self.current_water += int(water)
        print("Write how many ml of milk do you want to add:")
        milk = input()
        self.current_milk += int(milk)
        print("Write how many grams of coffee beans do you want to add:")
        beans = input()
        self.current_beans += int(beans)
        print("Write how many disposable cups of coffee do you want to add:")
        cups = input()
        self.current_cups += int(cups)


    def buy(self):
        #global current_water
        #global current_milk
        #global current_beans
        #global current_cups
        #global current_money
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        choice = input()
        if choice == "1":
            self.current_water -= 250
            self.current_beans -= 16
            self.current_money += 4
            self.current_cups -= 1
        elif choice == "2":
            if self.current_water - 350 < 0:
                print("Sorry, not enough water!")
                self.menu()
            else:
                print("I have enough resources, making you a coffee!")
                self.current_water -= 350
            self.current_milk -= 75
            self.current_beans -= 20
            self.current_money += 7
            self.current_cups -= 1
        elif choice == "3":
            self.current_water -= 200
            self.current_milk -= 100
            self.current_beans -= 12
            self.current_money += 6
            self.current_cups -= 1
        elif choice == "back":
            self.menu()

    def menu(self):
        action = ""
        while action != "exit":
            print("Write action (buy, fill, take, remaining, exit):")

            action = str(input())

            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.status()
            elif action == "exit":
                exit()
            else:
                print("Please input the right value.")


nescafe = Coffee_Machine()
nescafe.menu()
