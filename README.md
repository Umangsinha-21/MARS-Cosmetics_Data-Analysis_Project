
# 💄 MARS Cosmetics Analytics Dashboard | Data Analysis Project

### 📊 Unveiling Data-Driven Beauty Decisions

This interactive Power BI dashboard project analyzes real-world product and sales data from **MARS Cosmetics**, a brand known for crafting products tailored for Indian skin tones. By blending social media engagement metrics, customer feedback, and regional sales trends, the dashboard uncovers deep insights into what drives the brand’s performance — both online and offline.

---

## 🛠️ Project Description

This project encapsulates a full data pipeline workflow:

* 🔍 **Data Collection**: Scraped real-world product listings and metrics from MARS Inc.'s online platforms using **Python**.
* 🧹 **Data Cleaning & Integration**: Transformed and merged datasets using **SQL** (joins, aggregations) and **Excel Power Query** for a unified analytics-ready dataset.
* 📈 **Exploratory & Comparative Analysis**: Identified product performance trends, analyzed category-level ratings, regional preferences, and pricing effectiveness.
* 📉 **Storytelling through Data**: Built an interactive and visually rich **Power BI** dashboard to support strategic decision-making for marketing, inventory, and pricing.

---

## 🔑 Key Insights You Can Discover

* **💥 What Drives Engagement on Social Media?**

  * Image posts outperform videos dramatically (Image posts = 290K+ likes vs. 10K on videos).
  * Sunday posts have the highest engagement across likes and comments, peaking at **73K+**.

* **📦 Product Analytics at a Glance**

  * **Eyes** category has the highest product count.
  * Top-reviewed product: **Blur Base (Face)** with 910 reviews and a perfect 5.0 rating.
  * Overall product rating: **4.22**, indicating strong customer satisfaction across categories.

* **🌍 Regional Sales Breakdown**

  * **Delhi** dominates with ₹9.9M in monthly sales and the highest store traffic (81K+ footfall).
  * Refill frequencies suggest operational hotspots in **Delhi**, **Maharashtra**, and **West Bengal**.

* **📅 Performance by Time**

  * Best time to post: Around **10 AM & 8 PM**.
  * Sunday and Tuesday show the highest post performance in terms of engagement.

* **💰 Pricing Strategy**

  * Top 5 subcategories (Lip Liner, Cleanser, Highlighter, etc.) priced around ₹424–₹482, pointing to the mid-premium positioning of the brand.

---

## 📌 Dashboard Features

* **Post-Type Engagement Visuals**: Analyze performance across images vs. videos.
* **Year-wise Trendline**: Compare how engagement, likes, and comments evolved from 2022–2025.
* **Category-Level Product Distribution**: Breakdown of SKUs across lips, face, skincare, and eyes.
* **Geographical Sales Map**: Pinpoint top-performing states based on footfall, sales, and refill frequency.
* **Top Product Analytics**: Discover best-sellers by review count, price, and rating.

---

## 🧠 Tools & Technologies Used

| Tool              | Purpose                               |
| ----------------- | ------------------------------------- |
| Python            | Web scraping and data extraction      |
| SQL               | Data cleaning, joins, and aggregation |
| Excel Power Query | Data transformation and prep          |
| Power BI          | Dashboard creation and visualization  |

---

```
📁 Folder Structure
bash
Copy
Edit
MARS_Cosmetics_Dashboard/
│
├── 📊 MARS_Dashboard.pbix                # Power BI dashboard file
├── 📄 Dashboard_Report.pdf               # PDF export of the dashboard
│
├── 📁 data/
│   ├── mars_raw_data.csv                # Scraped product data
│   ├── cleaned_data.xlsx                # Cleaned and transformed dataset
│   └── sales_by_state.csv               # Regional sales data
│
├── 📁 python_scripts/
│   ├── scraper.py                       # Web scraping script
│   ├── data_cleaning.py                 # Data preprocessing and formatting
│   └── data_merge.py                    # Dataset merging logic
│
└── 📄 README.md                          # Project documentation
```
---

## 🚀 How It Helps Stakeholders

* **Marketing Teams** can plan content calendars and ad spends based on post engagement patterns.
* **Product Managers** can optimize inventory based on top-reviewed products and refill frequency.
* **Sales Executives** can target regions like **Delhi** and **Maharashtra** for expansion or deeper penetration.
* **Founders & Strategists** gain a comprehensive view of digital and retail performance, enabling smart pricing and product decisions.

---

## 📷 Dashboard Preview

<img width="1310" height="738" alt="Image" src="https://github.com/user-attachments/assets/216aa481-a512-41e5-8969-2364f04b85dd" />

---

## 🙌 Let's Connect!

If you found this project insightful or have feedback to share, feel free to connect or drop a ⭐️ on the repo!

---
