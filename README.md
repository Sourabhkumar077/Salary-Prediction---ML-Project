
# Salary Prediction Using Machine Learning

This project aims to predict an individual's salary based on their years of professional experience using a simple yet effective machine learning model — **Simple Linear Regression**.

It was developed as a **Minor Project** in partial fulfillment of the B.Tech degree in Computer Science & Engineering at **Bansal College of Engineering, Mandideep**, affiliated to **RGPV Bhopal**.

---

## 🔍 Problem Statement

Can we accurately predict an individual's salary based on their years of experience using machine learning?

The answer involves:
- Cleaning and preprocessing a real-world dataset
- Visualizing key relationships
- Training a regression model
- Evaluating model performance

---

## 💻 Tools & Technologies Used

- **Language:** Python
- **Platform:** Jupyter Notebook
- **Libraries:**
  - `pandas` – data manipulation
  - `numpy` – numerical operations
  - `matplotlib` & `seaborn` – visualizations
  - `scikit-learn` – machine learning

---

## 📊 Dataset Description

- File: `Salary_Data.csv`
- Features:
  - `YearsExperience` – Independent variable (X)
  - `Salary` – Dependent variable (Y)
- Rows: 30 real-world samples
- Source: Public ML dataset repositories (e.g., Kaggle)

---

## 🔧 Methodology

1. **Data Cleaning:**
   - Removed duplicates, handled missing values
   - Verified data types

2. **Data Visualization:**
   - Heatmaps and scatter plots to understand trends

3. **Model Building:**
   - Used `Simple Linear Regression`
   - Train-test split: 80/20

4. **Model Evaluation:**
   - MSE, RMSE, R² score

---

## 📈 Results

- **R² Score** close to 1.0
- Strong linear relationship between experience and salary
- Final scatter plot confirmed a well-fitting regression line

---

## 📉 Limitations

- Only one feature used (`YearsExperience`)
- Dataset is small (30 records)
- Assumes linear relationship
- No cross-validation used

---

## 🚀 Future Enhancements

- Add more features: Education, Role, Location, etc.
- Use advanced models: Decision Trees, Random Forest
- Deploy model via Flask or Streamlit web app
- Apply cross-validation techniques
- Integrate real-time salary data from APIs
- Add model explainability using SHAP

---

## 👨‍💻 Contributors

- **Pankaj Nishad** – Model training & future enhancements  
- **Piyush Kumar Sarathe** – Dataset exploration & testing  
- **Rachna Upadhyay** – Literature review & documentation  
- **Shubham Chourasiya** – Preprocessing & regression implementation  
- **Sourabh Kumar Mahuvar** – Visualization & evaluation metrics

---

## 📁 Project Structure

```
├── .idea/                         # IDE settings
├── venv/                          # Python virtual environment
├── main.py                        # Main ML script
├── Preprocessing_&_Visualization_Annotated.ipynb  # Jupyter notebook
├── Salary_Data.csv                # Dataset
├── salary_model.pkl               # Trained model
├── requirements.txt               # Dependencies
├── README.md                      # Project documentation
├── .gitignore                     # Files to ignore in Git
```

---

## 📜 License

This project is for **educational use only**.
