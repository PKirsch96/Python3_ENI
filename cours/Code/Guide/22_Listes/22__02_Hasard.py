from random import choice, sample, shuffle

cartes = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
          "o", "p", "q", "r", "s", "t", "u", "v", "w"]
print(len(cartes))
print("Voici les cartes qui vous sont présentées: ", " ".join(cartes))

print("Vous en piochez une au hasard:", " ".join(choice(cartes)))
print("Vous en piochez cinq au hasard:", " ".join(sample(cartes, 5)))
shuffle(cartes)
print("Vous les mélangez:", " ".join(cartes))
print(len(cartes))
