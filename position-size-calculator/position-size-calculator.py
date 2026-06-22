# Position size calculator v1.0
capital = float(input("Capital: "))
risk_percent = float(input("Risk %: "))
stoploss_depth = float(input("stop loss in pips: "))
pip_value = float(input("pip value in your instrument: "))

def postition_calculator(capital, risk_percent, entry, stop):
    risk_amount = capital * (risk_percent / 100)
    lot_size = risk_amount / (pip_value * stoploss_depth)
    return {
        "risk amount": risk_amount,
        "Lot size": lot_size
    }
print(postition_calculator(capital, risk_percent, stoploss_depth, pip_value))
