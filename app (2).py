
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Exponential Rate of Change Model")
st.subheader("Student Interactive Model")

st.markdown("""
**Scenario:**  
A driver starts at an initial speed and the speed changes by a fixed percentage per hour.
This model is for **learning purposes only**, not real-life driving.
""")

# Sidebar inputs
st.sidebar.header("Adjust the Parameters")

initial_speed = st.sidebar.slider("Initial Speed (mph)", 20, 120, 90)
rate_percent = st.sidebar.slider("Rate of Change (%)", -20, 20, 8)
hours = st.sidebar.slider("Time (hours)", 0, 24, 2)

rate = rate_percent / 100

# Exponential model
speed = initial_speed * (1 + rate) ** hours

st.markdown(f"""
### Model Equation
\[
S(t) = {initial_speed}(1 + {rate})^t
\]
""")

st.markdown(f"""
### Result
After **{hours} hours**, the car's speed is approximately:

## 🚗 **{speed:.2f} mph**
""")

# Graph
t = np.linspace(0, hours, 100)
s = initial_speed * (1 + rate) ** t

fig, ax = plt.subplots()
ax.plot(t, s)
ax.set_xlabel("Time (hours)")
ax.set_ylabel("Speed (mph)")
ax.set_title("Speed vs Time (Exponential Model)")

st.pyplot(fig)

st.markdown("""
### Interpretation
- Positive rate → exponential growth  
- Negative rate → exponential decay  
- Small rate changes can cause big differences over time  
""")
