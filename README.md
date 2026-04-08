# DecodeLabs Internship
📊 Data Analytics Project – Sales Insights Dashboard

📌 Project Overview
This project focuses on end-to-end data analysis of a retail transactional dataset. It involves data cleaning, exploratory data analysis (EDA), SQL querying, and dashboard development using Streamlit to generate actionable business insights.
The goal is to simulate a real-world data analyst workflow and present insights in a clear, business-friendly format.

🎯 Objectives
Clean and preprocess raw data
Perform exploratory data analysis (EDA)
Identify trends, patterns, and outliers
Analyze product performance, payment methods, and coupon usage
Build an interactive dashboard using Streamlit
Perform SQL-based analysis for structured querying

🛠️ Tech Stack
Python (Pandas, NumPy)
Visualization: Matplotlib
SQL (MySQL)
Dashboard: Streamlit
Tools: Excel, MySQL Workbench, VS Code

📂 Dataset Description
The dataset contains transactional data with the following fields:
Date – Transaction date
Product – Product purchased
Quantity – Number of units
UnitPrice – Price per unit
TotalPrice – Total transaction value
PaymentMethod – Mode of payment
CouponCode – Applied coupon (if any)
CustomerID – Unique customer identifier

🧹 Data Cleaning Steps
Handled missing values:
Replaced null/blank CouponCode with "No Coupon"
Checked and removed duplicates
Converted date column to datetime format
Created derived column: YearMonth
Validated data consistency (TotalPrice = Quantity × UnitPrice)
Handled outliers using IQR method (capping strategy)

📊 Exploratory Data Analysis (EDA)

📈 Monthly Trend Analysis
No strong upward or downward trend observed
Indicates stable order volume over time

📦 Product Analysis
Printer is the top-selling product
Demand is evenly distributed across products
Indicates a balanced product portfolio

💳 Payment Method Analysis
Online payment is most preferred
Cash and card payments are also significant
Shows a hybrid payment ecosystem

🎟️ Coupon Usage Analysis
Free shipping coupon is most popular
Many users purchase without coupons
Suggests strong base demand and margin opportunity

💎 High-Value Transactions
Top 5% transactions identified using quantile method
Helps identify premium customers

🗄️ SQL Analysis
Performed SQL-based analysis including:
Filtering (WHERE)
Aggregation (SUM, AVG, COUNT)
Grouping (GROUP BY)
Sorting (ORDER BY)

Example Query:
SELECT Product, SUM(TotalPrice) AS Revenue
FROM sales_data
GROUP BY Product
ORDER BY Revenue DESC;

📌 Key Business Insights
Stable order trend indicates consistent demand
Balanced product distribution reduces business risk
Digital payments are leading but traditional methods remain relevant
Free shipping is more effective than discount-based coupons
High-value customers contribute significantly to revenue

🎯 Learning Outcomes
Data cleaning and preprocessing techniques
Exploratory data analysis (EDA)
SQL querying and data extraction
Dashboard development using Streamlit
Business storytelling with data

📎 Future Improvements
Add interactive charts using Plotly
Perform customer segmentation (RFM analysis)
Build predictive models (sales forecasting)
Deploy dashboard online (Streamlit Cloud)

👨‍💻 Author
Avisek Bose
Aspiring Data Analyst | Finance Domain Specialist
