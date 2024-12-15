# Function to find the minimum number of coins to make 
# sum X
def solve(N, X, coins):
    # dp[] array such that dp[i] stores the minimum number
    # of coins to make sum = i
    dp = [float('inf')] * (X + 1)
    dp[0] = 0

    # Iterate over all possible sums from 1 to X
    for i in range(1, X + 1):
        # Iterate over all coins
        for j in range(N):
            if coins[j] > i or dp[i - coins[j]] == float('inf'):
                continue
            dp[i] = min(dp[i], dp[i - coins[j]] + 1)

    # If it is possible to make sum = X, return dp[X]
    if dp[X] != float('inf'):
        return dp[X]

    # If it is impossible to make sum = X, return -1
    return -1

# Sample Input
# N = [100,1000000]
# s ="649304 85832 159093 841262 930486 225095 306941 914339 469211 156923 460959 236712 440066 842678 379057 615269 321673 694036 378785 792217 78290 15844 644234 752342 102458 30237 191522 388758 697655 113684 20857 639493 641307 527161 977787 505822 196847 735190 169901 417528 342499 102964 907594 780802 577476 162325 790726 579970 148134 144070 624899 392951 594195 813112 534969 856431 25058 630213 641105 636550 762730 873997 275210 717753 243026 915205 52253 613173 751823 647785 928932 305278 858885 496267 717378 426281 245531 139541 942976 912031 550043 194533 504278 552822 805186 950257 673230 484067 790808 762595 590958 799224 711398 599947 858840 212470 820350 710862 546121 159727"
# coins =list(map(int,s.split()))

N = list(map(int, input().split()))
coins = list(map(int, input().split()))

print(solve(N[0], N[1], coins))