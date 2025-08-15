import pandas as pd
import numpy as np
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "inputs.csv"
OUTPUTS_DIR = Path(__file__).parent / "outputs"
OUTPUTS_DIR.mkdir(exist_ok=True)

def ltv(arpu, gross_margin_pct, churn_pct):
    gm = gross_margin_pct / 100.0
    churn = max(churn_pct / 100.0, 1e-6)
    return arpu * gm / churn

def cac_payback_months(cac, arpu, gross_margin_pct):
    gm = gross_margin_pct / 100.0
    m_contribution = arpu * gm
    return np.inf if m_contribution <= 0 else cac / m_contribution

def simulate(path=DATA_PATH):
    df = pd.read_csv(path, parse_dates=['month'])
    customers = []
    mrr = []
    gross_margin_usd = []
    cac_spend = []
    net_burn = []
    cash = []

    current_customers = 0
    current_cash = 0.0

    for i, row in df.iterrows():
        if i == 0:
            current_customers = int(row['starting_customers'])
            current_cash = float(row['cash_on_hand_usd'])

        churners = current_customers * (row['monthly_churn_pct']/100.0)
        current_customers = int(round(current_customers - churners + row['new_customers']))

        monthly_mrr = current_customers * row['arpu_usd']
        gm_usd = monthly_mrr * (row['gross_margin_pct']/100.0)

        cac = row['new_customers'] * row['cac_per_customer']
        burn = row['opex_burn_usd'] + cac - gm_usd
        current_cash = current_cash - burn

        customers.append(current_customers)
        mrr.append(monthly_mrr)
        gross_margin_usd.append(gm_usd)
        cac_spend.append(cac)
        net_burn.append(burn)
        cash.append(current_cash)

    df['customers'] = customers
    df['mrr_usd'] = np.round(mrr,2)
    df['gross_margin_usd'] = np.round(gross_margin_usd,2)
    df['cac_spend_usd'] = np.round(cac_spend,2)
    df['net_burn_usd'] = np.round(net_burn,2)
    df['cash_balance_usd'] = np.round(cash,2)

    last = df.iloc[-1]
    ltv_est = ltv(last['arpu_usd'], last['gross_margin_pct'], last['monthly_churn_pct'])
    payback = cac_payback_months(last['cac_per_customer'], last['arpu_usd'], last['gross_margin_pct'])
    recent_burn = last['net_burn_usd']
    runway = np.inf if recent_burn <= 0 else last['cash_balance_usd'] / recent_burn

    metrics = {
        "ltv_usd": round(ltv_est,2),
        "ltv_to_cac": round(ltv_est/last['cac_per_customer'],2),
        "cac_payback_months": None if np.isinf(payback) else round(payback,1),
        "runway_months": None if np.isinf(runway) else round(runway,1),
    }

    OUTPUTS_DIR.mkdir(exist_ok=True)
    df.to_csv(OUTPUTS_DIR / "monthly_simulation.csv", index=False)
    pd.Series(metrics).to_csv(OUTPUTS_DIR / "metrics.csv")

    print("Saved:", OUTPUTS_DIR / "monthly_simulation.csv")
    print("Saved:", OUTPUTS_DIR / "metrics.csv")
    print("\nMetrics:\n", metrics)

if __name__ == "__main__":
    simulate()
    