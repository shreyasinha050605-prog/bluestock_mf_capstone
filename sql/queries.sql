-- 1. Top 5 Fund Houses by AUM

SELECT
fund_house,
SUM(aum_crore) AS total_aum
FROM aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;


-- 2. Average NAV by Fund

SELECT
amfi_code,
AVG(nav) AS avg_nav
FROM nav_history
GROUP BY amfi_code;


-- 3. Average NAV Per Month

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM nav_history
GROUP BY month
ORDER BY month;


-- 4. SIP Inflow YoY Growth

SELECT
month,
sip_inflow_crore,
yoy_growth_pct
FROM sip
ORDER BY month;


-- 5. Transactions by State

SELECT
state,
COUNT(*) AS transactions
FROM transactions
GROUP BY state
ORDER BY transactions DESC;


-- 6. Funds With Expense Ratio Below 1%

SELECT
scheme_name,
expense_ratio_pct
FROM performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- 7. Top 10 Funds by 5 Year Return

SELECT
scheme_name,
return_5yr_pct
FROM performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- 8. Average Transaction Amount by Type

SELECT
transaction_type,
AVG(amount_inr) AS avg_amount
FROM transactions
GROUP BY transaction_type;


-- 9. Portfolio Allocation by Sector

SELECT
sector,
SUM(weight_pct) AS total_weight
FROM holdings
GROUP BY sector
ORDER BY total_weight DESC;


-- 10. Highest Sharpe Ratio Funds

SELECT
scheme_name,
sharpe_ratio
FROM performance
ORDER BY sharpe_ratio DESC
LIMIT 10;