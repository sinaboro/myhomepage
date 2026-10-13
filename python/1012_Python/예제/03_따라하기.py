price = 12000
quantity = 3
discount_rate = 10
subtotal = price * quantity  # 할인 전 금액입니다.
discount_amount = subtotal * discount_rate / 100  # 할인액입니다.
total = subtotal - discount_amount  # 할인 후 결제액입니다.
print("할인 전:", subtotal)
print("할인액:", discount_amount)
print("결제액:", total)
print("괄호 비교:", 100 + 200 * 3, (100 + 200) * 3)
