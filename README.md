# Snack Sales Exploratory Data Analysis (EDA)

## 📌 Project Overview

This project focuses on Exploratory Data Analysis (EDA) of snack sales data using Python. The goal is to understand sales performance, customer behavior, product categories, regional trends, and data quality through data cleaning, statistical analysis, and visualization.

The project uses a Jupyter Notebook to investigate the dataset and extract insights that can support data-driven business decisions.

## 🎯 Problem Statement

Businesses need to understand their sales patterns, customer preferences, product performance, and return behavior to make better decisions. Raw sales data may contain inconsistent values, unusual observations, and calculation discrepancies that can affect analysis.

This project explores snack sales data, validates data quality, analyzes important variables, and identifies patterns and potential business opportunities.

## 🎯 Project Objectives

- Understand the structure and characteristics of the dataset.
- Identify missing values, duplicate records, and data inconsistencies.
- Validate dates, numeric ranges, sales values, and return status.
- Standardize product, category, city, and region values.
- Analyze sales across products, categories, regions, and customer segments.
- Explore customer ratings, payment methods, discounts, and returns.
- Communicate findings and potential business recommendations.

## 📂 Project Structure

```text
EDA_SNACK_PROJECT/
│
├── Data/
│   ├── Raw_Data/
│   │   ├── EDA_Snack_Data_Dictionary.csv
│   │   └── EDA_Snack_Dirty_100000.csv
│   ├── Cleaned_Data/
│       └── cleaned_report.csv
│   
│
├── notebooks/
│   └── eda_portfolio_text_added.ipynb
│
├── Docs/
│   └── writing-block.md
│
├── README.md
├── requirements.txt
└── .gitignore
*Note: The notebook filename and folder structure above are examples of the recommended organization. Adjust them to match your actual files.*

## 📊 Dataset Description

The dataset contains snack sales records with **97,307 rows and 15 columns**.

| Column | Description |
|---|---|
| `order_id` | Identifier for an order record |
| `order_date` | Date of the transaction |
| `product_name` | Name of the snack product |
| `category` | Product category |
| `region` | Sales region |
| `city` | City associated with the record |
| `customer_age` | Customer age |
| `customer_segment` | Customer group |
| `unit_price` | Price per unit |
| `quantity` | Quantity recorded |
| `discount` | Discount value |
| `total_sales` | Recorded sales amount |
| `payment_method` | Payment method used |
| `customer_rating` | Customer rating |
| `returned` | Return status |

The dataset covers transactions dated from January 2023 through December 2024.

## 🛠️ Tools and Technologies

- **Python** — data analysis
- **Pandas** — data manipulation and cleaning
- **NumPy** — numerical operations
- **Matplotlib** — data visualization
- **Seaborn** — statistical visualization
- **Jupyter Notebook** — interactive analysis

## 🔍 Analysis Workflow

### 1. Data Loading and Initial Inspection
- Load the dataset into a Pandas DataFrame.
- Review its dimensions, column names, and data types.
- Generate descriptive statistics.

### 2. Data Quality Assessment
- Check for missing values and duplicate records.
- Validate order identifiers and date ranges.
- Check numeric values such as age, price, quantity, discount, and rating.
- Investigate unusual values and inconsistencies.

### 3. Data Cleaning and Standardization
- Standardize text values.
- Review product and category mappings.
- Check city and region consistency.
- Validate the relationship between return status and sales values.
- Investigate discrepancies between recorded sales and calculated sales.

### 4. Exploratory Data Analysis
- Perform univariate analysis to understand individual variables.
- Perform bivariate analysis to examine relationships between variables.
- Perform multivariate analysis to explore patterns across multiple variables.
- Use charts and summary statistics to communicate patterns.

### 5. Export
- Save the processed dataset for future analysis or reuse.

## ❓ Key Business Questions

- Which snack categories generate the most recorded sales?
- Which regions and cities contribute most to sales?
- How do sales vary over time?
- Which customer segments account for the most transactions?
- Which payment methods are used most frequently?
- How are discounts related to recorded sales?
- What patterns appear in customer ratings?
- What is the return rate, and how do returns relate to sales values?
- Are there data quality issues that could affect business conclusions?

## ⚠️ Data Quality Considerations

The analysis includes checks for inconsistent values and discrepancies between recorded sales and sales calculated from price, quantity, and discount.

These discrepancies should be investigated before treating calculated or recorded sales totals as definitive. Negative sales values associated with returned transactions should also be interpreted in the context of the dataset's business rules.

Findings and recommendations should be based on validated results from the completed notebook.

## 💡 Potential Business Applications

The analysis can help businesses:

- Understand product and regional sales performance.
- Identify customer segments for further investigation.
- Monitor customer ratings and return behavior.
- Review discount patterns and sales calculations.
- Improve the reliability of sales reporting.
- Identify opportunities for further analysis and business planning.

These are potential applications; specific recommendations should be supported by the final analysis results.

## 🚀 How to Run the Project

### Prerequisites

Install Python and Jupyter Notebook, or use an environment that supports Jupyter notebooks.

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd EDA_SNACK_PROJECT
```

### 2. Create and activate a virtual environment (optional)

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Open Jupyter Notebook

```bash
jupyter notebook
```

Open the project notebook and run the cells in order.

**Note:** Ensure the dataset path in the notebook matches the location of `report_tes5.csv` in your local project.

## 📌 Conclusion

This project demonstrates a structured EDA workflow, including data inspection, validation, cleaning, standardization, statistical analysis, and visualization. It emphasizes the importance of checking data quality before drawing conclusions from sales data.

The notebook serves as a foundation for deeper business analysis and future machine learning projects.

## 👤 Author

Balaji S

GitHub: https://github.com/Balajis2002bs
