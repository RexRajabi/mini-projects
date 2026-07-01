# Mini Projects 🛠️

Welcome to **Mini Projects**, a collection of my small coding experiments, fun projects, and learning exercises.  
This repository is my personal playground for trying out ideas, exploring new concepts, and practicing programming.

---

## Projects

### 🔐 Cipher
- **Path**: [`cipher/`](cipher/)
- A simple Caesar-style cipher that can **encrypt** and **decrypt** text using a numeric key.  
- Example usage:
```bash
./cipher -e "hello" 3   # Encrypt
./cipher -d "khoor" 3   # Decrypt
```
### 📊 Position Size Calculator
- **Path**: [`position-size-calculator/`](position-size-calculator/)
- **Status**: Just published the first clean version (v2.0)
- A risk management tool that calculates optimal position size based on capital, risk percentage and stoploss.
- **Under development features 🚧**: tick base calculation, Storing the history of calculations.
### Brute Force ASCII Tool

A simple Python script that takes a word and applies ASCII shifts from 1 to 57, displaying all possible combinations.

#### How it works

The script takes a word as input and for each character, subtracts values from 1 to 57 from its ASCII code, generating 57 different variations of the original word.

#### Usage

```bash
python3 brute_force.py
```