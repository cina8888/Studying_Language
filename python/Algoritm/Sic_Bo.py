import random
import questionary

class SicBo:
    def __init__(self, budget, goal):
        self.budget = budget
        self.goal = goal
        self.chains = []

    def play(self):
        self.check_input()
        self.create_chains()
        while self.budget > 0 and self.budget < self.goal:
            menu = questionary.select(
                "Choose",
                choices = ["Play", "Chains"]
            ).ask()
            if (menu == "Play"):
                self.guest_next()
                print(f"Your new balance is {self.budget}")
            else: 
                for item in self.chains:
                    print(f'{item["type"]} - {item["sum"]} - {item["dice"]}')
        if self.budget >= self.goal:
            print(f"You reach your goals!!! Congratualation")
        else:
            print(f"Game Over!")
    def guest_next(self):
        bet = float(input("Please enter bet: "))
        while (bet <= 0 or bet > self.budget):
            bet = float(input(f"Please enter bet lower or equal to your wallet ({self.budget}$): "))
        tx_choice = questionary.select(
            "Choose Tai or Xiu:",
            choices=["Tai", "Xiu"]
        ).ask()
        result = self.check_next()
        last = self.chains[-1]
        print(f'{last["type"]} - {last["sum"]} - {last["dice"]}')
        if result == tx_choice.lower():
            print("You guessed correct!!!")
            self.budget += bet
        else:
            print("You guessed incorrect!!!")
            self.budget -= bet


    def check_next(self):
        item = self.roll_dice()

        self.chains.append(item)

        return item["type"].lower()
    
    def check_input(self):
        while (self.budget <= 0):
            self.budget = float(input("Your budget must be greater than 0. Please try again: "))
        while self.goal <= self.budget:
            self.goal = float(input("Your goal must be greater than your budget. Please try again: "))
        print(f"Your budget: {self.budget}$ - Your goal: {self.goal}$")

    def roll_dice(self):
        dice = [random.randint(1, 6) for _ in range(3)]
        total = sum(dice)

        result = "Tai" if total > 10 else "Xiu"

        return {
            "type": result,
            "sum": total,
            "dice": dice
        }
    
    def create_chains(self):
        for _ in range(10):
            self.chains.append(self.roll_dice())

if __name__ == "__main__":
    print("Welcome to SIC BO gameplay")
    money = float(input("Please type your budget: "))
    goal = float(input("Please type your aim: "))
    Nghia = SicBo(money, goal)
    Nghia.play()