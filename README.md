# aave-credit-scoring
#  DeFi Credit Scoring using Aave V2 Protocol

This project uses machine learning to assign a **credit score (0–1000)** to DeFi wallet addresses based on their transaction history on the Aave V2 protocol. The goal is to evaluate and rank wallet reliability by analyzing actions such as deposits, borrows, repayments, and liquidations.

---

## Dataset

The raw dataset contains over 100,000 transaction records across thousands of wallets, each detailing:
- Wallet address
- Timestamp
- Action (`deposit`, `borrow`, `repay`, `redeemUnderlying`, `liquidationCall`)
- Asset and amount

Sample file:  
`data/user-wallet-transactions.json`

---

##  Project Structure
aave-credit-scoring/
├── data/
│ └── user-wallet-transactions.json
├── notebooks/
│ └── model.pkl
├── src/
│ ├── feature_engineering.py
│ ├── scoring_model.py
│ └── score_wallet.py
├── score_output.csv
├── analysis.md
└── README.md

---

# How It Works

1. **Feature Engineering**  
   Extracts behavioral features per wallet (e.g., number of liquidations, repayments).

2. **Model Training**  
   A `RandomForestRegressor` is trained on synthetic targets where more liquidations = lower scores.

3. **Scoring**  
   Each wallet is assigned a credit score between 0 and 1000.

---

#Getting Started

# 1. Clone the Repository

```bash
git clone https://github.com/yourusername/aave-credit-scoring.git
cd aave-credit-scoring

## Install Dependencies
pip install -r requirements.txt

## 1. Train the Model
Inside a notebook or script:

python
Copy
Edit
from feature_engineering import load_json_transactions, aggregate_wallet_features
from scoring_model import train_model

df = load_json_transactions("data/user-wallet-transactions.json")
features = aggregate_wallet_features(df)
features["target"] = 1000 - features["n_liquidations"] * 100  # dummy target
model = train_model(features)


## Score Wallets


bash
Copy
Edit
python -m src.score_wallet --input data/user-wallet-transactions.json --model notebooks/model.pkl --output score_output.csv
 Output
The output file score_output.csv contains:

walletAddress	 score
0x1234...     	983
0x5678...     	672


