#####When you go to restaurants in London you might see a bunch of people in restaurants wearing suits like banker types and @ time time they need to pay their bill you see everybody pull out their business cards and put it into a bowl. So What's going on it's apparently a game Where the rich banker type play like Russian roulette with the bill so everybody puts their business cards in and the person whose the card is picked up has to pay the bill for every body's bill that's crazy but it's What it is ;)
###This App replicates this random Bill Game with Code @ we are able to type a list of people separated by commas and the Banker Roulette App will pic one random name and say the Chosen Person is going to pay the meal today! ;)


#Split string method
nameString = input("Give me everybody's names, separated by comma: ")
names = nameString.split(",")
## Don't change this code above
##Let's write our code below this line
####Now we have to figure out how to pick a random name from this list and of course this list canchange

###That's the easy way to solve this problem importing random and using python's random.choice() function
import random
chosenName = random.choice(names)

print(chosenName,"is going to pay the meal today!")

####The hard way to solve this problem would be
###Get the number total in the list
###numItems = len(names)
###Genarate random numbers between 0 and the last index
##randomChoice = random.randint(0,numItems - 1)
###personWhoWillPay = names[randomChoice]
