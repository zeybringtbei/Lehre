from colorama import init, Fore, Style

"""
    Minimum Working Example (MWE) für die Greedy Heuristik zur Lösung des Set Cover Problems 
    Übung: Supply Chain Management
"""

i = 1



def print_data(H_s, S_o, S):
    global i

    print(Style.BRIGHT + Fore.GREEN + "Iteration {}:".format(i) + Style.RESET_ALL)
    print(f"---------------------------")
    print(Style.BRIGHT + "Ungeöffnete Standorte: Sortierung" + Style.RESET_ALL)
    for p in H_s:
        print("{:<10}: |H_s| = {:<4}, H_s = {}".format(p[0], len(p[1]), p[1]))
    print(f"---------------------------")
    print(Style.BRIGHT + "Geöffnete Standorte:" + Style.RESET_ALL)
    print(S_o)
    print(Style.BRIGHT + "Verbleibende unbelieferte Kunden:" + Style.RESET_ALL)
    print(H)
    print(f"---------------------------\n")

    i += 1


# Gibt an welches CrossDock welche Händler beliefern kann
haendler = {
    "Köln": ["Köln", "Bonn", "Aachen", "Leverkusen", "Mönchengladbach", "Düsseldorf"],
    "Düsseldorf": ["Düsseldorf", "Mönchengladbach", "Duisburg", "Wuppertal", "Leverkusen"],
    "Dortmund": ["Dortmund", "Duisburg", "Wuppertal", "Essen", "Bochum"],
    "Münster": ["Münster", "Gütersloh", "Bielefeld"],
    "Bielefeld": ["Bielefeld", "Münster", "Gütersloh", "Lemgo", "Paderborn"],
    "Paderborn": ["Paderborn", "Delbrück", "Lippstadt"]
}

# unbelieferte Händler (initial alle)
H = ["Aachen", "Essen", "Bielefeld", "Paderborn", "Bochum", "Leverkusen",
     "Düsseldorf", "Münster", "Gütersloh", "Lippstadt", "Wuppertal", "Dortmund",
     "Delbrück", "Duisburg", "Köln", "Mönchengladbach", "Lemgo", "Bonn"]

# Geschlossene Standorte (initial alle)
S = ["Köln", "Düsseldorf", "Dortmund", "Münster", "Bielefeld", "Paderborn"]

# Geöffnete Standorte (initial leer)
S_o = []

# Solange es noch unbelieferte Händler gibt...
while len(H) > 0:

    # Bestimmte welches ungeöffnete CrossDock noch welche unbelieferten Händler beliefern kann
    H_s = []
    for s in S:
        pair = (s, [h for h in haendler[s] if h in H])
        H_s.append(pair)
    #H_s = [(s, [h for h in haendler[s] if h in H]) for s in S]

    # Sortiere absteigend
    H_s.sort(key=lambda pair: len(pair[1]), reverse=True)

    # Öffnet Standort s (erster Eintrag gemäß Sortierung) und entfernt s aus S
    s = H_s[0]
    S_o.append(s[0])
    S.remove(s[0])

    # Entfernt neubelieferte Kunden aus H
    for h in s[1]:
        H.remove(h)
    print_data(H_s, S_o, H)

print(Style.BRIGHT + Fore.GREEN + "\nLÖSUNG" + Style.RESET_ALL)
print(f"---------------------------")
print(Style.BRIGHT + "Geöffnete Standorte:" + Style.RESET_ALL)
print(S_o)
print(Style.BRIGHT + "Nicht geöffnete Standorte:" + Style.RESET_ALL)
print(S)
print(f"---------------------------\n")
