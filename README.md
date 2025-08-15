saas-ltv-cac-simulation
Project Overview
This project simulates the financial performance of a SaaS (Software-as-a-Service) startup using common venture capital metrics.
It takes a company’s monthly operating data — revenue per user, churn rate, customer acquisition costs, operating expenses, and starting cash — and projects customer growth, monthly recurring revenue (MRR), gross margins, cash burn, and runway.
The key outputs are:
LTV (Lifetime Value): average revenue a customer is expected to generate over their lifetime
CAC (Customer Acquisition Cost): cost to acquire a single customer
LTV:CAC Ratio: a quick measure of whether customer acquisition is profitable
CAC Payback Period: how long it takes to recover acquisition costs
Runway: how many months until the company runs out of cash at the current burn rate
This type of modeling is widely used in venture capital and startup finance to test the sustainability of a company’s growth plan before making investment decisions.
Skills Demonstrated
Modeled startup growth and cash flow scenarios in Python using pandas and numpy
Translated SaaS finance concepts into working code and formulas
Simulated monthly customer and revenue changes based on churn and acquisition rates
Calculated core venture capital metrics from operational data
Produced clean CSV outputs for both metrics and month-by-month projections
Used Git & GitHub for version control and project sharing
Results Summary (Example Simulation)
LTV: $637.50 per customer
LTV:CAC Ratio: 2.66 (customers are worth more than double their acquisition cost)
CAC Payback: 9.4 months to recover acquisition costs
Runway: -8.5 months (the company would run out of cash in under a year without changes)
Takeaway: The LTV:CAC ratio suggests strong unit economics, but the short runway shows the company would need to raise capital or reduce burn to sustain growth.
How to Run
Clone the repository:
git clone https://github.com/PaddyFinan/saas-ltv-cac-simulation.git
cd saas-ltv-cac-simulation
Install dependencies:
pip install -r requirements.txt
Run the simulation:
python saas_model.py
Outputs will be saved in the outputs/ folder:
metrics.csv → LTV, CAC payback, runway, and ratio calculations
monthly_simulation.csv → month-by-month customer, revenue, and cash flow projections
Files in This Project
saas_model.py → Simulation and metric calculation script
data/inputs.csv → Example monthly projection data
outputs/ → Generated CSV results
requirements.txt → Python dependencies
README.md → Project overview and results
