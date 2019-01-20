#########################
# 141044080 Yunus CEVIK #
#########################

# The function that determines the stop at the most suitable hotels decides which hotel the passenger should stay in, 
# depending on the optimal distance (200 miles). This decision depends on the minimum penalty score.  
# If passenger travels x miles during a day, passenger would have  penalty score depending to square of (200-x).  
# But, passenger must plan how travel must be for minimum penalty score. 
def optimalStopsForHotels(hotel):
    minimalPenalty = []
    stop = []
    for i in range(len(hotel)):
        minimalPenalty.append(int((200-hotel[i])**2))
        stop.append(0)

        for j in range(0,i):
            if (minimalPenalty[j] + ((200-(hotel[i] - hotel[j]))**2) < minimalPenalty[i]):
                minimalPenalty[i] =  int(minimalPenalty[j] +((200-(hotel[i] - hotel[j]))**2))
                stop[i] = (j +1)

    print("Minimal Penalty : " + str(minimalPenalty[len(hotel) - 1]))
    print("The sum of the penalties in the order given in the day.\n",minimalPenalty)
    stoppedPath = ""
    index = len(stop)-1
    while (index >= 0):
        stoppedPath = str(index + 1) + " " + stoppedPath
        index = stop[index] -1
    print("Stop at : ", stoppedPath)



def main():
    A = [190, 220, 410, 580, 640, 770, 950, 1100, 1350 ]
    print("Hotels : ",A)
    optimalStopsForHotels(A)


if __name__ == '__main__':
    main()