raw_input : str = None

with open("input") as fd:
  raw_input = fd.read()

# parsing raw_input

matches = [line.split(" ") for line in raw_input.split("\n")]


(opp_rock, opp_paper, opp_scissors) = ('A', 'B', 'C')
(play_rock, play_paper, play_scissors) = ('X', 'Y', 'Z')

mapping = {
  "A" : 1,
  "B" : 2,
  "C" : 3,
  "X" : 1,
  "Y" : 2,
  "Z" : 3
}

"""
The score for a single round is the score for the shape you selected 
(1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the
outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
"""

def match(opp, player):
  round_score = 0

  # common mapping
  opp_hand = mapping[opp]
  player_hand = mapping[player]

  hands = [opp_hand, player_hand]

  shape_score = player_hand
  round_score += shape_score

  if opp_hand == player_hand:
    # draw
    round_score += 3
    return round_score

  match hands:
    case [2, 1]:
      # opp paper and player rock LOSS
      round_score += 0
    case [1, 2]:
      # opp rock and player paper VICTORY
      round_score += 6
    case [1, 3]:
      # LOSS
      round_score += 0
    case [3, 1]:
      # WIN
      round_score += 6
    case [3, 2]:
      # LOSS scissors vs Paper
      round_score += 0
    case [2, 3]:
      # WIN
      round_score += 6

  return round_score

total_score = 0
for r in matches:
  (opp, player) = r
  score = match(opp, player)
  total_score += score

print("r1:",total_score)


# round 2 

# Anyway, the second column says how the round needs to end:
# X means you need to lose,
# Y means you need to end the round in a draw, and
# Z means you need to win. Good luck!"

player_hands = ["_", "X", "Y", "Z"]

def gen_matches(opp, signal):
  # common mapping
  score = 0

  opp_hand = mapping[opp]
  player_hand = mapping[player]

  if signal == "Z":
    # win
    if opp_hand == 1: # rock
      player_hand = 2
    if opp_hand == 2: # paper
      player_hand = 3
    if opp_hand == 3: # scissor
      player_hand = 1
    score += 6

  if signal == "Y":
    # draw
    player_hand = opp_hand
    score += 3
  if signal == "X":
    # lose
    if opp_hand == 1: # rock
      player_hand = 3
    if opp_hand == 2: # paper
      player_hand = 1
    if opp_hand == 3: # scissor
      player_hand = 2
    score += 0

  score += player_hand

  # fuck we didnt even need to generate this whole thing !

  return score


total_score = 0
for r in matches:
  (opp, player) = r
  score = gen_matches(opp, player)
  total_score += score

print("r2:", total_score)
