import tkinter as tk
import random

class GuessNumberGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("GUESS THE NUMBER")
        self.geometry("400x300")
        self.configure(bg="#F5E1DA")  # Set background color

        # Center the window on the screen
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.winfo_width()) // 2
        y = (screen_height - self.winfo_height()) // 2
        self.geometry("+{}+{}".format(x, y))

        # Frame to hold the content
        self.content_frame = tk.Frame(self, bg="#F5E1DA")
        self.content_frame.pack(expand=True)

        self.start_label = tk.Label(self.content_frame, text="Enter the range for guessing:", bg="#F5E1DA", fg="#333", font=("Helvetica", 16))
        self.start_label.pack(pady=10)

        self.from_label = tk.Label(self.content_frame, text="From:", bg="#FF5A5F", fg="white", font=("Helvetica", 14))
        self.from_label.pack()

        self.from_entry = tk.Entry(self.content_frame, font=("Helvetica", 14))
        self.from_entry.pack()

        self.to_label = tk.Label(self.content_frame, text="To:", bg="#3D9970", fg="white", font=("Helvetica", 14))
        self.to_label.pack()

        self.to_entry = tk.Entry(self.content_frame, font=("Helvetica", 14))
        self.to_entry.pack()

        self.attempts_label = tk.Label(self.content_frame, text="Attempts:", bg="#0074D9", fg="white", font=("Helvetica", 14))
        self.attempts_label.pack()

        self.attempts_var = tk.StringVar()
        self.attempts_var.set("0")
        self.attempts_entry = tk.Entry(self.content_frame, textvariable=self.attempts_var, state="readonly", font=("Helvetica", 14))
        self.attempts_entry.pack()

        self.start_button = tk.Button(self.content_frame, text="Start Game", command=self.start_game, bg="#FF5A5F", fg="white", font=("Helvetica", 14, "bold"))
        self.start_button.pack(pady=20)

        self.message_label = tk.Label(self.content_frame, text="", bg="#F5E1DA", fg="#333", font=("Helvetica", 14, "bold"))
        self.message_label.pack()

        self.num = None
        self.attempts = 0

    def start_game(self):
        try:
            m = int(self.from_entry.get())
            n = int(self.to_entry.get())

            if m >= n:
                self.message_label.config(text="Invalid range. 'From' should be less than 'To.'", fg="#FF5A5F")
            else:
                self.num = random.randint(m, n)
                self.attempts = 0
                self.attempts_var.set(str(self.attempts))
                self.play_game()
        except ValueError:
            self.message_label.config(text="Invalid input. Please enter valid numbers.", fg="#FF5A5F")

    def play_game(self):
        def check_guess():
            try:
                guess = int(self.guess_entry.get())
                self.attempts += 1
                self.attempts_var.set(str(self.attempts))

                if guess == self.num:
                    self.message_label.config(text="Congratulations! You guessed correctly in {} attempts.".format(self.attempts), fg="#3D9970")
                elif guess < self.num:
                    self.message_label.config(text="Try again! The guess number is higher.", fg="#0074D9")
                else:
                    self.message_label.config(text="Try again! The guess number is lower.", fg="#0074D9")
            except ValueError:
                self.message_label.config(text="Invalid input. Please enter a valid number.", fg="#FF5A5F")

        self.start_label.pack_forget()
        self.from_label.pack_forget()
        self.from_entry.pack_forget()
        self.to_label.pack_forget()
        self.to_entry.pack_forget()
        self.attempts_label.pack_forget()
        self.attempts_entry.pack_forget()
        self.start_button.pack_forget()

        self.guess_label = tk.Label(self.content_frame, text="Guess a number:", bg="#F5E1DA", fg="#333", font=("Helvetica", 14))
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self.content_frame, font=("Helvetica", 14))
        self.guess_entry.pack()

        self.check_button = tk.Button(self.content_frame, text="Check", command=check_guess, bg="#FF5A5F", fg="white", font=("Helvetica", 14, "bold"))
        self.check_button.pack(pady=20)

if __name__ == "__main__":
    app = GuessNumberGame()
    app.mainloop()




'''import random
import math

n=int(input("Enter the second range :"))
num = random.randint(m,n)
chance=round(math.log(n-m+1, 2))
print("\n\tYou've only ",chance," chances to guess the integer!\n")
count=0
while count<chance:
     count=count+1
     guess =int(input('Guess a number:-'))
     if guess== num:
         print('Congratulations! you won the match in', count,'try')
         break     
     elif guess>num:
       print('You Guessed bigger number! ')
     elif guess<num:
         print('You Guessed smaller number!')
     if count>=chance:
         print('\n The number is:-',num)
         print('\nYou lose! & Better luck next time')'''

'''
import tkinter as tk
import random
import math

class NumberGuessGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Number Guessing Game")
        self.geometry("400x300")
        self.configure(bg="#F5E1DA")  # Set background color

        # Center the window on the screen
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.winfo_width()) // 2
        y = (screen_height - self.winfo_height()) // 2
        self.geometry("+{}+{}".format(x, y))

        self.range_label = tk.Label(self, text="Enter the first and second range:", bg="#F5E1DA", fg="#333", font=("Helvetica", 14))
        self.range_label.pack(pady=10)

        self.first_range_entry = tk.Entry(self, font=("Helvetica", 14))
        self.first_range_entry.pack(pady=5)

        self.second_range_entry = tk.Entry(self, font=("Helvetica", 14))
        self.second_range_entry.pack(pady=5)

        self.play_button = tk.Button(self, text="Play", command=self.play_game, bg="#FF5A5F", fg="white", font=("Helvetica", 14, "bold"))
        self.play_button.pack(pady=10)

        self.result_label = tk.Label(self, text="", bg="#F5E1DA", fg="#333", font=("Helvetica", 14, "bold"))
        self.result_label.pack(pady=20)

        self.num = 0
        self.chance = 0

    def play_game(self):
        try:
            first_range = int(self.first_range_entry.get())
            second_range = int(self.second_range_entry.get())
            if first_range >= second_range:
                raise ValueError("Invalid range. The second range should be greater than the first.")

            self.num = random.randint(first_range, second_range)
            self.chance = round(math.log(second_range - first_range + 1, 2))

            self.result_label.config(text="You've only {} chances to guess the integer!".format(self.chance), fg="#333")
        except ValueError as e:
            self.result_label.config(text=str(e), fg="red")

        self.guess_entry = tk.Entry(self, font=("Helvetica", 14))
        self.guess_entry.pack(pady=5)

        self.guess_button = tk.Button(self, text="Guess", command=self.check_guess, bg="#0074D9", fg="white", font=("Helvetica", 14, "bold"))
        self.guess_button.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            if guess == self.num:
                self.result_label.config(text="Congratulations! You won the match in {} tries.".format(self.chance), fg="#3D9970")
            elif guess > self.num:
                self.result_label.config(text="You Guessed a bigger number!", fg="#0074D9")
            elif guess < self.num:
                self.result_label.config(text="You Guessed a smaller number!", fg="#0074D9")

            if self.chance == 0:
                self.result_label.config(text="The number is: {}".format(self.num), fg="red")
                self.guess_button.config(state="disabled")
                self.guess_entry.config(state="disabled")
            else:
                self.chance -= 1
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid number.", fg="red")

if __name__ == "__main__":
    app = NumberGuessGame()
    app.mainloop()
'''
