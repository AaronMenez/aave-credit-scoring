import pandas as pd
import json
from collections import defaultdict

def load_json_transactions(file_path):
    with open(file_path, 'r') as f:
        raw_data = json.load(f)
    return pd.json_normalize(raw_data)

def aggregate_wallet_features(df):
    grouped = defaultdict(dict)
    
    for wallet, group in df.groupby("userWallet"):
        grouped[wallet]["total_transactions"] = len(group)
        grouped[wallet]["n_deposits"] = (group["action"] == "deposit").sum()
        grouped[wallet]["n_borrows"] = (group["action"] == "borrow").sum()
        grouped[wallet]["n_repays"] = (group["action"] == "repay").sum()
        grouped[wallet]["n_redeems"] = (group["action"] == "redeemunderlying").sum()
        grouped[wallet]["n_liquidations"] = (group["action"] == "liquidationcall").sum()

        # Ratios
        borrows = grouped[wallet]["n_borrows"]
        repays = grouped[wallet]["n_repays"]
        grouped[wallet]["repay_borrow_ratio"] = repays / borrows if borrows else 0

    features_df = pd.DataFrame.from_dict(grouped, orient="index").reset_index().rename(columns={"index": "wallet"})
    return features_df
