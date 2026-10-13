price = 2500
quantity = 4
discount_rate = 12.5

valid = price >= 0 and quantity >= 1 and discount_rate >= 0 and discount_rate <= 100

# valid = False
# if price >= 0:
#     if quantity >=1:
#         if discount_rate >=0:
#             if discount_rate <=100:
#                 valid = True

if valid:
    subtotal = price * quantity
    total = subtotal * (1 - discount_rate / 100)
    print(f"할인 전 {subtotal:,}원 / 결제액 {total:,.0f}원")
else:
    print("범위 오류: 단가 0 이상, 수량 1 이상, 할인율 0~100입니다.")
