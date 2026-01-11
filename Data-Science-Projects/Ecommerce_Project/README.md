# 📊 E-Commerce Customer Spending Predictor

A Machine Learning application designed to predict the yearly amount spent by e-commerce customers based on their digital behavior patterns. This tool helps businesses make data-driven decisions by analyzing user engagement on mobile apps and websites.

## 🚀 Live Demo
**[Click here to try the App]** *(Add your Hugging Face Space link here later)*

## 🧐 About the Project
This project leverages **Linear Regression** to analyze customer data and predict future spending. It takes into account various factors such as session length, time spent on the application, and length of membership.

The model was trained on an E-commerce dataset, achieving high accuracy in understanding the correlation between user activity and revenue.

## ⚙️ Key Features
* **Real-time Prediction:** Get instant results based on user input.
* **User-Friendly Interface:** Built with **Gradio** for an interactive experience.
* **Data Validation:** Automatically handles input errors and converts numerals.
* **Clean Architecture:** Separated model training (Jupyter) from the deployment logic (Python Script).

## 🛠️ Technologies Used
* **Python 3.x**
* **Scikit-Learn** (Model Building)
* **Pandas & NumPy** (Data Analysis)
* **Gradio** (Web Interface & Deployment)
* **Joblib** (Model Serialization)

## 💻 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Loai-Alrazi/Python.git](https://github.com/Loai-Alrazi/Python.git)
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    python app.py
    ```

## 📂 Project Structure
* `ecommerce_customers.ipynb`: The notebook containing data analysis, visualization, and model training.
* `app.py`: The main script for the Gradio web application.
* `linear_regression_model.pkl`: The pre-trained machine learning model.
* `requirements.txt`: List of required Python libraries.

## 👤 Author
**Loay Alrazi** - Data Scientist & IT Specialist
[GitHub Profile](https://github.com/Loai-Alrazi)