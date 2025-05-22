# Salary Prediction Project

This project aims to predict salaries based on historical data using machine learning. It includes data preprocessing, visualization, model training, and prediction, implemented in Python.

## Project Structure

```
├── .idea/                             # IDE configuration files (ignored by Git)
├── venv/                              # Python virtual environment (ignored by Git)
├── .gitignore                         # Specifies intentionally untracked files to ignore
├── main.py                            # Main script for model training or inference
├── Preprocessing_&_Visualization_Annotated.ipynb  # Jupyter notebook with data preprocessing and visualization
├── Salary_Data.csv                    # Dataset containing salary data
├── salary_model.pkl                   # Trained machine learning model (Pickle file)
├── requirements.txt                   # Project dependencies
```

## How to Run

1. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script**

   ```bash
   python main.py
   ```

## Notes

- The notebook provides detailed steps for data exploration and model building.
- The `.pkl` file contains the trained model.
- The `.csv` file is the dataset used for training and testing.
- All IDE-specific and environment folders are excluded via `.gitignore`.

## License

This project is for educational purposes.