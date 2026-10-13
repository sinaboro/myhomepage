product_name = "텀블러"
price = 12000
quantity = 3
subtotal = price * quantity
discount_rate = 10
discount_amount = subtotal * discount_rate / 100
total = subtotal - discount_amount
print("===== 주문 영수증 =====")
print(f"상품: {product_name}")
print(f"단가: {price:,}원 / 수량: {quantity}개")
print(f"할인 전: {subtotal:,}원")
print(f"할인({discount_rate}%): {discount_amount:,.0f}원")
print(f"결제액: {total:,.0f}원")

print("---------------------")

print(f"가격 : {price:,}원")
print(f"상품: {product_name}")