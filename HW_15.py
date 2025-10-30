# Task 1


def rod_c(pr, n):
    """
    This function determines the maximum 
    value obtainable by cutting up the 
    rod and selling the pieces
    """
    pr_cut = [0] * (n + 1)  # List of zeroes, later a list of money of different cuts
    cuts = [[] for i in range(n + 1)] # List of empty lists, later a list of cuts
  
    for i in range(1, n + 1):
        max_val = -1
        best_cut = []
        for j in range(1, i + 1):
            if j <= len(pr):
                cur = prices[j - 1] + pr_cut[i - j]
                if cur > max_val:
                    max_val = cur
                    best_cut = [j] + cuts[i - j]
        pr_cut[i] = max_val
        cuts[i] = best_cut
    return pr_cut[n], cuts[n]


pr = [1, 5, 8, 9, 10, 17, 17, 20] # Array of Prices
n = 8                             # Rod length

max_value, cut_list = rod_c(pr, n)
print("Maximum money gained -", max_value)
print("Recommended cut lengths -", cut_list)
