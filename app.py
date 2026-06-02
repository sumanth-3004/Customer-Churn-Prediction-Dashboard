import streamlit as st
import pandas as pd
import joblib

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# LOAD FILES
# ==========================================
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")
encoders = joblib.load("encoders.pkl")

# ==========================================
# TITLE
# ==========================================
st.title("📊 Customer Churn Prediction Dashboard")
st.markdown("Predict whether a customer is likely to churn.")

# ==========================================
# INPUT FORM
# ==========================================
col1, col2, col3 = st.columns(3)

with col1:
    customer_id = st.number_input("Customer ID", min_value=1, value=1001)
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    income = st.number_input("Income", min_value=0.0, value=50000.0)
    spending_score = st.slider("Spending Score", 0, 100, 50)
    purchase_amount = st.number_input("Purchase Amount", min_value=0.0, value=1000.0)
    session_time = st.number_input("Session Time", min_value=0.0, value=15.0)

with col2:
    gender = st.selectbox(
        "Gender",
        list(encoders["Gender"].classes_)
    )

    product_category = st.selectbox(
        "Product Category",
        list(encoders["ProductCategory"].classes_)
    )

    payment_method = st.selectbox(
        "Payment Method",
        list(encoders["PaymentMethod"].classes_)
    )

    city = st.selectbox(
        "City",
        list(encoders["City"].classes_)
    )

    state = st.selectbox(
        "State",
        list(encoders["State"].classes_)
    )

    country = st.selectbox(
        "Country",
        list(encoders["Country"].classes_)
    )

with col3:
    last_purchase = st.selectbox(
        "Last Purchase Date",
        list(encoders["LastPurchaseDate"].classes_)
    )

    is_active = st.selectbox(
        "Is Active",
        list(encoders["IsActive"].classes_)
    )

    discount_used = st.selectbox(
        "Discount Used",
        list(encoders["DiscountUsed"].classes_)
    )

    browser = st.selectbox(
        "Browser",
        list(encoders["Browser"].classes_)
    )

    device = st.selectbox(
        "Device",
        list(encoders["Device"].classes_)
    )

    returns = st.number_input(
        "Returns",
        min_value=0,
        value=0
    )

    review_score = st.slider(
        "Review Score",
        1,
        5,
        3
    )

# ==========================================
# PREDICTION
# ==========================================
if st.button("🔍 Predict Churn", use_container_width=True):

    gender = encoders["Gender"].transform([gender])[0]
    product_category = encoders["ProductCategory"].transform([product_category])[0]
    payment_method = encoders["PaymentMethod"].transform([payment_method])[0]
    city = encoders["City"].transform([city])[0]
    state = encoders["State"].transform([state])[0]
    country = encoders["Country"].transform([country])[0]
    last_purchase = encoders["LastPurchaseDate"].transform([last_purchase])[0]
    is_active = encoders["IsActive"].transform([is_active])[0]
    discount_used = encoders["DiscountUsed"].transform([discount_used])[0]
    browser = encoders["Browser"].transform([browser])[0]
    device = encoders["Device"].transform([device])[0]

    data = pd.DataFrame(
        [[
            customer_id,
            age,
            gender,
            income,
            spending_score,
            purchase_amount,
            product_category,
            payment_method,
            city,
            state,
            country,
            last_purchase,
            is_active,
            returns,
            discount_used,
            review_score,
            browser,
            device,
            session_time
        ]],
        columns=scaler.feature_names_in_
    )

    scaled_data = scaler.transform(data)

    prediction = model.predict(scaled_data)[0]
    probability = model.predict_proba(scaled_data)[0][1]

    st.divider()

    st.metric(
        "Churn Probability",
        f"{probability:.2%}"
    )

    if prediction == 1:
        st.error("⚠️ Customer is likely to churn.")
    else:
        st.success("✅ Customer is likely to stay.")