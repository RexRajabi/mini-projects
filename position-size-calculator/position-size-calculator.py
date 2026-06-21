# Position size calculator v1.0
capital = float(input("Capital: "))
risk_percent = float(input("Risk %: "))
entry = float(input("Entry: "))
stop = float(input("Stop: "))

def postition_calculator(capital, risk_percent, entry, stop):
    risk_amount = capital * (risk_percent / 100)
    lot_size = int(risk_amount / (entry - stop))
    return {
        "risk amount": risk_amount,
        "Lot size": lot_size
    }
print(postition_calculator(capital, risk_percent, entry, stop))
