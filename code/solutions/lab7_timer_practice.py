# Lab 7: Practice for the Quiz Game project - solution

import time

print("Seconds since 1 January 1970:", time.time())
input("Press Enter, then press Enter again as fast as you can...")
start_time = time.time()
input("NOW!")
seconds = time.time() - start_time
print(f"Your reaction time: {round(seconds, 2)} seconds")

scores = [(2, "Ola"), (5, "Jan"), (-1, "Kuba"), (4, "Zosia"), (3, "Ania")]
print(sorted(scores))
top = sorted(scores, reverse=True)[:3]
place = 1
for points, player in top:
    print(f"{place}. {player} - {points} points")
    place = place + 1
