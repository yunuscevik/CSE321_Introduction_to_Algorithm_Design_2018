#########################
# 141044080 Yunus CEVIK #
#########################

# This function calculates Minimize The Weighted Sum of Ending Times of Jobs
def jobsScheduling(w,t):
    n = len(w)
    optScheduling = []
    for i in range(n):
        optScheduling.append(i)

    for i in range(n):
        for j in range(n-i-1):
            if w[j]/t[j] < w[j+1]/(t[j+1]):
                w[j],w[j + 1] = w[j + 1],w[j]
                t[j], t[j + 1] = t[j + 1], t[j]
                optScheduling[j], optScheduling[j + 1] = optScheduling[j + 1], optScheduling[j]

    sumTimes = 0
    sum = 0
    for i in range(len(w)):
        sumTimes += t[i]
        sum += (w[i]*sumTimes)

    return  w, t, sum, optScheduling


def main():
    weights = [40, 55, 38, 54, 23]
    times = [3, 6, 4, 2, 9]

    print("Non-sorted Weights of Jobs")
    print("Weights ====> ",weights)
    print("Times ======> ",times)

    a,b,c,d = jobsScheduling(weights,times)
    print("")
    print("Weights and Times of Ended Jobs ")
    print("Weights ====> ",a)
    print("Times ======> ",b)
    print("")
    print("Minimize The Weighted Sum of Ending Times of Jobs ====> ",c)
    print("")
    print("Optimally Scheduling of Jobs ====> ",d)

if __name__ == '__main__':
    main()



