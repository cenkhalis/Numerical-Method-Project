# Numerical Methods: Interpolation Project

Implement and compare four interpolation methods: **Newton, Lagrange, Cubic Spline, and B-Spline**. Use provided Python templates, analyze their performance, compare the methods and summarize findings clearly in your report.

---

## Installation

Python 3.7+ is required. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Workflow and Project UI

Use the provided `project_runner.py` script for an interactive experience:

- **Main Menu:** Select tasks such as testing implementations, choosing waypoints, running experiments, visualizing methods, or generating report data.
- **Testing:** Quickly validate the correctness of your implementations.
- **Visualization:** Interactively visualize and compare interpolation methods.

To launch the interface, run:
```bash
python project_runner.py
```

---

## Your Tasks
Complete each interpolation method clearly marked by:

```python
# STUDENT IMPLEMENTATION START
# STUDENT IMPLEMENTATION END
```

---

## Experiments

Conduct and analyze the following experiments using the interactive UI:

- **Accuracy vs. Smoothness:** Balance between accurately following waypoints and maintaining a smooth path.
- **Local Control:** Observe how altering a waypoint influences the entire path.
- **Waypoint Density Analysis:** Compare methods' performances with varying waypoint densities.

---

## Report Guidelines

**Check the project PDF file for additional instructions**

Clearly address:

1. **Methods:** Mathematical explanation (brief).
2. **Analysis:** Accuracy, smoothness, local control, waypoint density.
3. **Implementation:** Challenges and key decisions.
4. **Conclusions:** Optimal methods for various scenarios.

---

## Resources
- **B-Spline:**
  - [Path Smoothing Techniques in Robot Navigation: State-of-the-Art, Current and Future Challenges](https://www.mdpi.com/1424-8220/18/9/3170)
- **Newton's Polynomial Interpolation:**
  - [Newton Polynomial - Wikipedia](https://en.wikipedia.org/wiki/Newton_polynomial)
- **Lagrange Polynomial Interpolation:**
  - [Lagrange Interpolating Polynomial - Wolfram MathWorld](https://mathworld.wolfram.com/LagrangeInterpolatingPolynomial.html)
- **Cubic Spline Interpolation:**
  - [Spline Method of Interpolation - Mathematics LibreTexts](https://math.libretexts.org/Workbench/Numerical_Methods_with_Applications_(Kaw)/5:_Interpolation/5.05:_Spline_Method_of_Interpolation)

---

## Assessment
- Implementation correctness (40%)
- Comparative analysis (30%)
- Visualization clarity (10%)
- Report quality (20%)

Good luck!