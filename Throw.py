import Dice

roll = "Yes"
while roll == "Yes" or roll =="y" or roll == "yes":
    print("Rolling Dice")
    print("Values are")
    Dice.Dice()
    roll = input("Roll again?")
