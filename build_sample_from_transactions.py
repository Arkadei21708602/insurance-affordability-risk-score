import pandas as pd
import random
from pathlib import Path


def build_sample(n: int = 10):
    path = Path("transactions.parquet")
    df_tr = pd.read_parquet(path)

    print("Columns:", df_tr.columns)

    #Check if needed tables exst
    required_cols = ["street", "suburb", "state", "price"]
    for col in required_cols:
        if col not in df_tr.columns:
            raise ValueError(f"Column '{col}' not found in dataset.")

   
    sample = df_tr[required_cols].head(n).copy()
    sample = sample.reset_index(drop=True)

    #Generate address 
    sample["address"] = (
        sample["street"].astype(str)
        + ", "
        + sample["suburb"].astype(str)
        + ", "
        + sample["state"].astype(str)
    )

    sample["property_id"] = sample.index + 1

    #Insurance model: 0.25% from the cost (example metrics 0.25 can be changed)
    sample["insurance_cost"] = sample["price"] * 0.0025

    
    sample["median_income"] = 80000

    #Climate risk category 
    risks = ["low", "medium", "high"]
    sample["climate_risk"] = [
        random.choices(risks, weights=[0.4, 0.4, 0.2])[0]
        for _ in range(len(sample))
    ]

    #Random building age
    sample["building_age"] = [random.randint(5, 40) for _ in range(len(sample))]

    #THE FINAL CSV
    out = sample[
        [
            "property_id",
            "address",
            "insurance_cost",
            "median_income",
            "climate_risk",
            "building_age",
        ]
    ]

    out.to_csv("sample_properties.csv", index=False)
    print("\nGenerated sample_properties.csv with", len(out), "rows.")


if __name__ == "__main__":
    build_sample()
