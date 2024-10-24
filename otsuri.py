n = int(input('投入金額\n'))  
x = int(input('商品価格。\n'))  

change = n - x
print(f'お釣り {change} 円')

coins = [500, 100, 50, 10]
counter = {} 


for coin in coins:
    count = change // coin 
    change %= coin  
    counter[coin] = count 


print("お釣りの内訳:")
for coin, count in counter.items():
    if count > 0:
        print(f"{coin}円硬貨: {count}枚")
