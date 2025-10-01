# Numerical Methods: Path Smoothing Project 🚀

This project was developed as part of my Computer Engineering coursework at ITU.  
It implements and compares **four interpolation methods** for robot path planning:

- **Newton Interpolation**
- **Lagrange Interpolation**
- **Cubic Spline**
- **B-Spline**

The goal is to analyze how different numerical methods affect **accuracy, smoothness, and local control** in trajectory generation.  
This project reflects my interest in **algorithmic thinking, problem solving, and building tools that combine theory with practice.**

---

## ✨ Features
- Modular implementation of four interpolation methods (`interpolation/` package).
- Interactive CLI application (`project_runner.py`).
- Experiments to compare methods:
  - Accuracy vs. Smoothness
  - Local Control Properties
  - Waypoint Density Analysis
- Visualization with **Matplotlib**.
- Automated report generation (CSV + plots).
- Metric calculations: **path length, deviation, curvature**.

---

## 🛠️ Tech Stack
- **Python 3.x**
- **NumPy**
- **Matplotlib**
- **termcolor**

---

## ▶️ Usage
```bash
python project_runner.py
