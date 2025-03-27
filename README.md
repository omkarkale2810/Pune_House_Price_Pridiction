Pune Home Price Prediction
Project Overview
This web application predicts home prices in Pune based on various input parameters such as total square footage, number of bedrooms (BHK), number of bathrooms, and location.
Features

Predict home prices for different property configurations
Dynamic location selection
Server-side rendering
User-friendly interface
Error handling and input validation

Technology Stack

Backend: Python Flask
Frontend: HTML, CSS
Machine Learning: implemented in util.py, main.ipynb

Prerequisites

Python 3.7+
pip (Python package manager)

Installation

Clone the repository:

git clone https://github.com/omkarkale2810/Pune_House_Price_Pridiction.git
cd Pune_House_Price_Pridiction

How to Use

Enter the total square footage of the property
Select the number of bedrooms (BHK)
Choose the number of bathrooms
Select the location from the dropdown
Click "Estimate Price" to get the predicted home price in Lakhs

Model Training

Collect historical home price data
Preprocess and clean the data
Split the data into training and testing sets
Train a regression model using Linear Regression model
Save the trained model for predictions

Customization

To add more locations, update the get_location_names() method in util.py
Modify the machine learning model in util.py to improve prediction accuracy

Error Handling
The application includes basic error handling:

Validates input parameters
Provides user-friendly error messages
Handles exceptions during price prediction

Contributing

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

License
Distributed under the MIT License. See LICENSE for more information.
Contact
Your Name - omkarkale7888@gmail.com
Project Link: https://github.com/omkarkale2810/Pune_House_Price_Pridiction.git

Last edited 2 minutes ago
