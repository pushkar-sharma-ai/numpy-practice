import tkinter as tk
from tkinter import ttk
import random


# ==========================================
# GAME VARIABLES
# ==========================================

secret_number = 0
max_number = 10
attempts = 3
total_score = 0
level_bonus = 1

rounds_won = 0
rounds_lost = 0

time_left = 20
timer_id = None

game_active = False


# ==========================================
# LOAD LEADERBOARD
# ==========================================

def load_leaderboard():

    leaderboard = []

    try:
        file = open("leaderboard.txt", "r")

        for line in file:

            name, score = line.strip().split(",")

            leaderboard.append(
                [name, int(score)]
            )

        file.close()

    except FileNotFoundError:
        pass

    return leaderboard


# ==========================================
# SAVE LEADERBOARD
# ==========================================

def save_leaderboard():

    global leaderboard

    leaderboard.sort(
        key=lambda x: x[1],
        reverse=True
    )

    leaderboard = leaderboard[:5]

    file = open("leaderboard.txt", "w")

    for player in leaderboard:

        file.write(
            player[0]
            + ","
            + str(player[1])
            + "\n"
        )

    file.close()


# ==========================================
# DISPLAY LEADERBOARD
# ==========================================

def display_leaderboard():

    leaderboard_text.delete(
        "1.0",
        tk.END
    )

    leaderboard.sort(
        key=lambda x: x[1],
        reverse=True
    )

    top_players = leaderboard[:5]

    if len(top_players) == 0:

        leaderboard_text.insert(
            tk.END,
            "No scores yet!"
        )

        return

    rank = 1

    for player in top_players:

        leaderboard_text.insert(
            tk.END,
            str(rank)
            + ". "
            + player[0]
            + " - "
            + str(player[1])
            + "\n"
        )

        rank += 1


# ==========================================
# TIMER
# ==========================================

def start_timer():

    global time_left
    global timer_id

    time_left = 20

    timer_label.config(
        text="⏱️ Time: 20"
    )

    progress["value"] = 200

    timer_id = window.after(
        2000,
        update_timer
    )


def update_timer():

    global time_left
    global timer_id

    if game_active:

        time_left -= 1

        timer_label.config(
            text="⏱️ Time: " + str(time_left)
        )

        progress["value"] = time_left * 20

        if time_left <= 0:

            lose_round(
                "⏰ Time Up!"
            )

        else:

            timer_id = window.after(
                2000,
                update_timer
            )


# ==========================================
# START ROUND
# ==========================================

def start_game(level):

    global secret_number
    global max_number
    global attempts
    global level_bonus
    global game_active
    global timer_id

    player_name = name_entry.get().strip()

    if player_name == "":

        result_label.config(
            text="❌ Enter your name first!"
        )

        return


    # Stop previous timer

    if timer_id is not None:

        window.after_cancel(timer_id)

        timer_id = None


    attempts = 3
    game_active = True


    if level == "Easy":

        max_number = 10
        level_bonus = 1

    elif level == "Medium":

        max_number = 50
        level_bonus = 2

    else:

        max_number = 100
        level_bonus = 3


    secret_number = random.randint(
        1,
        max_number
    )


    level_label.config(
        text="Level: " + level
    )

    range_label.config(
        text="Guess between 1 and "
        + str(max_number)
    )

    attempts_label.config(
        text="❤️ Attempts: 3"
    )

    result_label.config(
        text="🎮 Round Started!"
    )

    guess_entry.delete(
        0,
        tk.END
    )

    guess_button.config(
        state="normal"
    )


    start_timer()


# ==========================================
# CHECK GUESS
# ==========================================

def check_guess():

    global attempts
    global total_score
    global rounds_won
    global game_active
    global timer_id


    if not game_active:

        result_label.config(
            text="Select a difficulty first!"
        )

        return


    try:

        guess = int(
            guess_entry.get()
        )

    except ValueError:

        result_label.config(
            text="❌ Enter numbers only!"
        )

        return


    if guess < 1 or guess > max_number:

        result_label.config(
            text="⚠️ Number must be 1 - "
            + str(max_number)
        )

        return


    # ======================================
    # CORRECT ANSWER
    # ======================================

    if guess == secret_number:

        if attempts == 3:
            round_score = 100

        elif attempts == 2:
            round_score = 70

        else:
            round_score = 40


        round_score *= level_bonus

        total_score += round_score

        rounds_won += 1

        game_active = False


        if timer_id is not None:

            window.after_cancel(
                timer_id
            )

            timer_id = None


        result_label.config(
            text="🎉 Correct! +"
            + str(round_score)
            + " points"
        )


        score_label.config(
            text="⭐ Score: "
            + str(total_score)
        )


        stats_label.config(
            text="Wins: "
            + str(rounds_won)
            + " | Losses: "
            + str(rounds_lost)
        )


        guess_button.config(
            state="disabled"
        )

        return


    # ======================================
    # WRONG ANSWER
    # ======================================

    attempts -= 1


    attempts_label.config(
        text="❤️ Attempts: "
        + str(attempts)
    )


    if attempts == 0:

        lose_round(
            "💀 No attempts left!"
        )

        return


    if guess < secret_number:

        result_label.config(
            text="📈 Try a BIGGER number!"
        )

    else:

        result_label.config(
            text="📉 Try a SMALLER number!"
        )


    guess_entry.delete(
        0,
        tk.END
    )


# ==========================================
# LOSE ROUND
# ==========================================

def lose_round(message):

    global rounds_lost
    global game_active
    global timer_id

    game_active = False

    rounds_lost += 1


    if timer_id is not None:

        try:
            window.after_cancel(
                timer_id
            )

        except:
            pass

        timer_id = None


    result_label.config(
        text=message
        + "\nNumber was "
        + str(secret_number)
    )


    stats_label.config(
        text="Wins: "
        + str(rounds_won)
        + " | Losses: "
        + str(rounds_lost)
    )


    guess_button.config(
        state="disabled"
    )


# ==========================================
# SAVE CURRENT SCORE
# ==========================================

def save_score():

    player_name = name_entry.get().strip()

    if player_name == "":

        result_label.config(
            text="❌ Enter your name!"
        )

        return


    leaderboard.append(
        [player_name, total_score]
    )

    save_leaderboard()

    display_leaderboard()


    result_label.config(
        text="🏆 Score Saved!"
    )


# ==========================================
# RESTART COMPLETE GAME
# ==========================================

def restart_game():

    global total_score
    global rounds_won
    global rounds_lost
    global game_active
    global timer_id


    if timer_id is not None:

        try:
            window.after_cancel(
                timer_id
            )

        except:
            pass

        timer_id = None


    total_score = 0
    rounds_won = 0
    rounds_lost = 0

    game_active = False


    score_label.config(
        text="⭐ Score: 0"
    )

    stats_label.config(
        text="Wins: 0 | Losses: 0"
    )

    attempts_label.config(
        text="❤️ Attempts: 3"
    )

    timer_label.config(
        text="⏱️ Time: 10"
    )

    progress["value"] = 100

    level_label.config(
        text="Level: None"
    )

    range_label.config(
        text="Select difficulty"
    )

    result_label.config(
        text="Game Restarted 🎮"
    )

    guess_entry.delete(
        0,
        tk.END
    )

    guess_button.config(
        state="disabled"
    )


# ==========================================
# QUIT GAME
# ==========================================

def quit_game():

    window.destroy()


# ==========================================
# LOAD SCORES
# ==========================================

leaderboard = load_leaderboard()


# ==========================================
# WINDOW
# ==========================================

window = tk.Tk()

window.title(
    "Guess The Number - Version 7"
)

window.geometry(
    "600x750"
)


# ==========================================
# TITLE
# ==========================================

title_label = tk.Label(
    window,
    text="🎮 GUESS THE NUMBER 🎮",
    font=("Arial", 22, "bold")
)

title_label.pack(
    pady=15
)


# ==========================================
# PLAYER NAME
# ==========================================

tk.Label(
    window,
    text="Player Name:",
    font=("Arial", 12)
).pack()


name_entry = tk.Entry(
    window,
    font=("Arial", 14),
    justify="center"
)

name_entry.pack(
    pady=5
)


# ==========================================
# DIFFICULTY BUTTONS
# ==========================================

tk.Label(
    window,
    text="Choose Difficulty",
    font=("Arial", 14, "bold")
).pack(
    pady=10
)


button_frame = tk.Frame(
    window
)

button_frame.pack()


tk.Button(
    button_frame,
    text="Easy",
    width=10,
    command=lambda: start_game("Easy")
).grid(
    row=0,
    column=0,
    padx=5
)


tk.Button(
    button_frame,
    text="Medium",
    width=10,
    command=lambda: start_game("Medium")
).grid(
    row=0,
    column=1,
    padx=5
)


tk.Button(
    button_frame,
    text="Hard",
    width=10,
    command=lambda: start_game("Hard")
).grid(
    row=0,
    column=2,
    padx=5
)


# ==========================================
# GAME INFO
# ==========================================

level_label = tk.Label(
    window,
    text="Level: None",
    font=("Arial", 12)
)

level_label.pack(
    pady=10
)


range_label = tk.Label(
    window,
    text="Select difficulty"
)

range_label.pack()


attempts_label = tk.Label(
    window,
    text="❤️ Attempts: 3"
)

attempts_label.pack(
    pady=5
)


score_label = tk.Label(
    window,
    text="⭐ Score: 0",
    font=("Arial", 14, "bold")
)

score_label.pack(
    pady=5
)


stats_label = tk.Label(
    window,
    text="Wins: 0 | Losses: 0"
)

stats_label.pack()


# ==========================================
# TIMER
# ==========================================

timer_label = tk.Label(
    window,
    text="⏱️ Time: 10",
    font=("Arial", 12, "bold")
)

timer_label.pack(
    pady=10
)


progress = ttk.Progressbar(
    window,
    length=300,
    maximum=100
)

progress["value"] = 100

progress.pack()


# ==========================================
# GUESS INPUT
# ==========================================

guess_entry = tk.Entry(
    window,
    font=("Arial", 18),
    justify="center",
    width=12
)

guess_entry.pack(
    pady=15
)


guess_button = tk.Button(
    window,
    text="SUBMIT GUESS",
    font=("Arial", 12, "bold"),
    command=check_guess,
    state="disabled"
)

guess_button.pack()


# ==========================================
# RESULT
# ==========================================

result_label = tk.Label(
    window,
    text="Enter name and select difficulty 👆",
    font=("Arial", 12)
)

result_label.pack(
    pady=15
)


# ==========================================
# CONTROL BUTTONS
# ==========================================

control_frame = tk.Frame(
    window
)

control_frame.pack(
    pady=5
)


tk.Button(
    control_frame,
    text="💾 Save Score",
    command=save_score
).grid(
    row=0,
    column=0,
    padx=5
)


tk.Button(
    control_frame,
    text="🔄 Restart",
    command=restart_game
).grid(
    row=0,
    column=1,
    padx=5
)


tk.Button(
    control_frame,
    text="❌ Quit",
    command=quit_game
).grid(
    row=0,
    column=2,
    padx=5
)


# ==========================================
# LEADERBOARD
# ==========================================

tk.Label(
    window,
    text="🏆 TOP 5 LEADERBOARD",
    font=("Arial", 14, "bold")
).pack(
    pady=15
)


leaderboard_text = tk.Text(
    window,
    width=30,
    height=6,
    font=("Arial", 11)
)

leaderboard_text.pack()


display_leaderboard()


# ==========================================
# RUN GAME
# ==========================================

window.mainloop()