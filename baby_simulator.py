from random import choice

questions = ("why sky is blue? ", "why roses are red? ", "why there are so many people on earth? ")
question = choice(questions)

answer = input (question).lower().strip()

while answer != ("just because"):
    answer = input ("but why?:").lower().strip()

print ( "Oh..okay")
    
    
    
