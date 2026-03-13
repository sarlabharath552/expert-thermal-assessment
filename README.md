# Expert Thermal – Founding Engineer Intern Assessment
Candidate: Sarla Bharath Chandra  
Role: Python | AI/ML | Web Development

---

# Question 1 – Python Thermal Model + Flask API

## Objective
Develop a Python thermal model based on the provided thermal resistance network and validate the results against the reference spreadsheet.

According to the thermal reference document, the total thermal resistance is:

R_total = R_jc + R_TIM + R_hs

Where:

R_hs = R_cond + R_conv

Junction temperature is calculated using:

Tj = Ta + Q * R_total

Reference spreadsheet result:

Heat Sink Resistance ≈ 0.373 °C/W  
Junction Temperature ≈ 80.96 °C

---

## Python Implementation

thermal_model.py implements the following steps:

1. Calculate TIM resistance
2. Calculate base conduction resistance
3. Compute Reynolds number
4. Compute Nusselt number
5. Compute convection heat transfer coefficient
6. Compute convection resistance
7. Compute heat sink resistance
8. Compute junction temperature

---

## Output

Example output:

Heat Sink Resistance ≈ 0.359 
Total Thermal Resistance ≈ 0.47  
Junction Temperature ≈ 95.44 °C

---

## Flask API

A Flask API was implemented to expose the thermal model.

Endpoint:

GET /thermal

Example JSON response:

{
  "heat_sink_resistance": 0.3590123078510198,
  "junction_temperature": 95.43881189919338,
  "total_thermal_resistance": 0.4695920793279559
}

---

## Screenshots

### Python Model Output
![Python Output](screenshots/python_output.png)

### Flask API Output
![Flask API](screenshots/flask_api_output.png)

---

# Question 2 – Physics Informed Neural Networks (PINN)

Physics Informed Neural Networks combine neural networks with physical laws such as PDEs.

Instead of relying only on data, the model learns solutions while satisfying governing physics equations.

For this thermal problem, a PINN could be formulated as follows:

Inputs
- Geometry parameters
- Air velocity
- Material properties

Outputs
- Temperature distribution
- Heat sink thermal resistance

Loss Function
- PDE residual loss
- Boundary condition loss
- Data loss (if simulation/experimental data exists)

Libraries that could be used:

- PyTorch
- TensorFlow
- DeepXDE

PINNs are particularly useful for solving heat transfer problems because they can approximate solutions to heat diffusion equations while respecting boundary conditions.

---

# Question 3 – Vertex AI

Google Vertex AI is a unified ML platform that allows developers to:

- Train machine learning models
- Deploy scalable inference APIs
- Build generative AI applications

In the context of engineering tools, Vertex AI could be used to build:

- AI-assisted thermal design tools
- Heat sink optimization systems
- Engineering copilots for design validation

For example, a thermal design assistant could take heat sink geometry as input and predict cooling performance using a trained ML model deployed through Vertex AI.

---

# Question 4 – Motivation

I am interested in joining Expert Thermal because it combines engineering physics, AI, and software engineering.

I am particularly interested in building intelligent engineering tools that help automate complex design workflows. The opportunity to work in a startup environment where I can take ownership of the product and contribute directly to building real-world solutions is very exciting.

I am especially motivated by problems that combine:

- Physics
- Machine learning
- Backend engineering

This internship would allow me to apply my programming and problem-solving skills while learning how advanced AI tools can be applied to engineering simulations.

---

# Question 5 – Web Development Ownership

I have experience building backend systems using Java and REST APIs. My experience includes:

- Spring Boot backend development
- REST API design
- SQL database integration
- Git and GitHub for version control

Although my primary experience is in Java-based backend systems, I am comfortable learning new technologies quickly. I am confident I can take ownership of a Node.js / React.js web application by:

1. Understanding the project architecture
2. Reading the codebase
3. Debugging issues
4. Implementing new features

As the sole developer during the internship, I would focus on maintaining code quality, documenting changes, and delivering features quickly in a startup environment.

---

# GitHub Repository

This repository contains:

- Python thermal model
- Flask API implementation
- Screenshots of validated results
- Written answers to the assessment questions

---
