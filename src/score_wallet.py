import argparse
from src.feature_engineering import load_json_transactions, aggregate_wallet_features
from src.scoring_model import predict_scores
import joblib
import pandas as pd

def main(input_file, model_file, output_file):
    df = load_json_transactions(input_file)
    features_df = aggregate_wallet_features(df)

    # Drop wallet column for prediction
    X = features_df.drop(columns=["wallet"])
    model = joblib.load(model_file)
    features_df["score"] = predict_scores(model, X)

    features_df[["wallet", "score"]].to_csv(output_file, index=False)
    print(f"Saved scores to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--model", type=str, default="model.pkl")
    parser.add_argument("--output", type=str, default="score_output.csv")
    args = parser.parse_args()

    main(args.input, args.model, args.output)
