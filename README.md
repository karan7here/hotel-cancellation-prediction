# 🏨 Hotel Reservation Cancellation Prediction System

## 📌 Project Overview

The Hotel Reservation Cancellation Prediction System is a Machine Learning web application developed using Python and Streamlit.  

This project predicts whether a hotel reservation is likely to be cancelled based on customer booking details and reservation history.

The goal of this project is to help hotels improve revenue management, optimize room allocation, and reduce losses caused by booking cancellations.

---

# 🚀 Live Demo

Add your Streamlit deployment link here after deployment.

```text
https://your-app-name.streamlit.app
```

---

# 📷 Project Screenshot

Add screenshots here after deployment.

Example:

```md
![App Screenshot](screenshot.png)
```

---

# 🎯 Problem Statement

Hotel cancellations create major challenges for hotels, including:

- Revenue loss
- Inefficient room allocation
- Poor customer management
- Overbooking issues
- Resource wastage

This project uses Machine Learning to predict cancellation behavior in advance.

---

# 🧠 Machine Learning Workflow

The project follows a complete end-to-end Machine Learning pipeline:

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Data Preprocessing
6. Model Building
7. Model Evaluation
8. Hyperparameter Tuning
9. Model Saving
10. Streamlit Deployment

---

# 📊 Dataset Information

The dataset contains hotel reservation information such as:

| Feature | Description |
|---|---|
| no_of_adults | Number of adults |
| no_of_children | Number of children |
| no_of_weekend_nights | Weekend stay nights |
| no_of_week_nights | Weekday stay nights |
| type_of_meal_plan | Meal plan selected |
| required_car_parking_space | Parking requirement |
| room_type_reserved | Room category |
| lead_time | Days before booking |
| arrival_month | Arrival month |
| repeated_guest | Returning customer |
| avg_price_per_room | Average room price |
| no_of_special_requests | Special requests |
| booking_status | Target variable |

---

# ⚙️ Feature Engineering

Additional features created:

- total_guests
- total_nights

These engineered features improved model performance.

---

# 🤖 Machine Learning Models Used

The following algorithms were tested:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors

Final Selected Model:

✅ Random Forest Classifier

---

# 📈 Model Performance

| Metric | Score |
|---|---|
| Accuracy | 89%+ |
| Precision | High |
| Recall | High |
| F1 Score | Good |

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Libraries

- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit

---

# 💻 Streamlit Web Application Features

✅ Interactive User Interface  
✅ Real-time Prediction  
✅ Sidebar Input Controls  
✅ Machine Learning Prediction  
✅ Probability Display  
✅ Clean Dashboard Design  
✅ Responsive Layout  

---

# 📂 Project Structure

```text
Hotel_Project/
│
├── app.py
├── requirements.txt
├── README.md
├── hotel_reservation_model.pkl
├── scaler.pkl
├── Hotel Reservations.csv
├── Hotel_prediction_final_capstone.ipynb
```

---

# ▶️ How to Run Project Locally

## Step 1 — Clone Repository

```bash
git clone https://github.com/yourusername/hotel-cancellation-prediction.git
```

---

## Step 2 — Open Project Folder

```bash
cd hotel-cancellation-prediction
```

---

## Step 3 — Install Requirements

```bash
pip install -r requirements.txt
```

---

## Step 4 — Run Streamlit App

```bash
streamlit run app.py
```

---

# 🌐 Streamlit Deployment

This project is deployed using:

:contentReference[oaicite:0]{index=0}

---

# 📊 Exploratory Data Analysis (EDA)

EDA techniques used:

- Countplots
- Heatmaps
- Correlation Analysis
- Distribution Plots
- Outlier Detection
- Feature Relationships

---

# 🔍 Key Insights

- Higher lead time increases cancellation probability.
- Repeated guests are less likely to cancel.
- More special requests reduce cancellation chances.
- Online bookings have higher cancellation rates.
- Pricing impacts cancellation behavior.

---

# 📌 Future Improvements

Future enhancements planned:

- User Authentication
- Database Integration
- PDF Report Generation
- Advanced Dashboard Analytics
- API Deployment
- Docker Containerization
- Cloud Deployment on AWS
- Real-time Booking System

---

# 🎓 Learning Outcomes

Through this project I learned:

- End-to-End Machine Learning
- Data Preprocessing
- Feature Engineering
- Model Evaluation
- Hyperparameter Tuning
- Streamlit Deployment
- GitHub Project Management

---

# 📄 Requirements

Create a file named:

```text
requirements.txt
```

Add:

```text
streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
```

---

# 👩‍💻 Author

## Sneha Singh

Aspiring Data Analyst & Machine Learning Enthusiast

### Skills

- Python
- SQL
- Excel
- Power BI
- Machine Learning
- Streamlit

---

# 📬 Contact

Add your links here:

- LinkedIn
- GitHub
- Portfolio

Example:

```md
[LinkedIn](https://linkedin.com/in/yourprofile)
```

---

# ⭐ GitHub Support

If you liked this project:

⭐ Star this repository  
🍴 Fork this repository  
📢 Share with others  

---

# 📜 License

This project is for educational and learning purposes.

---

# 🙌 Acknowledgements

Special thanks to:

- Streamlit
- Scikit-learn
- Open-source community
- Dataset providers

---

# 📢 Conclusion

This project demonstrates a complete real-world Machine Learning workflow from data preprocessing to model deployment using Streamlit.

The system helps predict hotel reservation cancellations effectively and provides valuable business insights for the hospitality industry.
