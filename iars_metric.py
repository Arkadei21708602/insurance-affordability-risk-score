import pandas as pd

def building_age_factor(age: int) -> float:
    if age < 10:
        return 0.9
    elif age <= 30:
        return 1.1
    else:
        return 1.2

def main():
    df = pd.read_csv("sample_properties.csv")

    climate_weights = {
        "low": 1.0,
        "medium": 1.2,
        "high": 1.5,
    }

    df["ClimateRiskWeight"] = df["climate_risk"].map(climate_weights)
    df["BuildingAgeFactor"] = df["building_age"].apply(building_age_factor)

    df["IARS_base"] = df["insurance_cost"] / df["median_income"]
    df["IARS_extended"] = (
        df["IARS_base"] * df["ClimateRiskWeight"] * df["BuildingAgeFactor"]
    )

    df_sorted = df.sort_values("IARS_extended").reset_index(drop=True)
    print(df_sorted.round(4))

if __name__ == "__main__":
    main()
