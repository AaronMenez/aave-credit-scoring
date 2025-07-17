#  Credit Score Analysis for Aave V2 Wallets

This project assigns a **credit score (0–1000)** to each wallet address interacting with the Aave V2 DeFi protocol. The score is based on behavioral transaction data and reflects responsible or risky financial activity such as deposits, borrowings, repayments, and liquidations.

---

# Score Distribution

We analyzed 3,496 unique wallets. The table below shows how many wallets fall into each 100-point score bracket:

| Score Range   | Number of Wallets |
|---------------|-------------------|
| 0–100         | 0                 |
| 100–200       | 0                 |
| 200–300       | 0                 |
| 300–400       | 1                 |
| 400–500       | 0                 |
| 500–600       | 2                 |
| 600–700       | 2                 |
| 700–800       | 2                 |
| 800–900       | 16                |
| 900–1000      | 3,473             |

** Insight:**  
>  Over **99%** of wallets scored above 900, indicating most users behave responsibly (low liquidation, regular repayments). Only a small fraction fall below 800.

---

# Behavior Insights

# High-Scoring Wallets (900–1000)
- Zero or very few liquidation events  
- Regular repayments of borrowed funds  
- Consistent protocol usage over time  
- Interaction with multiple actions (e.g. deposit + repay)

# Low-Scoring Wallets (< 800)
- Scored low due to liquidation penalties in our dummy logic  
- Minimal or one-time interactions  
- Likely either test wallets, bots, or failed attempts

---

# Feature Importance

The following features were used to generate credit scores:

- Total number of transactions
- Number of deposits
- Number of repayments
- Number of borrow events
- Number of liquidation calls
- Ratios like `repayments / borrows` and `deposits / total tx`

>  We used a RandomForestRegressor trained on these engineered features with a synthetic target (`1000 - n_liquidations * 100`).

---

# Limitations

- The target variable is rule-based (penalizing liquidations), not learned from real credit risk outcomes.
- Model doesn't account for transaction volume or token value.
- Temporal behavior (time between events) is not yet included.

---

# Recommendations for Improvement

- Incorporate real market value exposure and token price
- Label historical defaults or actual liquidations across protocols
- Add time-series features like transaction frequency or time-to-repay
- Experiment with alternative models (e.g. XGBoost, LightGBM)

---

# Output

All wallet scores are saved in:
```bash
score_output.csv
