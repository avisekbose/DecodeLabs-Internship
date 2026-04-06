import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the dataset
df = pd.read_excel('Dataset for Data Analytics.xlsx')
df.fillna({'CouponCode':'NO COUPON'}, inplace=True) # Handling Null Values imputing with no coupon

# Page configuration
st.set_page_config(page_title="E-Commerce Data Analytics Dashboard", layout="wide")
st.title("E-Commerce Data Analytics Interactive Dashboard")
st.write("This dashboard provides insights into the dataset for our E-Commerce Data Analytics project. Use the filters in the sidebar to explore the data.")
st.write('Author: Avisek Bose')

st.subheader("Data Visualization and Insights")

# Side bar for user input
st.sidebar.write('### Dataset:')
st.sidebar.write('Dataset for Data Analytics.xlsx')
st.sidebar.write('Shape of the dataset:', df.shape)
st.sidebar.header("Filters")
selected_product = st.sidebar.multiselect("Products", df['Product'].unique(), default=df['Product'].unique())
selected_payment = st.sidebar.multiselect("Payment Methods", df['PaymentMethod'].unique(), default=df['PaymentMethod'].unique())
selected_order_status = st.sidebar.multiselect("Order Status", df['OrderStatus'].unique(), default=df['OrderStatus'].unique())
selected_coupon_code = st.sidebar.multiselect('Coupon Code', df['CouponCode'].unique(), default=df['CouponCode'].unique())
filtered_df = df[(df['Product'].isin(selected_product)) & (df['PaymentMethod'].isin(selected_payment)) & (df['OrderStatus'].isin(selected_order_status)) & (df['CouponCode'].isin(selected_coupon_code))]

# KPI Metrics
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Orders", len(filtered_df))
col2.metric("Total Revenue", '$' + str(round(filtered_df['TotalPrice'].sum(), 2)))
col3.metric("Avg Order Value", '$' + str(round(filtered_df['TotalPrice'].mean(), 2)))

st.subheader("Histogram Analysis")
numerical_cols = ['Quantity', 'UnitPrice', 'ItemsInCart', 'TotalPrice']
selected_col = st.selectbox("Select Column", numerical_cols)
fig, ax = plt.subplots(figsize=(12,5))
ax.hist(df[selected_col], bins=20)
ax.set_title(f"Distribution of {selected_col}")
ax.set_xlabel(selected_col)
ax.set_ylabel("Frequency")
st.pyplot(fig)

st.subheader("Box Plot Analysis")
fig, ax = plt.subplots(figsize=(12,5))
ax.boxplot(df[selected_col])
ax.set_title(f"Box Plot of {selected_col}")
ax.set_xlabel(selected_col)
ax.set_ylabel(selected_col)
st.pyplot(fig)

st.subheader("Correlation Heatmap")
corr = filtered_df[numerical_cols].corr()
fig, ax = plt.subplots(figsize=(12, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Monthly Trend
st.subheader("Monthly Orders Trend")
monthly_orders = filtered_df.groupby(filtered_df['Date'].dt.to_period('M')).size()
fig1, ax1 = plt.subplots(figsize=(12, 5))
monthly_orders.plot(ax=ax1, marker='o')
ax1.set_title("Monthly Orders")
ax1.set_xlabel("Month")
ax1.set_ylabel("Orders")
st.pyplot(fig1)
st.write('### Insights:')
st.write('No Strong Upward or Downward Trend in Monthly Orders')

# Product Analysis
st.subheader("Top Products")
product_counts = filtered_df['Product'].value_counts().sort_values()
fig2, ax2 = plt.subplots(figsize=(12, 5))
product_counts.plot(kind='barh', ax=ax2)
ax2.set_title("Top 10 Products")
st.pyplot(fig2)
st.markdown("""
### Product Insights:
1. Printer is the Top-Selling Product Highest number of orders (~180+) Indicates strong demand / high utility product
Business Action: Ensure high inventory availability Run premium pricing or bundled offers
2. Tablet and Chair Close Behind Very similar order volumes (~175–178) Suggests consistent demand across categories (tech + furniture)
Insight: Your business is not dependent on a single category
3. Laptops & Desks Show Strong Mid-Level Demand Slightly lower but still high (~170 range)
Business Action: Bundle offers: Laptop + Desk combo Increase cross-selling opportunities
4. Monitor & Phone Slightly Lower Still strong (~155–165), but comparatively less
Possible Reasons: Higher price sensitivity Less frequent replacement cycle
Action: Offer discounts or EMI options Improve marketing visibility
5. Demand is Fairly Even (Important Insight) No extreme drop-off between products All products fall within a narrow range (~150–180)
This means: Balanced product portfolio Lower business risk (not dependent on one product)       
6. No “Low Performer” in Top 10
Insight: All top products are consistently contributing Suggests healthy product mix
Advanced Business Insight
This looks like a high-frequency retail dataset, where:
Products are either:
Everyday-use items Or popular electronics/furniture
The demand distribution is relatively uniform, indicating stable consumption patterns and a diversified revenue stream.""")

# Payment Method
st.subheader("Payment Methods")
payment_counts = filtered_df['PaymentMethod'].value_counts()
fig3, ax3 = plt.subplots(figsize=(12, 5))
payment_counts.plot(kind='bar', ax=ax3)
ax3.set_title("Payment Distribution")
st.pyplot(fig3)
st.markdown("""
### Payment Insights:
1. Online is the Most Preferred Payment Method Highest transactions (~260) Indicates strong digital adoption
Business Insight: Customers prefer convenience & speed
Action: Optimize online payment UX Offer cashback / digital discounts
2. Cash Still Has Strong Presence Second highest (~245) Shows a hybrid customer base
Insight: Not all users are fully digital yet
Action: Keep cash option available, Gradually push digital via incentives
3. Credit Card, Debit Card, Gift Card Are Similar All around (~230–235) Very close distribution
Insight: No dominant card type Customers are flexible in payment choices
4. Balanced Payment Ecosystem (Very Important) No method is extremely low All methods are within a tight range (~230–260)
This means: Low dependency risk Business is well-diversified across payment channels
5. Slight Drop from Online → Others, Online leads, but difference is not huge
Insight: Opportunity to increase digital dominance
Action:
    Introduce:
        UPI offers
        Card cashback
        Wallet rewards
Advanced Business Insight
"The payment distribution indicates a well-balanced mix of traditional and digital methods, with online payments leading slightly. This suggests a transitioning customer base where digital adoption is growing but cash and card-based transactions remain significant.""")
            
# Coupon Usage
st.subheader("Coupon Usage")
coupon_counts = filtered_df['CouponCode'].value_counts().head(10)
fig4, ax4 = plt.subplots(figsize=(12, 5))
coupon_counts.plot(kind='bar', ax=ax4)
ax4.set_title("Top Coupons")
st.pyplot(fig4)
st.markdown("""
### Coupon Usage Insights
1. FREESHIP is the Most Used Coupon Highest usage (~315) Outperforms all discount-based coupons
Insight: Customers value free shipping more than discounts
Business Action: Promote free shipping campaigns Use FREESHIP as a primary acquisition strategy
2. “NO COUPON” is Almost as High Second highest (~310)
Insight: Large number of customers are willing to buy without discounts
What this means: Strong brand value / product demand Opportunity to increase margins
Action: Avoid over-discounting Target only price-sensitive users with coupons
3. WINTER15 Performs Moderately Well Mid-level usage (~290)
Insight: Seasonal campaigns work but are not dominant
Action: Improve timing & promotion, Combine with: Free shipping Limited-time urgency
4. SAVE10 is the Least Used Lowest (~285)
Insight: Flat discounts may be less attractive
Possible Reasons: Not high enough discount Less visibility Less perceived value vs free shipping
Action:
    Test:
        Higher discount (SAVE20)
        Combo offers (SAVE10 + FREESHIP)
5. Small Gap Between Coupons All coupons are within a narrow range (~285–315)
This means: No single campaign dominates strongly Marketing effectiveness is moderately balanced
6. Key Strategic Insight The data suggests that logistics-related incentives like free shipping drive higher engagement than direct discounts, while a significant portion of customers purchase without any coupon, indicating strong underlying demand.""")

# Top 10 Customers
st.subheader("Top 10 Customers")
top_customers = filtered_df.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False).head(10)
fig5, ax5 = plt.subplots(figsize=(12, 5))
top_customers.plot(kind='bar', ax=ax5)
ax5.set_title("Top 10 Customers by Revenue")
ax5.set_xlabel("Customer ID")
ax5.set_ylabel("Total Revenue")
st.pyplot(fig5)
st.markdown("""
### Top Customers Insights:
1. Customer Concentration: The top 10 customers contribute a significant portion of total revenue, indicating a high customer concentration risk.
2. Revenue Distribution: The revenue from the top customers is relatively evenly distributed, suggesting that there isn't a single dominant customer driving the majority of sales.
3. Customer Loyalty: The presence of high-spending customers indicates potential loyalty and satisfaction with the products or services offered.
4. Business Strategy: Focusing on retaining these top customers through personalized marketing, loyalty programs, and exclusive offers could be beneficial for sustaining revenue.
5. Risk Management: While having high-value customers is advantageous, it also poses a risk if any of these customers were to stop purchasing. Diversifying the customer base and acquiring new customers should also be a priority to mitigate this risk.""")


# Order Status Distribution
st.subheader("Order Status Distribution")
os_count = filtered_df['OrderStatus'].value_counts()
fig6, ax6 = plt.subplots(figsize=(12, 5))
os_count.sort_values().plot(kind='bar', ax=ax6)
ax6.set_title("Order Status Distribution")
ax6.set_xlabel("Order Status")
ax6.set_ylabel("Number of Orders")
st.pyplot(fig6)
st.markdown("""
### Order Status Insights:
1. High Proportion of Completed Orders: The majority of orders are marked as "Completed," indicating a successful transaction process and customer satisfaction.
2. Low Cancellation Rate: The number of "Cancelled" orders is relatively low, suggesting that customers are generally satisfied with their purchases and the order fulfillment process. This could also indicate effective customer service and return policies.
3. Minimal Returns: The "Returned" status is also low, which may imply that the products meet customer expectations and that the return process is efficient.
4. Business Implication: The high completion rate and low cancellation/return rates are positive indicators for the business, suggesting strong customer satisfaction and effective operational processes. However, continuous monitoring of these metrics is essential to maintain and improve customer experience.""")
