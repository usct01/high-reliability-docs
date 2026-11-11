# INSTITUTIONAL PORTFOLIO REBALANCING PROCEDURE

## 1. Prerequisites & Access
- Approved Target Weight File (`rebalance_weights_YYYYMMDD.csv`) signed by the Lead Portfolio Manager
- Read/Write access to the Portfolio Management System (PMS) and Order Management System (OMS)
- Verified custodian cash balance reconciliation report from T-1 market close

## 2. Hazard & Risk Precautions
CRITICAL: Verify corporate action adjustments before you generate trade lists to prevent short-selling restricted shares.
CAUTION: Do not transmit basket orders during the first 15 minutes after market open when opening auction volatility peaks.

## 3. Procedure
1. Download the signed target weight file from the Portfolio Governance Repository.
2. Confirm that total target portfolio weights equal exactly 100.00 percent.
3. Import the target weight file into the PMS Rebalancing Staging Module.
4. Run the Pre-Trade Compliance Check to verify sector and issuer concentration limits.

   CAUTION: Resolve all compliance warning flags before you stage orders in the OMS.

5. Generate the net rebalance trade list against settled custodian positions.
6. Set minimum trade lot threshold to 0.05 percent of Net Asset Value (NAV) to eliminate dust orders.
7. Route the approved trade basket to the OMS Execution Blotter using a Volume-Weighted Average Price (VWAP) strategy.
8. Verify that all parent orders display status `ACTIVE` in the OMS Execution Blotter.
