saas-ltv-cac-simulation

Project Overview

This project simulates the financial performance of a SaaS (Software-as-a-Service) startup using common venture capital metrics. By taking a company’s monthly operating data — revenue per user, churn rate, customer acquisition costs, operating expenses, and starting cash — the script projects customer growth, monthly recurring revenue (MRR), gross margins, cash burn, and cash runway.

The main goal is to calculate the key SaaS metrics that both founders and investors care about:

LTV (Lifetime Value) — average revenue a customer is expected to generate over their lifetime

CAC (Customer Acquisition Cost) — cost to acquire a single customer

LTV:CAC Ratio — a quick measure of whether customer acquisition is profitable

CAC Payback Period — how long it takes to recover acquisition costs

Runway — how many months until the company runs out of cash at the current burn rate

This type of modeling is widely used in venture capital and startup finance to test the sustainability of a company’s growth plan before making investment decisions.

Skills Demonstrated

While building this, I:

Modeled startup growth and cash flow scenarios in Python using pandas and numpy

Translated SaaS finance concepts into working code and formulas

Simulated monthly customer and revenue changes based on churn and acquisition rates

Calculated core venture capital metrics from operational data

Produced clean CSV output files for metrics and month-by-month projections

Used Git & GitHub for version control and sharing the project

Results Summary (Example Simulation)

LTV: $637.50 per customer

LTV:CAC Ratio: 2.66 (customers are worth more than double their acquisition cost)

CAC Payback: 9.4 months to recover acquisition costs

Runway: -8.5 months (the company would run out of cash in under a year without changes)

Takeaway: With a strong LTV:CAC ratio, the unit economics are promising, but the negative runway shows the company would need to raise more capital or reduce burn to sustain growth.

How to Run

Clone the repository:

git clone https://github.com/PaddyFinan/saas-ltv-cac-simulation.git
cd saas-ltv-cac-simulation

Install dependencies:

pip install -r requirements.txt
Run the simulation:
python saas_model.py
Outputs will be saved in the outputs/ folder, including:
metrics.csv → LTV, CAC payback, runway, and ratio calculations
monthly_simulation.csv → month-by-month customer, revenue, and cash flow projections
Files in This Project
saas_model.py → Full simulation and metric calculation script
data/inputs.csv → Sample input file with monthly projections
outputs/ → Contains generated CSVs with results
requirements.txt → Dependencies needed to run the script
README.md → Project overview and results summary
Files in This Project
saas_model.py → Simulation and metric calculation script
data/inputs.csv → Example monthly projection data
outputs/ → Generated CSV results
requirements.txt → Python dependencies
README.md → Project overview and results

