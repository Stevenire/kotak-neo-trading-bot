import os

class Broker:
    def __init__(self):
        self.api_key = os.getenv("KOTAK_API_KEY")

    def connect(self):
        if not self.api_key:
            print("API key not found!")
            return

        if self.api_key in ("KOTAK_API_KEY", "your_api_key_here"):
            print("API key is placeholder. Update GitHub Codespaces secret.")
            return

        print("Kotak API key loaded successfully.")

    def get_market_data(self):
        return {}

    def place_order(self, action: str, contract: str, qty: int):
        print(f"[PAPER] {action} {contract} x {qty}")
        return "ORDER_ID_PLACEHOLDER"
