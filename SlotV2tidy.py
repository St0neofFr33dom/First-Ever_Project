from random import choice

Cherrybase_1 = 0
Melonbase_1 = 510
Rosebase_1 = 805
BTbase_1 = 902
GBbase_1 = 976
Cherrybase_2 = 0
Melonbase_2 = 410
Rosebase_2 = 705
BTbase_2 = 852
GBbase_2 = 951
Cherrybase_3 = 0
Melonbase_3 = 310
Rosebase_3 = 605
BTbase_3 = 802
GBbase_3 = 926
Cap = 1000
Wins = 1
Losses = 1
N_Cherry_Prob_2 = 0
N_Melon_Prob_2 = 0
N_Rose_Prob_2 = 0
N_BT_Prob_2 = 0
N_GB_Prob_2 = 0
N_Cherry_Prob_3 = 0
N_Melon_Prob_3 = 0
N_Rose_Prob_3 = 0
N_BT_Prob_3 = 0
N_GB_Prob_3 = 0

def newlimit(alo, naprob, nbprob, ncprob, ndprob, b, c, d, e):
    blo = int((naprob * 1000) + alo)
    clo = int((nbprob * 1000) + blo)
    dlo = int((ncprob * 1000) + clo)
    elo = int((ndprob * 1000) + dlo)
    b = blo
    c = clo
    d = dlo
    e = elo


def newprob(A, NA, B, NB, C, NC, D, ND, E, NE, Severity):
    NA = A + ((Modifier / 100) * Severity)
    NB = B * ((1 - A) / (1 - NA))
    NC = C * ((1 - A) / (1 - NA))
    ND = D * ((1 - A) / (1 - NA))
    NE = E * ((1 - A) / (1 - NA))



while True:
    # Determining the modifier for slot chance based on wins to losses
    Ratio = Wins / Losses
    Modifier = 1 / Ratio
    # Adjusting the limits
    Melonlo_1 = int(Melonbase_1 - (Modifier * 10))
    Roselo_1 = int(Rosebase_1 - (Modifier * 5))
    BTlo_1 = int(BTbase_1 - (Modifier * 2))
    GBlo_1 = int(GBbase_1 - Modifier)
    Melonlo_2 = int(Melonbase_2 - (Modifier * 10))
    Roselo_2 = int(Rosebase_2 - (Modifier * 5))
    BTlo_2 = int(BTbase_2 - (Modifier * 2))
    GBlo_2 = int(GBbase_2 - Modifier)
    Melonlo_3 = int(Melonbase_3 - (Modifier * 10))
    Roselo_3 = int(Rosebase_3 - (Modifier * 5))
    BTlo_3 = int(BTbase_3 - (Modifier * 2))
    GBlo_3 = int(GBbase_3 - Modifier)

# First slot is ready
    Cherryset_1 = set(range(Cherrybase_1, Melonlo_1))
    Melonset_1 = set(range(Melonlo_1, Roselo_1))
    Roseset_1 = set(range(Roselo_1, BTlo_1))
    BTset_1 = set(range(BTlo_1, GBlo_1))
    GBset_1 = set(range(GBlo_1, Cap))
    # Turning the limits into percentages
    Cherry_Prob_1 = (Melonlo_1 - Cherrybase_1) / 10
    Melon_Prob_1 = (Roselo_1 - Melonlo_1) / 10
    Rose_Prob_1 = (BTlo_1 - Roselo_1) / 10
    BT_Prob_1 = (GBlo_1 - BTlo_1) / 10
    GB_Prob_1 = (Cap - GBlo_1) / 10
    Cherry_Prob_2 = (Melonlo_2 - Cherrybase_2) / 10
    Melon_Prob_2 = (Roselo_2 - Melonlo_2) / 10
    Rose_Prob_2 = (BTlo_2 - Roselo_2) / 10
    BT_Prob_2 = (GBlo_2 - BTlo_2) / 10
    GB_Prob_2 = (Cap - GBlo_2) / 10
    Cherry_Prob_3 = (Melonlo_3 - Cherrybase_3) / 10
    Melon_Prob_3 = (Roselo_3 - Melonlo_3) / 10
    Rose_Prob_3 = (BTlo_3 - Roselo_3) / 10
    BT_Prob_3 = (GBlo_3 - BTlo_3) / 10
    GB_Prob_3 = (Cap - GBlo_3) / 10

    Slot_1 = {'Cherry': Cherryset_1, 'Melon': Melonset_1, 'Rose': Roseset_1, 'Blue Tit': BTset_1, 'Gold Bar': GBset_1}
    Spin = choice(range(1000))
    for result_1, number in Slot_1.items():
        if Spin in number:
            print(result_1)
            display_1 = result_1
    if display_1 == 'Cherry':
        newprob(Cherry_Prob_2, N_Cherry_Prob_2, Melon_Prob_2, N_Melon_Prob_2, Rose_Prob_2, N_Rose_Prob_2, BT_Prob_2,
                N_BT_Prob_2, GB_Prob_2, N_GB_Prob_2, 2)
        newlimit(Cherrybase_2, N_Cherry_Prob_2, N_Melon_Prob_2, N_Rose_Prob_2, N_BT_Prob_2, Melonlo_2, Roselo_2, BTlo_2,
                 GBlo_2)
        newprob(Cherry_Prob_3, N_Cherry_Prob_3, Melon_Prob_3, N_Melon_Prob_3, Rose_Prob_3, N_Rose_Prob_3, BT_Prob_3,
                N_BT_Prob_3, GB_Prob_3, N_GB_Prob_3, 2)
        newlimit(Cherrybase_3, N_Cherry_Prob_3, N_Melon_Prob_3, N_Rose_Prob_3, N_BT_Prob_3, Melonlo_3, Roselo_3, BTlo_3,
                 GBlo_3)
    elif display_1 == 'Melon':
        newprob(Melon_Prob_2, N_Melon_Prob_2, Cherry_Prob_2, N_Cherry_Prob_2, Rose_Prob_2, N_Rose_Prob_2, BT_Prob_2,
                N_BT_Prob_2, GB_Prob_2, N_GB_Prob_2, 1.75)
        newlimit(Cherrybase_2, N_Cherry_Prob_2, N_Melon_Prob_2, N_Rose_Prob_2, N_BT_Prob_2, Melonlo_2, Roselo_2, BTlo_2,
                 GBlo_2)
        newprob(Melon_Prob_3, N_Melon_Prob_3, Cherry_Prob_3, N_Cherry_Prob_3, Rose_Prob_3, N_Rose_Prob_3, BT_Prob_3,
                N_BT_Prob_3, GB_Prob_3, N_GB_Prob_3, 1.75)
        newlimit(Cherrybase_3, N_Cherry_Prob_3, N_Melon_Prob_3, N_Rose_Prob_3, N_BT_Prob_3, Melonlo_3, Roselo_3, BTlo_3,
                 GBlo_3)
    elif display_1 == 'Rose':
        newprob(Rose_Prob_2, N_Rose_Prob_2, Cherry_Prob_2, N_Cherry_Prob_2, Melon_Prob_2, N_Melon_Prob_2, BT_Prob_2,
                N_BT_Prob_2, GB_Prob_2, N_GB_Prob_2, 1.5)
        newlimit(Cherrybase_2, N_Cherry_Prob_2, N_Melon_Prob_2, N_Rose_Prob_2, N_BT_Prob_2, Melonlo_2, Roselo_2, BTlo_2,
                 GBlo_2)
        newprob(Rose_Prob_3, N_Rose_Prob_3, Cherry_Prob_3, N_Cherry_Prob_3, Melon_Prob_3, N_Melon_Prob_3, BT_Prob_3,
                N_BT_Prob_3, GB_Prob_3, N_GB_Prob_3, 1.5)
        newlimit(Cherrybase_3, N_Cherry_Prob_3, N_Melon_Prob_3, N_Rose_Prob_3, N_BT_Prob_3, Melonlo_3, Roselo_3, BTlo_3,
                 GBlo_3)
    elif display_1 == 'Blue Tit':
        newprob(BT_Prob_2, N_BT_Prob_2, Cherry_Prob_2, N_Cherry_Prob_2, Melon_Prob_2, N_Melon_Prob_2, Rose_Prob_2,
                N_Rose_Prob_2, GB_Prob_2, N_GB_Prob_2, 1.25)
        newlimit(Cherrybase_2, N_Cherry_Prob_2, N_Melon_Prob_2, N_Rose_Prob_2, N_BT_Prob_2, Melonlo_2, Roselo_2, BTlo_2,
                 GBlo_2)
        newprob(BT_Prob_3, N_BT_Prob_3, Cherry_Prob_3, N_Cherry_Prob_3, Melon_Prob_3, N_Melon_Prob_3, Rose_Prob_3,
                N_Rose_Prob_3, GB_Prob_3, N_GB_Prob_3, 1.25)
        newlimit(Cherrybase_3, N_Cherry_Prob_3, N_Melon_Prob_3, N_Rose_Prob_3, N_BT_Prob_3, Melonlo_3, Roselo_3, BTlo_3,
                 GBlo_3)
    elif display_1 == 'Gold Bar':
        newprob(GB_Prob_2, N_GB_Prob_2, Cherry_Prob_2, N_Cherry_Prob_2, Melon_Prob_2, N_Melon_Prob_2, Rose_Prob_2,
                N_Rose_Prob_2, BT_Prob_2, N_BT_Prob_2, 1)
        newlimit(Cherrybase_2, N_Cherry_Prob_2, N_Melon_Prob_2, N_Rose_Prob_2, N_BT_Prob_2, Melonlo_2, Roselo_2, BTlo_2,
                 GBlo_2)
        newprob(GB_Prob_3, N_GB_Prob_3, Cherry_Prob_3, N_Cherry_Prob_3, Melon_Prob_3, N_Melon_Prob_3, Rose_Prob_3,
                N_Rose_Prob_3, BT_Prob_3, N_BT_Prob_3, 1)
        newlimit(Cherrybase_3, N_Cherry_Prob_3, N_Melon_Prob_3, N_Rose_Prob_3, N_BT_Prob_3, Melonlo_3, Roselo_3, BTlo_3,
                 GBlo_3)

    Cherryset_2 = set(range(Cherrybase_2, Melonlo_2))
    Melonset_2 = set(range(Melonlo_2, Roselo_2))
    Roseset_2 = set(range(Roselo_2, BTlo_2))
    BTset_2 = set(range(BTlo_2, GBlo_2))
    GBset_2 = set(range(GBlo_2, Cap))
    Cherryset_3 = set(range(Cherrybase_3, Melonlo_3))
    Melonset_3 = set(range(Melonlo_3, Roselo_3))
    Roseset_3 = set(range(Roselo_3, BTlo_3))
    BTset_3 = set(range(BTlo_3, GBlo_3))
    GBset_3 = set(range(GBlo_3, Cap))

    Slot_2 = {'Cherry': Cherryset_2, 'Melon': Melonset_2, 'Rose': Roseset_2, 'Blue Tit': BTset_2, 'Gold Bar': GBset_2}
    Spin = choice(range(1000))
    for result_2, number in Slot_2.items():
        if Spin in number:
            display_2 = result_2

    Slot_3 = {'Cherry': Cherryset_3, 'Melon': Melonset_3, 'Rose': Roseset_3, 'Blue Tit': BTset_3, 'Gold Bar': GBset_3}
    Spin = choice(range(1000))
    for result_3, number in Slot_3.items():
        if Spin in number:
            display_3 = result_3

    if (display_1 == display_2) and (display_2 == display_3):
        print('Congratulations')
        Wins += 1
        input()
    else:
        print('Unlucky')
        Losses += 1
        input()
