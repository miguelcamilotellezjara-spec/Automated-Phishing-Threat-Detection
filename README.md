AI-Sentinel: Automated Phishing & Social Engineering Defense
📌 Project Overview
AI-Sentinel is an end-to-end security solution that bridges the gap between raw data and actionable business intelligence. It uses a Python-based detection engine to classify phishing attempts and an interactive Power BI dashboard to visualize organizational risk in real-time.
🛠️ The Problem
Cybersecurity teams struggle to track the volume and success rate of phishing attacks across fragmented systems. Without a centralized dashboard, it is difficult to identify trends or verify the effectiveness of automated security filters.
🚀 The Solution
This project provides a full-stack technical workflow:
Detection Engine (Python): A script that analyzes email content, flags suspicious patterns (e.g., "URGENT", "Winner", "Bank Account Locked"), and assigns a binary classification.
Automated Logging: The engine writes detection results to a structured security_logs.csv file, creating a reliable audit trail.
BI Reporting (Power BI): A dynamic dashboard that consumes the CSV data and uses DAX measures to calculate:
Phishing Detection Rate (%): A real-time KPI of system accuracy.
Status Distribution: A visual breakdown of Safe vs. Malicious emails.
Threat Triage Table: A detailed list of flagged content for immediate review.
💻 Tech Stack
Backend: Python (Data Processing & Logic)
Data Visualization: Power BI (DAX, Data Modeling)
Storage: CSV / Flat File Database
Version Control: Git / GitHub
📈 Dashboard Features
Gauge Visual: Provides an instant "at-a-glance" look at the overall detection success rate.
Conditional Formatting: Uses color-coded logic (Red for Phishing, Green for Success) to speed up decision-making.
Interactive Slicers: (Optional) Allows users to filter threats by date or severity.
🏗️ How to Run
Clone the Repo: git clone https://github.com
Generate Data: Run python phishing_detector.py to process new emails and update the logs.
View Insights: Open AI_Sentinel_Dashboard.pbix in Power BI Desktop and click Refresh.
