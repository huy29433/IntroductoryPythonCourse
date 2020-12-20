import random

def randomWalk(countOfSteps, broadthLeftInSteps = None, broadthRightInSteps = None, biasToRight =  0):
    # -0.5 <= bias <= 0.5
    actualPosition = 0

    pStepRight = 0.5 + biasToRight
    pStepLeft = 1 - pStepRight

    choices = [-1, 1]
    distribution = [pStepLeft, pStepRight]
    for i in range(countOfSteps):
        if broadthLeftInSteps != None and actualPosition <= -broadthLeftInSteps:       ## == würde auch ausreichen
            actualPosition += 1
        elif broadthRightInSteps != None and actualPosition >= broadthRightInSteps:     ## == würde auch ausreichen
            actualPosition -= 1
        else:
            direction = random.choices(choices, distribution)[0]        # Gibt Liste mit 1 Element zurück
            actualPosition += direction

    return actualPosition




def main():
    countOfRepetitions = 1000
    countOfMaxSteps = 10
    results = {i : 0 for i in range(-countOfMaxSteps, countOfMaxSteps+1)}
    #results = dict() ## for Try, Except Initialisierung
    for i in range(countOfRepetitions):
        position = randomWalk(countOfMaxSteps)
        results[position] += 1
       # try:       ## Kann bei dieser Initialisierung gespart werden
        #    results[position] += 1
        #except KeyError:
         #   results[position] = 1
#    for i in sorted(results):
#        print(f"{i} \t {results[i]}")

    scaleFactor = 10

    for i in range(-countOfMaxSteps, countOfMaxSteps+1):
        print(f"{i:^5}" + results[i]%scaleFactor*"#")



if __name__ == "__main__":
    main()
