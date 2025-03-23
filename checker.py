from web3 import Web3

# RPC-адреса тестовых сетей
TESTNETS = {
    "ethereum-sepolia": "https://sepolia.infura.io/v3/YOUR_INFURA_API_KEY",
    "ethereum-holesky": "https://holesky.infura.io/v3/YOUR_INFURA_API_KEY",
    "base-sepolia": "https://sepolia.base.org",
    "optimism-sepolia": "https://optimism-sepolia.infura.io/v3/YOUR_INFURA_API_KEY",
    "arbitrum-sepolia": "https://sepolia-rollup.arbitrum.io/rpc",
    "polygon-amoy": "https://rpc-amoy.polygon.technology",
    "bnb-testnet": "https://data-seed-prebsc-1-s1.binance.org:8545/"
}

# Чтение адресов из файла
with open("addresses.txt", "r") as f:
    addresses = [line.strip() for line in f if line.strip()]

results = []

# Проверка балансов в каждой сети
for network, rpc_url in TESTNETS.items():
    print(f"Checking balances in {network}...")
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    if not w3.is_connected():
        results.append(f"{network}: RPC connection failed")
        continue
    
    for address in addresses:
        try:
            balance = w3.eth.get_balance(address)
            balance_ether = w3.from_wei(balance, 'ether')
            results.append(f"{network}, {address}: {balance_ether} ETH")
        except Exception as e:
            results.append(f"{network}, {address}: Error {e}")

# Запись результатов в файл
with open("balances.txt", "w") as f:
    f.write("\n".join(results))

print("Балансы сохранены в balances.txt")
