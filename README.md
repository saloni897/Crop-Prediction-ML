🌾 Crop Recommendation System using Machine Learning
📌 About the Project

This is a Machine Learning-based project where I have developed a Crop Recommendation System that suggests the most suitable crop based on soil nutrients and environmental conditions.

In this project, I also created a simple user interface using Gradio, where users can enter values and get instant predictions along with crop images.

🎯 Objective

The main objective of this project is to:

Help farmers select the best crop
Use data-driven decision making
Reduce crop failure chances
⚙️ Technologies Used
Python
Pandas, NumPy
Matplotlib, Seaborn (for visualization)
Scikit-learn
Gradio (for UI)
📊 Dataset

The dataset contains agricultural parameters like:

Nitrogen (N)
Phosphorus (P)
Potassium (K)
Temperature
Humidity
pH value
Rainfall

These features are used to train the model and predict crops.

🤖 Machine Learning Model

I have used Logistic Regression algorithm to train the model.

Data is split into training and testing sets
Model is trained using train_test_split
Accuracy is calculated using sklearn metrics
Classification report is also generated
📈 Data Visualization

Before training, I performed data analysis using:

Histograms
Feature distribution plots

This helped in understanding the dataset better.

🧠 How the System Works
Load dataset
Visualize and understand data
Train Logistic Regression model
Take user input through Gradio sliders
Predict crop based on input values
Display crop name and image
💻 User Interface (Gradio)
User enters values using sliders:
N, P, K
Temperature
Humidity
pH
Rainfall
Output:
Predicted crop name
Crop image
🚀 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/saloni897/Crop-Prediction-ML.git
cd Crop-Prediction-ML
2️⃣ Install Requirements
pip install pandas numpy matplotlib seaborn scikit-learn gradio
3️⃣ Run the App
python app.py
4️⃣ Open in Browser

Gradio will generate a link → open it to use the app.

📁 Project Structure
Crop-Prediction-ML/
│── app.py
│── Crop_recommendation.csv
│── images/
│── README.md
📌 Key Features
Simple and interactive UI
Real-time crop prediction
Visualization of dataset
Shows crop image with result
🌱 Future Improvements
Use advanced models like Random Forest
Add real-time weather API
Deploy as web application
Improve UI design
