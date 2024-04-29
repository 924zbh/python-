import random
def gamble(stake,trials):
    #返回输掉stake所要的次数
    total_bets = 0 #总下注次数
    max_cash = stake #最大赌资
    for t in range(trials):
        cash = stake
        while cash > 0:
            total_bets += 1
            if random.randrange(0,2) ==0:
                cash += 1
                max_cash = max(max_cash,cash)
            else:cash -=1
            #print(cash)
    #print("赌博过程中最大赌资={}".format(max_cash))
    return int(total_bets/trials)
if __name__ == "__main__":
    print("输掉{}个筹码的平均次数：{}".format(1,gamble(1,100)))
    print("输掉{}个筹码的平均次数：{}".format(5,gamble(5,100)))
    print("输掉{}个筹码的平均次数：{}".format(20,gamble(20,100)))
