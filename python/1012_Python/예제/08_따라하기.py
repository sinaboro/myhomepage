price = 12000
quantity = 3
discount_rate = 0
total = price * quantity * (1 - discount_rate / 100)
print("기대값:", 36000)
print("실제값:", total)
print("일치:", total == 36000)  # ==는 두 값이 같은지 비교합니다.
