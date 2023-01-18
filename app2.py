import streamlit as st
import numpy as np
from scipy.optimize import minimize

st.title("最適化問題の解析")

st.write("最適化問題は、関数の最大値または最小値を求めることです。")
st.write("以下の関数を最小化します。")

def objective_function(x):
    return x[0]**2 + x[1]**2

st.write(objective_function)

st.write("最適解は、x1 = 0, x2 = 0です。")

initial_guess = np.array([1, 1])

result = minimize(objective_function, initial_guess)

st.write("最適解:")
st.write(result.x)
