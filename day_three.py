popular_coins = ["BTC", "ETH", "XRP", "ADA", "DOT"]
print("인기 암호화폐 목록:", popular_coins)

# 리스트 조작
print(f"첫 번째 코인: {popular_coins[0]}")
print(f"마지막 코인: {popular_coins[-1]}")
print(f"상위 3개 코인: {popular_coins[:3]}")

# 새로운 코인 추가
popular_coins.append("SOL")
print(f"SOL 추가 후: {popular_coins}")

popular_coins.insert(1, "KRW-BTC")

print(f"KRW-BTC Insert 후: {popular_coins}")
popular_coins.pop()

popular_coins.remove("KRW-BTC")
# 리스트 길이
print(f"총 코인: {popular_coins}개")
print(f"총 코인 개수: {len(popular_coins)}개")