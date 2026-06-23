# Position Size Calculator v2.0
import os

def clear_screen():
    """Clears the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_help():
    """Display help information"""
    print("\n" + "="*60)
    print("📊 POSITION SIZE CALCULATOR - HELP")
    print("="*60)
    print("\n📌 WHAT IT DOES:")
    print("  Calculates the optimal position size (lot size) for your trades")
    print("  based on your risk management rules.")
    print("  Really usefull in Forex matket for getting into position.")
    #==========
    print("\n📋 INPUT PARAMETERS:")
    print("  • Capital        : Your total account balance")
    print("  • Risk %         : Percentage of capital you're willing to risk")
    print("  • Stop Loss (pips): Distance from entry to stop loss in pips")
    print("  • Pip Value      : Monetary value of 1 pip for your instrument")
    print("\t(You can find the value via checking your broker \n\t or just a simple search in google)")
    #==========
    print("\n🧮 FORMULA:")
    print("  Risk Amount = Capital × (Risk% / 100)")
    print("  Lot Size = Risk Amount / (Pip Value × Stop Loss in Pips)")
    #==========
    print("\n💡 EXAMPLE:")
    print("  Capital: $10,000")
    print("  Risk %: 2%")
    print("  Stop Loss: 50 pips")
    print("  Pip Value: $10")
    print("  → Risk Amount: $200")
    print("  → Lot Size: 0.40")
    #==========
    print("\n⚠️  IMPORTANT NOTES:")
    print("  • Always risk 1-2% per trade for proper risk management")
    print("  • Pip value varies by instrument \n   (Forex(XAU/USD, EUR/USD, etc.), indices, crypto, etc.)")
    print("  • Round down lot size to match broker minimums")
    #==========
    print("\n" + "="*60)
    input("\nPress Enter to return to menu...")
    #==========
def calculate_position():
    """Calculate position size based on user inputs"""
    print("\n" + "="*60)
    print("📈 POSITION SIZE CALCULATION")
    print("="*60)
    
    # Get inputs with validation
    while True:
        try:
            capital = float(input("\n💰 Capital: "))
            if capital <= 0:
                print("❌ Capital must be greater than 0!")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number!")
    
    while True:
        try:
            risk_percent = float(input("📊 Risk %: "))
            if risk_percent <= 0 or risk_percent > 100:
                print("❌ Risk % must be between 0 and 100!")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number!")
    
    while True:
        try:
            stoploss_depth = float(input("📉 Stop Loss (pips): "))
            if stoploss_depth <= 0:
                print("❌ Stop loss must be greater than 0!")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number!")
    
    while True:
        try:
            pip_value = float(input("💵 Pip Value: "))
            if pip_value <= 0:
                print("❌ Pip value must be greater than 0!")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number!")
    
    # Calculate
    risk_amount = capital * (risk_percent / 100)
    lot_size = risk_amount / (pip_value * stoploss_depth)
    
    # Display results with clear separation
    print("\n" + "="*60)
    print("✅ CALCULATION RESULT")
    print("="*60)
    print(f"\n💰 Risk Amount  : ${risk_amount:,.2f}")
    print(f"📊 Lot Size     : {lot_size:.2f} lots")
    print(f"\n📋 Breakdown:")
    print(f"   • Capital         : ${capital:,.2f}")
    print(f"   • Risk %          : {risk_percent:.1f}%")
    print(f"   • Stop Loss       : {stoploss_depth:.1f} pips")
    print(f"   • Pip Value       : ${pip_value:.2f}")
    print("="*60)
    
    # Risk warning if too high
    if risk_percent > 2:
        print("\n⚠️  WARNING: Risking more than 2% per trade is high risk!")
        print("   Consider reducing your risk percentage.")
    
    print("\n" + "="*60)

def main():
    """Main program loop with menu"""
    while True:
        clear_screen()
        print("\n" + "="*60)
        print("  📊 POSITION SIZE CALCULATOR v2.0")
        print("="*60)
        print("\n  [1] Calculate Position Size")
        print("  [2] Help / Documentation")
        print("  [3] Exit")
        print("\n" + "="*60)
        
        choice = input("\n👉 Select an option (1-3): ").strip()
        
        if choice == "1":
            calculate_position()
            input("\nPress Enter to return to menu...")
            
        elif choice == "2":
            show_help()
            
        elif choice == "3":
            print("\n" + "="*60)
            print("👋 Thank you for using Position Size Calculator!")
            print("   Happy Trading! 📈")
            print("="*60 + "\n")
            break
            
        else:
            print("\n❌ Invalid option! Please choose 1, 2, or 3.")
            input("\nPress Enter to continue...")

# Run the program
if __name__ == "__main__":
    main()
