def sort_poker(john, uncle):

    # gets the correct order of suits from the uncle
    suits = []
    for i in uncle:
        if i == 'S':
            if 'S' not in suits:
                suits.append('S')
        if i == 'H':
            if 'H' not in suits:
                suits.append('H')
        if i == 'D':
            if 'D' not in suits:
                suits.append('D')
        if i == 'C':
            if 'C' not in suits:
                suits.append('C')
    
    # creates a list of the cards in john's hand
    diamonds=[]
    spades=[]
    hearts=[]
    clubs=[] 
    for i in range(len(john)):
        if i < len(john)-2:
            if john[i] == 'S' and john[i+2] == '0':
                spades.append(john[i]+john[i+1]+john[i+2])
            if john[i] == 'H' and john[i+2] == '0':
                hearts.append(john[i]+john[i+1]+john[i+2])
            if john[i] == 'D' and john[i+2] == '0':
                diamonds.append(john[i]+john[i+1]+john[i+2])
            if john[i] == 'C' and john[i+2] == '0':
                clubs.append(john[i]+john[i+1]+john[i+2])
            
            if john[i] == 'S' and john[i+2] != '0':
                spades.append(john[i]+john[i+1])
            if john[i] == 'H' and john[i+2] != '0':
                hearts.append(john[i]+john[i+1])
            if john[i] == 'D' and john[i+2] != '0':
                diamonds.append(john[i]+john[i+1])
            if john[i] == 'C' and john[i+2] != '0':
                clubs.append(john[i]+john[i+1])
        else:  
            if john[i] == 'S':
                spades.append(john[i]+john[i+1])
            if john[i] == 'H':
                hearts.append(john[i]+john[i+1])
            if john[i] == 'D':
                diamonds.append(john[i]+john[i+1])
            if john[i] == 'C':
                clubs.append(john[i]+john[i+1])
    
    # sorts the cards by number
    spades=xSort(spades)
    hearts=xSort(hearts)
    diamonds=xSort(diamonds)
    clubs=xSort(clubs)
    
    # append the cards to the results string in the suit order of the uncle's hand
    results=""
    for i in suits:
        if i == 'S':
            for j in spades:
                results+=j
        if i == 'H':
            for j in hearts:
                results+=j
        if i == 'D':
            for j in diamonds:
                results+=j
        if i == 'C':
            for j in clubs:
                results+=j          
    return results

# sorts based on weight of the card
def xSort(list):
        weights = []
        for i in list:
            if len(i) == 2:
                if i[1] == '1':
                    weight = 1
                if i[1] == '2':
                    weight = 2
                if i[1] == '3':
                    weight = 3
                if i[1] == '4':
                    weight = 4
                if i[1] == '5':
                    weight = 5
                if i[1] == '6':
                    weight = 6
                if i[1] == '7':
                    weight = 7
                if i[1] == '8':
                    weight = 8
                if i[1] == '9':
                    weight = 9
                if i[1] == 'J':
                    weight = 11
                if i[1] == 'Q':
                    weight = 12
                if i[1] == 'K':
                    weight = 13
                if i[1] == 'A':
                    weight = 14
            if len(i) == 3:
                weight=10
            weights.append(weight)
            
        # assigns the values in the original list with a weight and sorts the original list
        zipped=zip(weights,list)
        zipped = sorted(zipped)
        unzipped = [x for y, x in zipped]
        return unzipped
