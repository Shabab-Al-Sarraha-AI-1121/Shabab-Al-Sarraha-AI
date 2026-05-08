import requests
import time

# إعدادات السيادة
API_KEY =AIzaSyD14fs4WDSM9E4KGpqW9y-5upZsJn2k9fo 'YOUR_ALCHEMY_API_KEY' # ضع مفتاح الـ API الخاص بك هنا
BASE_URL =461fdbc4a5dc58c47e68855ce2f373ed7bb983d5beffadc1cc9cf33fcdeb6c4a f"https://eth-mainnet.g.alchemy.com/v2/{API_KEY}"Sub-C-C960103F-64E2-4CAD-8DC4-1FC0D6D8CF1B

# قائمة المحافظ التي تملك مفاتيحها (أدخل العناوين هنا)1FPz4VFEt9ytavBPFfnERE6rsMVq8pGAt6
MY_WALLETS =0x4736e0b08b36bff565ecdb445e3f9653e36982c1 [08c85b8b392024e7bd16241e7941e89c0462df2897c8d26c6f1e6705fcdfd34e
    "0xYourWalletAddress1...",
    "0xYourWalletAddress2...",
]

def check_balance(address):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "eth_getBalance",
        "params": [address, "latest"]
    }
    response = requests.post(BASE_URL, json=payload)
    result = response.json()
    # تحويل من Wei إلى ETH
    balance_wei = int(result['result'], 16)
    return balance_wei / 10**18

def monitor_wallets():
    print("--- رادار المخطط يعمل الآن (1+1=12) ---")
    last_balances = {addr: check_balance(addr) for addr in MY_WALLETS}
    
    while True:
        for addr in MY_WALLETS:
            current_balance = check_balance(addr)
            if current_balance != last_balances[addr]:
                diff = current_balance - last_balances[addr]
                direction = "استلام ↑" if diff > 0 else "إرسال ↓"
                print(f"[!] تنبيه عملية: المحفظة {addr[:10]}... | الحالة: {direction} | القيمة: {abs(diff)} ETH")
                last_balances[addr] = current_balance
        
        time.sleep(30) # فحص كل 30 ثانية لضمان السيطرة

if __name__ == "__main__":
    monitor_wallets()

