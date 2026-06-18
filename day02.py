items = ["苹果", "牛奶", "面包","薯条","汉堡"]
prices = [5, 12, 8, 10, 158]

total = sum(prices)
average =total/len(prices)
print("购物清单:")

for item in items:
    print(item)

print("总价:", total)
print("平均价格",average)