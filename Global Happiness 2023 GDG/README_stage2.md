# Stage 2: Machine Learning Prediction – Global Happiness Report (2023)

## 📌 Overview

In this stage, we built and evaluated machine learning models to **predict the Happiness Score** for countries based on the 2023 World Happiness Report dataset.

The target variable was **`happiness_score`**, while features included economic, social, and health indicators.

---

## 🛠️ Steps Taken

1. **Data Preprocessing**

   * Focused only on the **2023 dataset**.
   * Renamed columns for consistency (e.g., `healthy_life_expectancy`, `freedom_to_make_life_choices`).
   * Applied **One-Hot Encoding** for categorical feature: `region`.

2. **Model Training**

   * Split the dataset into **80% training** and **20% testing**, Mainly givig 30 sample for test.
   * Trained two models:

     * **Linear Regression**
     * **Random Forest Regressor**

3. **Model Evaluation**

   * Metrics: **R² Score, RMSE, MSE**

---

## 📊 Results

| Model             | R² Score | RMSE  | MSE   |
| ----------------- | -------- | ----- | ----- |
| Linear Regression | 0.796    | 0.524 | 0.275 |
| Random Forest     | 0.799    | 0.521 | 0.272 |

🔎 **Observation:**

* Random Forest performed slightly better than Linear Regression.
* **Random Forest** was chosen as the final model.

---

## 💾 Deliverables

* **`final_model.pkl`** → Trained Random Forest model.
* **`columns.pkl`** → Saved feature columns for preprocessing.
* **Notebook** → Contains training, evaluation, and model saving steps.

---

## 🚀 Next Stage

The best model (`Random Forest`) will be used to power an **interactive Streamlit app** (Stage 3).
