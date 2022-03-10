import pyupbit

access = "vsKNb9ponftg5CuWoLGEcGv7XsXBYw1xCYK9hZa8"          # 본인 값으로 변경
secret = "I1thxAHWtz9K8zTIZY4vOyG7Akr6JNZOL2hxN7jo"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회