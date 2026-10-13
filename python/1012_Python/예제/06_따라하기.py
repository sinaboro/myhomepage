total = 20000

print("30000원 이상인가요?", total >= 30000)

if total >= 30000:
    shipping_fee = 0  # 조건이 참일 때 실행합니다.
    print("무료배송입니다.")
else:
    shipping_fee = 3000  # 조건이 거짓일 때 실행합니다.
    print("배송비가 있습니다.")

payment = total + shipping_fee  # if/else 밖에서는 공통 계산을 합니다.
print(f"배송비: {shipping_fee:,}원")
print(f"최종 결제액: {payment:,}원")
