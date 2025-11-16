#TASK 1
import re
import pandas as pd

with open(r"C:/Users/Chari/WorkspacePY/NLP/Exercise_1/magic.txt", "r", encoding="utf8") as f:
    lines = f.readlines()

cards = []
pattern = r"CardName:\s*(.*?)\s*CardCost:\s*(.*?)\s*CardType:\s*(.*?)\s*CardEffect:\s*(.*)$"

for line in lines:
    line = line.strip()
    if not line:
        continue
    card = {
        "CardName":  re.search(pattern, line).group(1),
        "CardCost":  re.search(pattern, line).group(2),
        "CardType":  re.search(pattern, line).group(3),
        "CardEffect": re.search(pattern, line).group(4)
    }
    cards.append(card)

df = pd.DataFrame(cards)
print(df.head(), "\nTotal cards:", len(df))

with open("magic_cards.txt", "w", encoding="utf8") as out:
    for card in cards:
        out.write(f"CardName: {card['CardName']}\n")
        out.write(f"CardCost: {card['CardCost']}\n")
        out.write(f"CardType: {card['CardType']}\n")
        out.write(f"CardEffect: {card['CardEffect']}\n")
        out.write("\n")  


#TASK 2
with open(r"C:/Users/Chari/WorkspacePY/NLP/Exercise_1/magic.txt", "r", encoding="utf8") as f:
    text = f.read()
card_lines = text.strip().split("\n")
print(card_lines[:5])  

#TASK 3
cards_data = []
pattern = r"CardName:\s*(.*?)\s*CardCost:\s*(.*?)\s*CardType:\s*(.*?)\s*CardEffect:\s*(.*)$"

for card in card_lines:
    match = re.search(pattern, card)
    if match:
        card_info = {
            "Name": match.group(1),
            "Cost": match.group(2),
            "Type": match.group(3),
            "Effect": match.group(4)
        }
        cards_data.append(card_info)

df_cards = pd.DataFrame(cards_data)
print(df_cards.head())

#TASK 4
types_to_count = ["Creature", "Sorcery", "Instant", "Enchantment", "Artifact"]

type_counts = {}
for t in types_to_count:
    type_counts[t] = df_cards["Type"].str.contains(t, regex=False).sum()

most_common_type = max(type_counts, key=type_counts.get)
print("Counts:", type_counts, "\nMost frequent type:", most_common_type)

#TASK 4 Counter Method
from collections import Counter

type_list = " ".join(df_cards["Type"].dropna()).split()
type_counter = Counter(type_list)
type_counts = {t: type_counter[t] for t in types_to_count}

most_common_type = max(type_counts, key=type_counts.get)
print("Most frequent:", most_common_type, "\nCounts:", type_counts)
