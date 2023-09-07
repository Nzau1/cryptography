class Token:
    def __init__(self, name, symbol, initial_supply):
        self.name = name
        self.symbol = symbol
        self.total_supply = initial_supply
        self.balance = initial_supply

    def transfer(self, to_address, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        to_address.receive(self.symbol, amount)
        return True

class Wallet:
    def __init__(self, name):
        self.name = name
        self.balance = {}

    def create_token(self, token_name, token_symbol, initial_supply):
        token = Token(token_name, token_symbol, initial_supply)
        self.balance[token_symbol] = initial_supply
        return token

    def receive(self, token_symbol, amount):
        if token_symbol in self.balance:
            self.balance[token_symbol] += amount
        else:
            self.balance[token_symbol] = amount

    def send(self, to_wallet, token_symbol, amount):
        if token_symbol in self.balance and self.balance[token_symbol] >= amount:
            success = to_wallet.receive(token_symbol, amount)
            if success:
                self.balance[token_symbol] -= amount
                return True
        return False

# Create two wallets and a token
wallet_aef_fx = Wallet("AEF.FX")
wallet_bob = Wallet("Bob")

aef_coin = wallet_aef_fx.create_token("AEF Coin", "AEF", 1000)

# Transfer AEF Coins between wallets
wallet_aef_fx.send(wallet_bob, "AEF", 100)

# Check wallet balances
print(f"{wallet_aef_fx.name} Balance:")
for symbol, balance in wallet_aef_fx.balance.items():
    print(f"{symbol}: {balance}")

print(f"{wallet_bob.name} Balance:")
for symbol, balance in wallet_bob.balance.items():
    print(f"{symbol}: {balance}")
