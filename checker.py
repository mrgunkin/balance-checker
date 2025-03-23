from web3 import Web3
import json

# Чтение API-ключа из файла config.json
try:
    with open("config.json", "r") as f:
        config = json.load(f)
        INFURA_API_KEY = config.get("INFURA_API_KEY", "")
except Exception as e:
    print(f"Error reading config.json: {e}")
    exit(1)

# RPC-адреса тестовых сетей
TESTNETS = {
    "ethereum-sepolia": f"https://sepolia.infura.io/v3/{INFURA_API_KEY}",
    "ethereum-holesky": f"https://holesky.infura.io/v3/{INFURA_API_KEY}",
    "base-sepolia": "https://sepolia.base.org",
    "optimism-sepolia": f"https://optimism-sepolia.infura.io/v3/{INFURA_API_KEY}",
    "arbitrum-sepolia": "https://sepolia-rollup.arbitrum.io/rpc",
    "polygon-amoy": "https://rpc-amoy.polygon.technology",
    "bnb-testnet": "https://data-seed-prebsc-1-s1.binance.org:8545/"
}

# Чтение адресов из файла
try:
    with open("addresses.txt", "r") as f:
        addresses = [line.strip() for line in f if line.strip()]
except Exception as e:
    print(f"Error reading addresses.txt: {e}")
    exit(1)

results = []

# Проверка балансов по каждому адресу
for address in addresses:
    results.append(f"Address: {address}")
    try:
        checksum_address = Web3.to_checksum_address(address)
    except Exception as e:
        results.append(f"  Invalid address format: {address} - {e}")
        continue
    
    for network, rpc_url in TESTNETS.items():
        print(f"Checking {network} for {address}...")
        try:
            w3 = Web3(Web3.HTTPProvider(rpc_url))
            if not w3.is_connected():
                raise ConnectionError("RPC connection failed")
            
            balance = w3.eth.get_balance(checksum_address)
            balance_ether = w3.from_wei(balance, 'ether')
            results.append(f"  {network}: {balance_ether} ETH")
        except Exception as e:
            results.append(f"  {network}: Error {e}")
    results.append("-")

# Запись результатов в файл
try:
    with open("balances.txt", "w") as f:
        f.write("\n".join(results))
    print("Балансы сохранены в balances.txt")
except Exception as e:
    print(f"Error writing balances.txt: {e}")
