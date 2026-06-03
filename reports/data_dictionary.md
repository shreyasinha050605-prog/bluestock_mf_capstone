# Bluestock Mutual Fund Analytics Capstone

## Data Dictionary

### Project Overview

This document describes the datasets used in the Bluestock Mutual Fund Analytics Capstone project. It provides column definitions, data types, business meanings, and source references for all cleaned datasets stored in the `data/processed/` directory.

---

# Dataset 1: Fund Master

**Source File:** `01_fund_master_clean.csv`

| Column Name        | Data Type | Business Definition                            |
| ------------------ | --------- | ---------------------------------------------- |
| amfi_code          | int64     | Unique AMFI scheme identifier                  |
| fund_house         | object    | Mutual fund company managing the scheme        |
| scheme_name        | object    | Name of the mutual fund scheme                 |
| category           | object    | Broad investment category (Equity, Debt, etc.) |
| sub_category       | object    | Specific scheme classification                 |
| plan               | object    | Plan type (Direct/Regular)                     |
| launch_date        | object    | Scheme launch date                             |
| benchmark          | object    | Benchmark index used for comparison            |
| expense_ratio_pct  | float64   | Annual expense ratio (%)                       |
| exit_load_pct      | float64   | Exit load charged on redemption (%)            |
| min_sip_amount     | int64     | Minimum SIP investment amount                  |
| min_lumpsum_amount | int64     | Minimum lump-sum investment amount             |
| fund_manager       | object    | Name of the fund manager                       |
| risk_category      | object    | Risk classification of the scheme              |
| sebi_category_code | object    | SEBI classification code                       |

---

# Dataset 2: NAV History

**Source File:** `02_nav_history_clean.csv`

| Column Name | Data Type | Business Definition           |
| ----------- | --------- | ----------------------------- |
| amfi_code   | int64     | Unique AMFI scheme identifier |
| date        | object    | NAV date                      |
| nav         | float64   | Net Asset Value of scheme     |

---

# Dataset 3: AUM by Fund House

**Source File:** `03_aum_clean.csv`

| Column Name    | Data Type | Business Definition                    |
| -------------- | --------- | -------------------------------------- |
| date           | object    | Reporting date                         |
| fund_house     | object    | Mutual fund company                    |
| aum_lakh_crore | float64   | Assets Under Management (Lakh Crore ₹) |
| aum_crore      | int64     | Assets Under Management (Crore ₹)      |
| num_schemes    | int64     | Number of schemes managed              |

---

# Dataset 4: Monthly SIP Inflows

**Source File:** `04_sip_clean.csv`

| Column Name               | Data Type | Business Definition                        |
| ------------------------- | --------- | ------------------------------------------ |
| month                     | object    | Reporting month                            |
| sip_inflow_crore          | int64     | Total SIP inflow (Crore ₹)                 |
| active_sip_accounts_crore | float64   | Active SIP accounts (Crore)                |
| new_sip_accounts_lakh     | float64   | New SIP accounts added (Lakh)              |
| sip_aum_lakh_crore        | float64   | SIP Assets Under Management (Lakh Crore ₹) |
| yoy_growth_pct            | float64   | Year-over-Year growth percentage           |

---

# Dataset 5: Category Inflows

**Source File:** `05_category_clean.csv`

| Column Name      | Data Type | Business Definition                 |
| ---------------- | --------- | ----------------------------------- |
| month            | object    | Reporting month                     |
| category         | object    | Mutual fund category                |
| net_inflow_crore | float64   | Net inflow/outflow amount (Crore ₹) |

---

# Dataset 6: Industry Folio Count

**Source File:** `06_folios_clean.csv`

| Column Name         | Data Type | Business Definition           |
| ------------------- | --------- | ----------------------------- |
| month               | object    | Reporting month               |
| total_folios_crore  | float64   | Total investor folios (Crore) |
| equity_folios_crore | float64   | Equity folios (Crore)         |
| debt_folios_crore   | float64   | Debt folios (Crore)           |
| hybrid_folios_crore | float64   | Hybrid folios (Crore)         |
| others_folios_crore | float64   | Other category folios (Crore) |

---

# Dataset 7: Scheme Performance

**Source File:** `07_performance_clean.csv`

| Column Name        | Data Type | Business Definition               |
| ------------------ | --------- | --------------------------------- |
| amfi_code          | int64     | Unique AMFI scheme identifier     |
| scheme_name        | object    | Scheme name                       |
| fund_house         | object    | Fund house name                   |
| category           | object    | Scheme category                   |
| plan               | object    | Plan type                         |
| return_1yr_pct     | float64   | 1-Year return (%)                 |
| return_3yr_pct     | float64   | 3-Year return (%)                 |
| return_5yr_pct     | float64   | 5-Year return (%)                 |
| benchmark_3yr_pct  | float64   | Benchmark 3-Year return (%)       |
| alpha              | float64   | Risk-adjusted excess return       |
| beta               | float64   | Volatility relative to benchmark  |
| sharpe_ratio       | float64   | Risk-adjusted return measure      |
| sortino_ratio      | float64   | Downside-risk-adjusted return     |
| std_dev_ann_pct    | float64   | Annualized standard deviation (%) |
| max_drawdown_pct   | float64   | Maximum historical drawdown (%)   |
| aum_crore          | int64     | Assets Under Management (Crore ₹) |
| expense_ratio_pct  | float64   | Expense ratio (%)                 |
| morningstar_rating | int64     | Morningstar rating score          |
| risk_grade         | object    | Scheme risk grade                 |

---

# Dataset 8: Investor Transactions

**Source File:** `08_transactions_clean.csv`

| Column Name        | Data Type | Business Definition         |
| ------------------ | --------- | --------------------------- |
| investor_id        | object    | Unique investor identifier  |
| transaction_date   | object    | Transaction date            |
| amfi_code          | int64     | Scheme identifier           |
| transaction_type   | object    | SIP / Lumpsum / Redemption  |
| amount_inr         | int64     | Transaction amount (₹)      |
| state              | object    | Investor state              |
| city               | object    | Investor city               |
| city_tier          | object    | Tier classification of city |
| age_group          | object    | Investor age segment        |
| gender             | object    | Investor gender             |
| annual_income_lakh | float64   | Annual income (Lakh ₹)      |
| payment_mode       | object    | Transaction payment mode    |
| kyc_status         | object    | KYC verification status     |

---

# Dataset 9: Portfolio Holdings

**Source File:** `09_holdings_clean.csv`

| Column Name       | Data Type | Business Definition       |
| ----------------- | --------- | ------------------------- |
| amfi_code         | int64     | Scheme identifier         |
| stock_symbol      | object    | Stock ticker symbol       |
| stock_name        | object    | Stock name                |
| sector            | object    | Industry sector           |
| weight_pct        | float64   | Portfolio allocation (%)  |
| market_value_cr   | float64   | Market value (Crore ₹)    |
| current_price_inr | float64   | Current stock price (₹)   |
| portfolio_date    | object    | Portfolio disclosure date |

---

# Dataset 10: Benchmark Indices

**Source File:** `10_benchmark_clean.csv`

| Column Name | Data Type | Business Definition  |
| ----------- | --------- | -------------------- |
| date        | object    | Trading date         |
| index_name  | object    | Benchmark index name |
| close_value | float64   | Closing index value  |

---

## Data Sources

* AMFI Mutual Fund Data
* MFAPI NAV API
* Fund Performance Dataset
* Investor Transaction Dataset
* Portfolio Holdings Dataset
* Benchmark Market Index Dataset

---

## Prepared By

**Shreya Sinha**
Bluestock Mutual Fund Analytics Capstone

Version: Day 2 Submission
