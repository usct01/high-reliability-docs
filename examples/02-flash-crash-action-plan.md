# GOAL ACTION PLAN: EQUITY INDEX FLASH CRASH & LIQUIDITY RESPONSE
**Timestamp:** 11 November 2026, 14:05 IST
**Primary Time Zone:** IST (UTC+05:30)

## 1. CONTEXT & IMPACT
- **Current Situation / Root Cause:** Benchmark equity index futures dropped 6.2 percent within four minutes due to an external liquidity vacuum. Bid-ask spreads across mid-cap holdings widened beyond 120 basis points.
- **Available Teams & Dependencies:** Quantitative Execution Desk, Portfolio Risk Team, Prime Brokerage Operations, and Exchange Connectivity Engineering.
- **Assumptions:** Primary exchange matching engines remain operational and clearinghouse margin portals remain accessible.

## 2. OBJECTIVE
The Quantitative Execution and Risk teams will stabilize net portfolio delta exposure and restore automated order routing no later than 15:15 IST on the National Stock Exchange in order to prevent forced margin liquidation and limit fund drawdown below 3.0 percent.

## 3. EXECUTION
- **Leadership Intent / Desired End State:** All passive market-making algorithms remain paused until bid-ask spreads normalize below 15 basis points. Net portfolio beta sits within 0.05 of target mandate bounds, and zero unacknowledged orders remain open in the Order Management System (OMS).
- **Phased Rollout:** Phase I (Immediate Order Cancellation & Exposure Freeze), Phase II (Index Futures Delta Hedging), Phase III (Controlled Algorithm Reactivation).
- **Team Assignments:**
  - **Quantitative Execution Desk:**
    - *Task:* Cancel all resting limit orders across mid-cap equities and execute offsetting index futures hedges.
    - *Purpose:* Eliminate adverse fill risk during extreme spread widening and neutralize directional market exposure.
  - **Portfolio Risk Team:**
    - *Task:* Calculate real-time Net Asset Value (NAV) drawdown and intraday Variation Margin obligations every 10 minutes.
    - *Purpose:* Ensure uninterrupted liquidity coverage with prime brokers before market close.
  - **Exchange Connectivity Engineering:**
    - *Task:* Audit Financial Information eXchange (FIX) drop-copy sessions against exchange execution reports.
    - *Purpose:* Confirm zero orphaned orders or duplicate fills exist in internal position ledgers.
- **Coordinating Instructions:** Do not re-enable automated Volume-Weighted Average Price (VWAP) execution engines without joint sign-off from the Head of Trading and Chief Risk Officer.

CRITICAL: Confirm full cancellation of resting cash-equity orders before you transmit index futures hedge orders to prevent double exposure.

1. Open the OMS Kill-Switch Console and select all active mid-cap equity strategies.
2. Click `CANCEL ALL WORKING ORDERS` and verify that open order count equals zero.
3. Calculate net unhedged portfolio beta on the Real-Time Risk Dashboard.
4. Transmit short index futures orders in tranches of 50 contracts until net beta reaches 0.00.
5. Verify that exchange execution acknowledgments match internal position ledgers within 30 seconds.

## 4. RESOURCES & HANDOFFS
- **Tooling & Infrastructure:** OMS Kill-Switch Console, Real-Time Risk Dashboard, Prime Broker Margin Portal, and FIX Drop-Copy Monitor.
- **Staffing & Shift Rotation:** Current Asia-Pacific trading desk maintains coverage through market close at 15:30 IST, handing over post-trade reconciliation to the London Middle Office at 16:00 IST.

## 5. ESCALATION & COMMS
- **Decision Chain:** Head of Quantitative Trading (Primary Incident Lead), followed by Chief Risk Officer, followed by Chief Investment Officer.
- **Communication Channels:**
  - *Primary Channel:* `#market-dislocation-war-room`
  - *Backup Channel:* Trading Floor Bridge Line (`ext. 4400`)
  - *Status Cadence:* Written status update posted every 15 minutes on the quarter-hour.
