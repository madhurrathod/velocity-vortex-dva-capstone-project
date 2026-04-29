"""
ETL pipeline for the NST DVA Capstone 2 project.

Primary dataset:
- UCI Bank Marketing (bank-additional-full.csv)

Business problem:
- Which customer and campaign patterns are associated with higher term-deposit
  subscription, and how can the bank improve campaign efficiency?
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
RAW_FILE = (
    BASE_DIR
    / "data"
    / "raw"
    / "bank_marketing"
    / "bank-additional"
    / "bank-additional"
    / "bank-additional-full.csv"
)
PROCESSED_DIR = BASE_DIR / "data" / "processed"


MONTH_ORDER = ["mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
DAY_MAP = {"mon": "Monday", "tue": "Tuesday", "wed": "Wednesday", "thu": "Thursday", "fri": "Friday"}
MONTH_MAP = {
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December",
}


def load_data() -> pd.DataFrame:
    return pd.read_csv(RAW_FILE, sep=";")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()

    cleaned.columns = [col.strip().lower().replace(".", "_").replace("-", "_") for col in cleaned.columns]
    cleaned = cleaned.rename(columns={"nr_employed": "number_employed", "y": "subscribed"})

    unknown_cols = ["job", "marital", "education", "default", "housing", "loan"]
    for col in unknown_cols:
        cleaned[col] = cleaned[col].replace("unknown", np.nan)

    cleaned["subscribed_flag"] = cleaned["subscribed"].map({"yes": 1, "no": 0})
    cleaned["contacted_before"] = np.where(cleaned["pdays"] == 999, "No", "Yes")
    cleaned["pdays_clean"] = cleaned["pdays"].replace(999, np.nan)
    cleaned["month_name"] = cleaned["month"].map(MONTH_MAP)
    cleaned["day_name"] = cleaned["day_of_week"].map(DAY_MAP)
    cleaned["age_group"] = pd.cut(
        cleaned["age"],
        bins=[0, 24, 34, 44, 54, 64, 120],
        labels=["18-24", "25-34", "35-44", "45-54", "55-64", "65+"],
    )
    cleaned["campaign_band"] = pd.cut(
        cleaned["campaign"],
        bins=[0, 1, 2, 3, 5, 10, np.inf],
        labels=["1 contact", "2 contacts", "3 contacts", "4-5 contacts", "6-10 contacts", "11+ contacts"],
    )
    cleaned["duration_minutes"] = cleaned["duration"] / 60
    cleaned["previous_contact_band"] = pd.cut(
        cleaned["previous"],
        bins=[-1, 0, 1, 3, np.inf],
        labels=["0", "1", "2-3", "4+"],
    )

    month_order_map = {month: idx for idx, month in enumerate(MONTH_ORDER, start=1)}
    cleaned["month_order"] = cleaned["month"].map(month_order_map)
    cleaned = cleaned.sort_values(["month_order", "day_of_week"]).reset_index(drop=True)

    return cleaned


def build_kpi_tables(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    kpi_overview = pd.DataFrame(
        [
            {"metric": "total_records", "value": int(len(df))},
            {"metric": "subscription_rate_pct", "value": round(df["subscribed_flag"].mean() * 100, 2)},
            {"metric": "avg_call_duration_seconds", "value": round(df["duration"].mean(), 2)},
            {"metric": "share_previously_contacted_pct", "value": round((df["contacted_before"] == "Yes").mean() * 100, 2)},
            {"metric": "missing_job_pct", "value": round(df["job"].isna().mean() * 100, 2)},
            {"metric": "missing_education_pct", "value": round(df["education"].isna().mean() * 100, 2)},
        ]
    )

    def rate_table(group_col: str) -> pd.DataFrame:
        out = (
            df.groupby(group_col, dropna=False, observed=False)
            .agg(
                clients=("subscribed_flag", "size"),
                subscribers=("subscribed_flag", "sum"),
                subscription_rate_pct=("subscribed_flag", lambda s: round(s.mean() * 100, 2)),
                avg_duration_seconds=("duration", lambda s: round(s.mean(), 2)),
            )
            .reset_index()
        )
        return out.sort_values("subscription_rate_pct", ascending=False)

    month_table = rate_table("month_name")
    month_table["month_sort"] = month_table["month_name"].map({v: i for i, v in enumerate(MONTH_MAP.values(), start=1)})
    month_table = month_table.sort_values("month_sort").drop(columns="month_sort")

    return {
        "kpi_overview": kpi_overview,
        "subscription_by_contact": rate_table("contact"),
        "subscription_by_month": month_table,
        "subscription_by_job": rate_table("job"),
        "subscription_by_age_group": rate_table("age_group"),
        "subscription_by_campaign_band": rate_table("campaign_band"),
        "subscription_by_previous_outcome": rate_table("poutcome"),
        "subscription_by_education": rate_table("education"),
    }


def save_outputs(cleaned: pd.DataFrame, tables: dict[str, pd.DataFrame]) -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    cleaned.to_csv(PROCESSED_DIR / "bank_marketing_cleaned.csv", index=False)
    cleaned.to_csv(PROCESSED_DIR / "bank_marketing_tableau.csv", index=False)

    for name, table in tables.items():
        table.to_csv(PROCESSED_DIR / f"{name}.csv", index=False)


def main() -> None:
    raw = load_data()
    cleaned = clean_data(raw)
    tables = build_kpi_tables(cleaned)
    save_outputs(cleaned, tables)
    print("Processed bank marketing outputs generated successfully.")


if __name__ == "__main__":
    main()
