# Testnet Balance Checker

[🇬🇧 English](#testnet-balance-checker) | [🇷🇺 Русский](#проверка-балансов-в-тестовых-сетях)

## 🇬🇧 English

This script checks Ethereum addresses' balances in test networks and saves the results to a text file.

### Supported Test Networks

- Ethereum Sepolia
- Ethereum Holesky
- Base Sepolia
- Optimism Sepolia
- Arbitrum Sepolia
- Polygon Amoy
- BNB Testnet

### Installation & Setup

1. Install dependencies (if not installed):
   ```sh
   pip install web3
   ```

2. Create a `config.json` file and add your Infura API key:
   ```json
   {
       "INFURA_API_KEY": "your_api_key_here"
   }
   ```

3. Create an `addresses.txt` file and add a list of addresses (one per line).

### Usage

Run the script with:
```sh
python script.py
```

The results will be saved in `balances.txt` after execution.

### Output Format

The `balances.txt` file will contain entries in the following format:
```
Address: 0xYourAddressHere
  ethereum-sepolia: 1.234 ETH
  ethereum-holesky: 0.567 ETH
  base-sepolia: 0.000 ETH
  ...
-
```

### Error Handling

If the RPC server is unavailable or the address is invalid, an appropriate message will be written to `balances.txt`.

### License

This project is licensed under the MIT License.

---

## 🇷🇺 Проверка балансов в тестовых сетях

Этот скрипт проверяет балансы Ethereum-адресов в тестовых сетях и сохраняет результаты в текстовый файл.

### Поддерживаемые тестовые сети

- Ethereum Sepolia
- Ethereum Holesky
- Base Sepolia
- Optimism Sepolia
- Arbitrum Sepolia
- Polygon Amoy
- BNB Testnet

### Установка и настройка

1. Установите зависимости (если не установлены):
   ```sh
   pip install web3
   ```

2. Создайте файл `config.json` и добавьте в него ваш API-ключ Infura:
   ```json
   {
       "INFURA_API_KEY": "your_api_key_here"
   }
   ```

3. Создайте файл `addresses.txt` и добавьте в него список адресов (по одному на строку).

### Использование

Запустите скрипт командой:
```sh
python script.py
```

После выполнения результаты будут записаны в `balances.txt`.

### Формат вывода

Файл `balances.txt` будет содержать записи в следующем формате:
```
Address: 0xYourAddressHere
  ethereum-sepolia: 1.234 ETH
  ethereum-holesky: 0.567 ETH
  base-sepolia: 0.000 ETH
  ...
-
```

### Обработка ошибок

Если RPC-сервер недоступен или адрес некорректен, соответствующее сообщение будет записано в файл `balances.txt`.

### Лицензия

Этот проект распространяется под лицензией MIT.
