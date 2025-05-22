import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 3

    def take_damage(self):
        self.health -= 1
        return self.health <= 0

class Game:
    def __init__(self):
        self.players = [Player("User"), Player("Dealer")]
        self.shotgun = [random.choice(['🔴', '🔵']) for _ in range(6)]
        self.current_player = 0
        self.current_round = 1

    def switch_player(self):
        self.current_player = 1 - self.current_player

    def shoot(self, target):
        shell = self.shotgun.pop(0)
        print(f"{self.players[self.current_player].name} fires at {target.name}... {shell}")

        if shell == '🔴':
            if target.take_damage():
                print(f"{target.name} is down! {self.players[self.current_player].name} wins!")
                return True
        elif target == self.players[self.current_player]:
            print("Lucky! You keep the turn.")
        else:
            self.switch_player()
        return False

    def use_magnifying_glass(self):
        print(f"Next shell: {self.shotgun[0]}")

    def getShells(self):
        return len(self.shotgun)
    
    def reload(self):
        self.shotgun = [random.choice(['🔴', '🔵']) for _ in range(6)]

    def play(self):
        print("Welcome to Buckshot Roulette!")
        while True:
            player = self.players[self.current_player]
            print(f"+++ Round {self.current_round} ++\n\n{player.name}'s turn - Health: {player.health}\n              Shells: {self.getShells()}")
            print("1: Shoot Yourself  2: Shoot Opponent  3: Use Magnifying Glass  4: Quit")
            choice = input("Choose: ")

            if choice == '1':
                if self.shoot(player): break
            elif choice == '2':
                if self.shoot(self.players[1 - self.current_player]): break
            elif choice == '3':
                self.use_magnifying_glass()
            elif choice == '4':
                print("Exiting game.")
                break
            
            self.current_round += 1

            if self.getShells() is 0:
                print("==============\nEmpty! Reloading...\n==============\n")
                self.reload()
        

        print("See you next time...")

if __name__ == "__main__":
    game = Game()
    game.play()
