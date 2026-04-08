# Loading Schema
use `decodelabs-internship`;

# Viewing Dataset
select * from `datasetfordataanalytics`;

# Identifing Missing Values
select * from datasetfordataanalytics
where CouponCode is null or trim(CouponCode) = '';

set sql_safe_updates = 0;

# Imputing Missing Values
update datasetfordataanalytics
set CouponCode = 'No Coupon'
where CouponCode is null or trim(CouponCode) = '';

set sql_safe_updates = 1;

# Checking imputation of missing values
select * from datasetfordataanalytics
where CouponCode = 'No Coupon';

# Identifying High Value Orders
select * from datasetfordataanalytics
where TotalPrice > 1000;

# Identifying Orders using Coupons
select * from datasetfordataanalytics
where CouponCode != 'No Coupon';

# KPI Metrics
# Total Revenue
select round(SUM(TotalPrice),2) as TotalRevenue
from datasetfordataanalytics;

# Total Orders
select count(*) as TotalOrders
from datasetfordataanalytics;

# Avg. Order values
select round(avg(TotalPrice),2) as AvgOrderValue
from datasetfordataanalytics;

# Top Performing Products
select Product, count(*) as Orders, round(sum(TotalPrice),2) as Revenue
from datasetfordataanalytics
group by Product
order by Revenue desc;

# Customer Payment Preference
select 	PaymentMethod, count(*) as Transactions, round(sum(TotalPrice),2) as Revenue
from datasetfordataanalytics
group by PaymentMethod
order by Revenue desc;

# Coupon Performance
select CouponCode, count(*) as CouponUsage, round(sum(TotalPrice),2) as Revenue
from datasetfordataanalytics
group by CouponCode
order by CouponUsage desc;

# Monthly Order Trend
select date_format(Date, '%Y-%m') as YearMonth, count(*) as Orders
from datasetfordataanalytics
group by YearMonth
order by YearMonth;

# Monthly Revenue Trend
select date_format(Date, '%Y-%m') as YearMonth, round(sum(TotalPrice),2) as Revenue
from datasetfordataanalytics
group by YearMonth
order by YearMonth;

# Identifying High Value / Premium Customers
select * from datasetfordataanalytics
order by TotalPrice desc
limit 10;

# YoY Growth
select date_format(Date, '%Y') as Year, count(*) as Orders, round(sum(TotalPrice),2) as Revenue
from datasetfordataanalytics
group by Year
order by Year;

# Order Status Distribution
select OrderStatus, count(*) as Orders,
    round(count(*) * 100.0 / (select count(*) from datasetfordataanalytics), 2) as Percentage
from datasetfordataanalytics
group by OrderStatus;

