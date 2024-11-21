import random as rand

# Assumptions:
# Everyone plays at a high level
# In an ideally balanced environment, you have a 50/50 chance of winning each PvP fight
# no Genie

class Run():
    def __init__(self):
        # VARIABLES
        self.day = 1
        self.prestige = 20
        self.cheat_death = True
        self.wins = 0

# CONSTANTS
BRONZE_WIN = 4
SILVER_WIN = 7
GOLD_WIN = 10
PERFECT_PRESTIGE = 20

# PARAMS
NUM_RUNS = 10000000
WIN_RATE = 50

data = []
print(f"Simulating {NUM_RUNS} runs with a {WIN_RATE}% win rate per PvP match")
print("Starting simulation...")

while(len(data) < NUM_RUNS):
    run = Run()
    while(run.prestige > 0 and run.wins < 10):
        pvp_roll = rand.randint(1, 100)
        pvp_is_win = pvp_roll >= WIN_RATE
        
        if pvp_is_win:
            run.wins += 1
        else:
            run.prestige -= run.day
            if run.prestige < 0 and run.cheat_death:
                run.prestige = 1
                run.cheat_death = False

        run.day += 1
    # <- endwhile ->
    data.append(run)
# <- endwhile ->

# DATA PROCESSING
win_distribution = 11 * [0]
gold_win_percentage = 0
silver_win_percentage = 0
bronze_win_percentage = 0
no_win_percentage = 0
gold_prestige_distribution = 21 * [0]

for run in data:
    win_distribution[run.wins] += 1
    gold_prestige_distribution[run.prestige] += 1 if run.wins == 10 else 0
gold_win_percentage = win_distribution[GOLD_WIN] / NUM_RUNS
silver_win_percentage = sum(win_distribution[SILVER_WIN : GOLD_WIN]) / NUM_RUNS
bronze_win_percentage = sum(win_distribution[BRONZE_WIN : SILVER_WIN]) / NUM_RUNS
no_win_percentage = sum(win_distribution[0: BRONZE_WIN]) / NUM_RUNS


print("...Simulation complete.")
print()
print("Results:")
print()
print("Here is the win distribution data:")
for i in range(11):
    print(f"\t{win_distribution[i]}")
print()
print(f"This data suggests that {gold_win_percentage * 100}% of runs reach gold")
print(f"\t{silver_win_percentage * 100}% of runs stop at silver")
print(f"\t{bronze_win_percentage * 100}% of runs end at bronze")
print(f"\tand {no_win_percentage * 100}% of runs have an unfortunate end")
print()
print("Here is the prestige distrubution data for gold runs:")
for i in range(21):
    print(f"\t{gold_prestige_distribution[i]}")