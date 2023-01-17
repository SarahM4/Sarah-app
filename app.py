import streamlit as st
import numpy as np
from pyswarms.single.global_best import GlobalBestPSO

st.title("Particle Swarm Optimization Demonstration")

# Define the optimization function
def optimize_func(x):
    return np.sum(x**2)

# Create an instance of the class
optimizer = GlobalBestPSO(n_particles=10, dimensions=2, options=options)

# Perform optimization
best_cost, best_pos = optimizer.optimize(optimize_func, iters=100)

# Plot the results
st.pyplot(optimizer.plot_cost_history)
st.pyplot(optimizer.plot_contour(optimize_func))
