# 🌍 Top 10 Largest Economies by GDP

## 📌 Project Overview
This project shows how to **extract data from a website, process it, and save it** using Python.  
We find the **top 10 largest economies** in the world based on **IMF GDP (nominal) data**.

---

## 🌐 Data Source
- Wikipedia page (archived):  
[https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)](https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29)

---

## 🛠 Tools
- **Python 3**  
- **Pandas** – for tables and data processing  
- **NumPy** – for numbers and rounding  
- **lxml** – for reading HTML tables  

---

## 🔹 Steps

1. **Extract the Data**
   - Read tables from the website using `pandas.read_html()`  
   - Select the **3rd table** which contains GDP information  

2. **Process the Data**
   - Keep **top 10 countries**  
   - Take columns: **Country** and **GDP (IMF)**  
   - Convert GDP from **Million USD → Billion USD**  
   - Round numbers to **2 decimal places**  

3. **Save the Data**
   - Export the final table as CSV: `Largest_economies.csv`  

---

## 💾 Output Example

| Country       | GDP (Billion USD) |
|---------------|-----------------|
| United States | 105568.78       |
| China         | 26854.60        |
| Japan         | 19373.59        |
| Germany       | 4409.73         |
| India         | 4308.85         |
| ...           | ...             |

---

## ⚡ How to Run
```bash
# Install required libraries
pip install pandas numpy lxml

# Run the script
python largest_economies.py

📝 Notes
- This project demonstrates basic data engineering skills:
  - Web scraping
  - Data cleaning
  - Numerical transformation
  - Saving to CSV

**Created by [Abdullah Ahmed]**



