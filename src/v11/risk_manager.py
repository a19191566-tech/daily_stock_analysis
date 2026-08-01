"""
V11 Risk Manager
"""

class RiskManager:
    def evaluate(self, entry, stop_loss, target):
        if entry is None or stop_loss is None or target is None:
            return {"risk_reward": 0}

        risk = abs(entry - stop_loss)
        reward = abs(target - entry)

        return {
            "risk": risk,
            "reward": reward,
            "risk_reward": round(reward / risk, 2) if risk else 0,
        }
