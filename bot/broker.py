class Broker:
    """
    Placeholder broker adapter.
    Later we will connect this to Kotak Neo SDK safely.
    """

    def connect(self):
        print("Broker connect() called")

    def get_market_data(self):
        # later: fetch candle/ltp from Kotak Neo
        return {}

    def place_order(self, action: str, contract: str, qty: int):
        # later: call Kotak order API
        print(f"PLACE ORDER: {action} {contract} x {qty}")
        return "ORDER_ID_PLACEHOLDER"
