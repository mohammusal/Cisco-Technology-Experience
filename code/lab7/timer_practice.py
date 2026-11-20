# Lab 7: Practice for the Quiz Game project
# Run this file after each TODO. It works even before you change anything.

import time

# TODO 1: Measure time. time.time() is the number of seconds since 1970.
print("Seconds since 1 January 1970:", time.time())
# Reaction game: remove the # in front of the 5 lines below.
# input("Press Enter, then press Enter again as fast as you can...")
# start_time = time.time()
# input("NOW!")
# seconds = time.time() - start_time
# print(f"Your reaction time: {round(seconds, 2)} seconds")

# TODO 2: Sort a list of (points, name) tuples, best first, and keep the top 3.
scores = [(2, "Ola"), (5, "Jan"), (-1, "Kuba"), (4, "Zosia"), (3, "Ania")]
print(sorted(scores))
# top = sorted(scores, reverse=True)[:3]
# place = 1
# for points, player in top:
#     print(f"{place}. {player} - {points} points")
#     place = place + 1
