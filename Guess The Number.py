import random as rd

class NumberGuessingGame:
    def __init__(self, players):
        self.bet=int(input("On how much bet you want to play: \n 100 \ 250 \ 500 : "))
        self.point=[100,250,500]
        self.players = players
        self.nopcp = [4, 6, 8, 10]
        self.attempts = {}  # Dictionary to keep track of attempts for each player

    def start_game(self):
        if self.players in self.nopcp:
            for j in range(self.players):
                print(f"Player number: {j + 1}")
                num = rd.randint(1, 100)
                i = 1
                print("---Game Started---")
                print("You have 5 chances to guess the number.")
                
                while i <= 5:
                    user_num = int(input("Guess the Number: "))
                    
                    if user_num == num:
                        print("You Won")
                        print("Correct Guess")
                        self.attempts[f"Player {j + 1}"] = i  # Store the number of attempts
                        break
                    
                    if i == 5:
                        print("You lost. The correct number is:", num)
                        self.attempts[f"Player {j + 1}"] = None  # Indicate that the player did not guess correctly
                        break
                    else:
                        if user_num > num:
                            print("Your number is bigger than the target number. Guess again.", 5 - i, "chances left")
                        else:
                            print("Your number is smaller than the target number. Guess again.", 5 - i, "chances left")
                    
                    i += 1
                
                print("---GAME OVER---")
            self.ranking()
            self.determine_winner()
        else:
            raise ValueError("Invalid value provided.")
    
    def determine_winner(self):
        # Determine the winner
        valid_attempts = {player: attempt for player, attempt in self.attempts.items() if attempt is not None}
        
        if valid_attempts:
            min_attempts = min(valid_attempts.values())
            self.winners = [player for player, attempt in valid_attempts.items() if attempt == min_attempts]
            print("\n---WINNER---")
            if len(self.winners) > 1:
                print(f"It's a tie! The winners are: {', '.join(self.winners)} with {min_attempts} attempts.")
            else:
                print(f"The winner is {self.winners[0]} with {min_attempts} attempts.")
            self.bet_points()
        else:
            print("No player guessed the number correctly.")

    def bet_points(self):
        if self.bet in self.point:
            self.points_= self.players * self.bet *(2.5/100)
            self.win_point= (self.players * self.bet) - self.points_

            if len(self.winners) > 1 :
                self.bet_dis = self.win_point / len(self.winners)
                print(f"The winners: {', '.join(self.winners)} get equal points as it's tie! {self.bet_dis} each.")
            else:
                print(f"{self.winners[0]} get {self.win_point}")

        else:
            raise ValueError("Invalid value provided.")
    
    def ranking(self):
        # Sort players by the number of attempts in ascending order
        self.player_attempts = sorted(self.attempts.items(), key=lambda x: x[1] if x[1] is not None else float('inf'))
        
        # Display the ranking
        print("\n--- RANKING ---")
        for rank, (player, attempts) in enumerate(self.player_attempts, start=1):
            if attempts is not None and attempts <= 5:
                print(f"Rank {rank}: {player} with {attempts} attempts")
            else:
                print(f"Rank {rank}: {player} did not guess the number")


# Example of creating and starting the game with 4 players
if __name__ == "__main__":
    players = int(input("With how many players do you want to play:\n 4 / 6 / 8 / 10 :")) 
    game = NumberGuessingGame(players)
    game.start_game()