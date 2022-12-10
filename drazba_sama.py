from auctionLogo import auction_logo
import os


print("Vítejte v programu na tichou aukci.")

bidders = {}
lets_continue = "ano"

#naplnění dictionary nabízejícími:

while lets_continue == "ano":
    name = input("Jaké je vaše jméno? ")
    bid = int(input("Jaká je vaše nabídka v dolarech? "))
    bidders[name] = bid
    lets_continue = input("Jsou další nabízející? Napište ano nebo ne: ")
    if lets_continue == "ne":
        os.system("clear")
        

#zjistit nejvyšší nabídku:
#highest_bid = 0
#winner = ""
#for key in bidders:
   # if bidders[key] > highest_bid:
    #    highest_bid = bidders[key]
     #   winner = key

#print(f"Vítězem tiché aukce je {winner} s konečným příhozem {highest_bid} dolarů.")   

print(auction_logo)


def highest_bid(bidders_dictionary):
    highest_bid = 0
    winner = ""
    for key in bidders_dictionary:
        if bidders_dictionary[key] > highest_bid:
            highest_bid = bidders_dictionary[key]
            winner = key

    print(f"Vítězem tiché aukce je {winner} s konečným příhozem {highest_bid} dolarů.")   


highest_bid(bidders)