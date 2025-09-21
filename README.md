# 🌍 Global Happiness 2023 – GDG Bowen Submission  

This project is part of my submission for the **Data & ML Lead role** in the Google Developer Group on Campus (GDG) at Bowen University.  

The analysis focuses **only on the 2023 Global Happiness dataset**, following the assignment requirements.  

---

## 📂 Project Files  

- `Global_happiness_2023_GDG.ipynb` → Main notebook with data cleaning, EDA, model building, and evaluation.  
- `final_model.pkl` → Saved Random Forest model trained on the 2023 dataset.  
- `training_columns.pkl` → Columns used during model training.  
- `streamlit_app.py` → Minimal Streamlit web app for interactive predictions.  

---

## 🚀 Quick Start  

1. Clone this repository:  

   git clone https://github.com/<your-username>/global-happiness-2023.git
   cd global-happiness-2023

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

---

## 📊 Model Used

* **Random Forest Regressor**

  * Best performing model on the 2023 dataset.
  * Metrics (on test data):

    * R² Score: \~0.80
    * RMSE: \~0.52

---

## 🔗 Stage 2 Documentation

For detailed methodology, reasoning, and explanation of the steps taken in **Stage 2**, please see the [Stage 2 README](../Stage2/README.md).

---

## 🙋 About

Author: **Adedokun Marvellous**
Role applied: **Data & ML Lead – GDG on Campus (Bowen University)**
Year: **2023 Dataset Submission**
