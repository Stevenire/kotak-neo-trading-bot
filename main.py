import time

from bot.broker import Broker
from bot.strategy import Strategy
from bot.risk_manager import RiskManager


def main():
    print("Kotak Neo Trading Bot (PAPER MODE) Starting...")

    broker = Broker()
    strategy = Strategy()
    risk = RiskManager(max_daily_loss=2000, max_trades=5)

    broker.connect()

    # Paper loop: runs 10 cycles then stops
    for i in range(10):
        print(f"\nCycle {i+1}/10")

        if not risk.can_trade():
            print("Risk limits hit. Stopping trading for today.")
            break

        market_data = broker.get_market_data()
        signal = strategy.generate_signal(market_data)

        if signal is None:
            print("No trade signal.")
        else:
            # PAPER: just printing what would happen
            print(f"Signal: {signal} (paper)")
            risk.on_trade()

        time.sleep(1)

    print("\nBot finished (paper mode).")


if __name__ == "__main__":
    main()
