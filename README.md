# 🧹 Employee Data Cleaning using Pandas & NumPy

A practical **data cleaning and preprocessing project** built with **Python, Pandas, and NumPy**.

This project takes an uncleaned Indian employee dataset and applies a complete data-cleaning workflow to make the dataset cleaner and ready for further **Exploratory Data Analysis (EDA)** and **Machine Learning**.

---

## 📌 Project Overview

Real-world datasets are rarely perfect.

They can contain:

* Missing values
* Duplicate records
* Infinite values
* Invalid numerical values
* Negative values
* Extreme/outlier values
* Inconsistent data

The goal of this project is to identify and handle these data-quality issues using **Pandas and NumPy**.

The final result is a cleaned employee dataset that can be used for further analysis.

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Load the employee dataset using Pandas.
2. Inspect the dataset and identify missing values.
3. Detect and replace infinite values.
4. Remove duplicate records.
5. Identify and correct negative salary values.
6. Handle missing salary values.
7. Handle missing performance ratings.
8. Fill remaining numerical missing values.
9. Detect salary outliers using the **3-Sigma Rule**.
10. Validate the cleaned dataset.
11. Export the cleaned dataset as a new CSV file.

---

## 🛠️ Technologies Used

| Technology | Purpose                                          |
| ---------- | ------------------------------------------------ |
| 🐍 Python  | Programming language                             |
| 🐼 Pandas  | Data loading, manipulation and cleaning          |
| 🔢 NumPy   | Numerical operations and conditional replacement |
| 📄 CSV     | Dataset storage                                  |

---

## 📂 Dataset

The project uses an **Indian Employee Dataset** containing employee-related information.

The dataset includes **8 columns**, covering employee information such as:

* Employee ID
* Employee Name
* Age
* Salary (INR)
* Experience
* City
* Department
* Performance Rating

---

## 📊 Dataset Information

### Before Cleaning

* **Rows:** 1,005
* **Columns:** 8

### After Cleaning

* **Rows:** 997
* **Columns:** 8

The reduction in records occurs because duplicate records and salary outliers are removed during preprocessing.

---

# 🧹 Data Cleaning Workflow

## 1️⃣ Load the Dataset

The dataset is loaded using Pandas:

```python
df = pd.read_csv("data/indian_employee_data.csv")
```

The first five records are displayed using:

```python
print(df.head())
```

---

## 2️⃣ Check Missing Values

Missing values are identified using:

```python
df.isnull().sum()
```

This helps determine which columns require data preprocessing.

The raw dataset contains missing values in:

| Column             | Missing Values |
| ------------------ | -------------: |
| Age                |             10 |
| Salary (INR)       |             27 |
| Performance Rating |             16 |

---

## 3️⃣ Handle Infinite Values

Infinite values can cause problems during numerical calculations.

Therefore, positive and negative infinity are converted into `NaN`:

```python
df.replace([np.inf, -np.inf], np.nan, inplace=True)
```

These values can then be handled using the missing-value treatment.

---

## 4️⃣ Remove Duplicate Records

Duplicate records are removed using:

```python
df.drop_duplicates(inplace=True)
```

The raw dataset contains:

**5 duplicate rows**

After cleaning:

**0 duplicate rows**

---

## 5️⃣ Handle Negative Salary Values

Negative salaries are considered invalid for this dataset.

First, the mean salary is calculated using only valid non-negative salary values:

```python
salary_mean = df.loc[
    df["Salary (INR)"] >= 0,
    "Salary (INR)"
].mean()
```

NumPy's `where()` function is then used to replace negative salaries:

```python
df["Salary (INR)"] = np.where(
    df["Salary (INR)"] < 0,
    salary_mean,
    df["Salary (INR)"]
)
```

The raw dataset contains:

**11 negative salary values**

After cleaning:

**0 negative salary values**

---

## 6️⃣ Handle Missing Salary Values

Missing salary values are replaced with the mean salary:

```python
df["Salary (INR)"].fillna(
    df["Salary (INR)"].mean(),
    inplace=True
)
```

This prevents missing salary values from affecting future analysis.

---

## 7️⃣ Handle Missing Performance Ratings

Missing performance ratings are replaced using the median:

```python
df["Performance Rating"].fillna(
    df["Performance Rating"].median(),
    inplace=True
)
```

### Why Median?

The median is less affected by extreme values compared with the mean, making it a useful choice for rating data.

---

## 8️⃣ Fill Remaining Numerical Missing Values

Any remaining numerical missing values are filled using the mean of their respective numerical columns:

```python
df.fillna(
    df.mean(numeric_only=True),
    inplace=True
)
```

This ensures that numerical columns do not contain missing values after preprocessing.

---

# 📈 9️⃣ Salary Outlier Detection

Extreme salary values are detected using the **3-Sigma Rule**.

The method uses the mean and standard deviation of the salary column.

### Formula

```text
Lower Bound = Mean - (3 × Standard Deviation)

Upper Bound = Mean + (3 × Standard Deviation)
```

In Python:

```python
salary_mean = df["Salary (INR)"].mean()
salary_std = df["Salary (INR)"].std()

lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)
```

The dataset is then filtered:

```python
df = df[
    (df["Salary (INR)"] >= lower_bound) &
    (df["Salary (INR)"] <= upper_bound)
]
```

This removes salary observations that fall outside the calculated 3-Sigma range.

> **Note:** An outlier is not necessarily an incorrect record. In this project, extreme salary values are treated as outliers according to the selected 3-Sigma preprocessing method.

---

# ✅ 10️⃣ Final Data Quality Check

After cleaning, the project performs several validation checks.

### Missing Values

```python
df.isnull().sum()
```

### Duplicate Records

```python
df.duplicated().sum()
```

### Negative Salaries

```python
(df["Salary (INR)"] < 0).sum()
```

These checks confirm whether the main cleaning operations were successful.

---

# 📊 Before vs After

| Data Quality Check         | Before Cleaning | After Cleaning |
| -------------------------- | --------------: | -------------: |
| Total Rows                 |           1,005 |            997 |
| Total Columns              |               8 |              8 |
| Missing Age                |              10 |              0 |
| Missing Salary             |              27 |              0 |
| Missing Performance Rating |              16 |              0 |
| Duplicate Rows             |               5 |              0 |
| Negative Salaries          |              11 |              0 |
| Infinite Values            |              23 |              0 |

---

# 📁 Project Structure

```text
employee-data-cleaning-pandas-numpy/
│
├── data/
│   ├── indian_employee_data.csv
│   └── cleaned_indian_employee_data.csv
│
├── data_cleaning.py
│
├── README.md
│
└── requirements.txt
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/employee-data-cleaning-pandas-numpy.git
```

## 2. Navigate to the Project

```bash
cd employee-data-cleaning-pandas-numpy
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

The project requires:

```text
numpy
pandas
```

You can install them using:

```bash
pip install numpy pandas
```

---

# ▶️ How to Run

Run the data-cleaning script:

```bash
python data_cleaning.py
```

The script will:

1. Load the raw dataset.
2. Display the initial data.
3. Check missing values.
4. Replace infinite values.
5. Remove duplicates.
6. Fix negative salary values.
7. Handle missing values.
8. Detect salary outliers.
9. Perform final validation.
10. Save the cleaned dataset.

The final dataset will be saved as:

```text
data/cleaned_indian_employee_data.csv
```

---

# 🧠 Concepts Demonstrated

This project demonstrates practical knowledge of:

### Pandas

* `pd.read_csv()`
* `DataFrame.head()`
* `isnull()`
* `fillna()`
* `drop_duplicates()`
* Boolean filtering
* `select_dtypes()`
* `to_csv()`

### NumPy

* `np.inf`
* `np.nan`
* `np.where()`

### Data Cleaning

* Missing-value handling
* Duplicate removal
* Invalid-value handling
* Numerical imputation
* Outlier detection
* Statistical preprocessing
* Data validation

---

# 🎓 Learning Outcomes

After completing this project, I gained practical experience in:

* Working with real-world-style tabular data
* Identifying common data-quality problems
* Cleaning datasets using Pandas
* Performing numerical operations using NumPy
* Handling missing and invalid data
* Detecting statistical outliers
* Applying the 3-Sigma Rule
* Creating reproducible data-cleaning workflows
* Exporting cleaned datasets for further analysis

---

# 🚀 Future Improvements

The project can be extended with:

### 📊 Exploratory Data Analysis

* Salary distribution
* Department-wise salary analysis
* City-wise employee analysis
* Experience vs salary
* Performance rating analysis

### 📈 Visualization

Possible libraries:

* Matplotlib
* Seaborn

### 🤖 Machine Learning

The cleaned dataset could later be used for:

* Salary prediction
* Employee performance prediction
* Employee segmentation
* Salary classification

### 📊 Dashboard

A future version could include an interactive dashboard using:

* Streamlit
* Power BI

---

# 🔮 Future Project Pipeline

```text
Raw Employee Dataset
        ↓
Data Inspection
        ↓
Missing Value Detection
        ↓
Infinite Value Handling
        ↓
Duplicate Removal
        ↓
Invalid Salary Handling
        ↓
Missing Value Imputation
        ↓
Outlier Detection
        ↓
Data Validation
        ↓
Clean Dataset
        ↓
EDA / Visualization
        ↓
Machine Learning
```

---

# 👨‍💻 Author

## Shubham Londhe

**B.Tech Computer Science Engineering — Artificial Intelligence & Machine Learning**

Interested in:

* Artificial Intelligence
* Machine Learning
* Python
* Data Science
* Data Analysis

---

# ⭐ Conclusion

This project demonstrates a complete beginner-level **data cleaning workflow using Pandas and NumPy**.

The raw Indian employee dataset contained several data-quality issues, including missing values, duplicate records, infinite values, negative salaries, and extreme salary observations.

After preprocessing, the dataset contains **997 rows and 8 columns** and is ready for further analysis.

This project serves as a foundation for the next stages of the data science workflow:

**Data Cleaning → EDA → Visualization → Machine Learning**

---

## ⭐ If you found this project useful

Give this repository a ⭐ on GitHub!
