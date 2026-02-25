class RiskManager:
    def __init__(self, max_daily_loss=2000, max_trades=5):
        self.max_daily_loss = max_daily_loss
        self.max_trades = max_trades
        self.trades_today = 0
        self.daily_pnl = 0.0

    def can_trade(self) -> bool:
        if self.trades_today >= self.max_trades:
            return False
        if self.daily_pnl <= -abs(self.max_daily_loss):
            return False
        return True

    def on_trade(self):
        self.trades_today += 1

    def update_pnl(self, pnl: float):
        self.daily_pnl = pnl
