# Customer-Churn-Prediction-Dashboard
6.1 Introduction
The Customer Churn Prediction System is a machine learning-based application designed to predict whether a customer is likely to leave a service or not. This project uses classification algorithms to analyze customer data and identify patterns that indicate churn behavior.The system is built using the Random Forest Classifier, a powerful ensemble learning algorithm known for its accuracy and robustness. The model processes historical customer data and predicts churn based on various features.This project is highly useful in industries such as telecom, banking, and e-commerce, where retaining customers is critical for business growth.
6.2 Problem statement
Customer churn is a major challenge for businesses, as losing customers directly impacts revenue and growth. Identifying customers who are likely to churn in advance allows companies to take preventive actions.However, manual analysis of customer data is difficult due to large volumes and complex patterns. There is a need for an automated system that can efficiently predict churn with high accuracy.This project aims to build a machine learning model that predicts whether a customer will churn or not using historical data.
6.3 Objectives of the Project
The objectives of this project are:
To develop a customer churn prediction system
To perform data cleaning and preprocessing
To encode categorical data into numerical form
To apply machine learning algorithms for classification
To evaluate model performance using accuracy metrics
To save the trained model for future predictions
Additionally, the project aims to create a scalable solution that can be integrated into real-time business systems.

6.4 System Architecture
The system consists of the following stages:
Input Layer: Customer dataset (CSV file)
Data Preprocessing: Cleaning, handling missing values, encoding
Feature Engineering: Splitting features and target variable
Model Training: Random Forest Classifier
Evaluation Layer: Accuracy calculation
Output Layer: Churn prediction result



6.5 Tools and technologies 
6.5.1 Pandas
Used for data loading and manipulation
Handles missing values and duplicates
Works with structured datasets

6.5.2 NumPy
Supports numerical computations
Used for array operations
Improves performance of data processing

6.5.3 Scikit-learn
Provides machine learning algorithms
Used for:
Train-test splitting
Label encoding
Feature scaling
Model training and evaluation

6.5.4 Joblib
Used to save trained models
Enables reuse without retraining


6.6 Data Understanding
 Dataset Description
 Contains customer-related features
 Includes target variable: Churn (Yes/No or 1/0)
 
 Data Exploration
 Checked for missing values
 Identified categorical and numerical columns
 Observed dataset structure

  Observations
  Presence of missing values
  Categorical features need encoding
  Data requires normalization 








6.7 Data Preprocessing
Steps Involved
1. Removing Duplicates
Duplicate rows are removed to ensure data quality
2. Handling Missing Values
Categorical columns → filled with mode
Numerical columns → filled with mean
3. Encoding Categorical Data
Label Encoding is applied
Converts text data into numerical form
4. Feature and Target Split
Features (X): Input variables
Target (y): Churn column
5. Train-Test Split
Data split into:
Training set (80%)
Testing set (20%)
6. Feature Scaling
StandardScaler is applied
Ensures all features are on the same scale 

6.8 Model Building
Algorithm Used: Random Forest Classifier
Ensemble learning method
Combines multiple decision trees
Improves accuracy and reduces overfitting

Model Design
Input: Scaled feature data
Output: Binary classification (Churn / No Churn)

Why Random Forest?
High accuracy
Handles large datasets
Works well with both categorical and numerical data

6.9 Model Training
Training Process
Model trained using training dataset
Learns patterns from customer data
Key Aspects
Uses multiple decision trees
Aggregates predictions for final output



6.10 Model Evaluation
Metric Used:
Accuracy
Measures correctness of predictions
Formula:
Accuracy = (Correct Predictions / Total Predictions)
Analysis
High accuracy indicates good model performance
Helps evaluate prediction capability

6.11 Model Prediction
Steps
Load new customer data
Apply preprocessing (same as training)
Use trained model to predict
Output
Churn (1) → Customer likely to leave
No Churn (0) → Customer likely to stay

6.12 Model Deployment
Model saved using Joblib
model.pkl → trained model
scaler.pkl → scaling object
Advantages
No need to retrain model
Can be used in web applications
Faster predictions

6.13 Limitations of the System
•	Accuracy depends on dataset quality
•	Cannot handle unseen patterns effectively
•	Requires proper preprocessing for new data
6.14 Future Enhancements
•	Use advanced algorithms like XGBoost
•	Deploy using web frameworks (Flask/Streamlit)
•	Improve feature engineering
•	Add real-time prediction system
•	Use deep learning models for better accuracy






CHAPTER 7

 7.1 CODE
 








 7.2 RESULTS AND DISCUSSION

•	Model successfully predicts customer churn
•	Achieved good accuracy on test data
•	Efficient in handling structured datasets
•	Suitable for business decision-making

   



 		  

					
















        CONCLUSION

The internship at Take It Smart Pvt. Ltd. provided a valuable learning experience in the field of Data Science. It helped me understand the practical aspects of data analysis, machine learning, and the workflow involved in solving real-world data-driven problems. The exposure to industry-relevant concepts improved my overall technical knowledge and analytical thinking.

During the internship, I gained knowledge of core Data Science concepts such as data preprocessing, exploratory data analysis, and machine learning techniques. I also understood the importance of working with structured datasets and extracting meaningful insights from data. Learning about model building and evaluation further strengthened my understanding of predictive analytics and decision-making processes.

The internship also helped me become familiar with development tools such as Git and Visual Studio Code. These tools improved my coding efficiency and introduced me to version control practices. Additionally, it enhanced my problem-solving abilities, logical reasoning, and data interpretation skills in analytical scenarios.
The Customer Churn Prediction project provided valuable insights into machine learning and data preprocessing techniques. It helped in understanding how to handle real-world datasets, clean data, and build predictive models.
Through this project, knowledge of classification algorithms, especially Random Forest, was strengthened. The use of tools like Pandas, NumPy, and Scikit-learn improved practical implementation skills.The project demonstrates how machine learning can be applied to solve real-world business problems such as customer retention. Overall, it enhanced analytical thinking, problem-solving skills, and understanding of predictive modeling.


