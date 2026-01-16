# Air Quality: Data for Decision Making

## Project Overview
This project simulates a **City Manager's Dilemma**: Can we trust cheap, scalable IoT sensors to make public health decisions (e.g., banning traffic), or do they produce too many false alarms compared to expensive "Ground Truth" analyzers?

We analyze the **Air Quality UCI Dataset** to demonstrate:
1.  **Data Cleaning:** Handling non-standard formats and missing values.
2.  **Sensor Calibration:** Visualizing the drift between cheap sensors and reference equipment.
3.  **Policy Impact:** Quantifying the economic and health costs of relying on raw sensor data.

## Repository Structure
This project simulates a professional data team workflow that uses different modules for each step/functionality, here's the structure:
* `src/loader.py`: **Data Engineering**. Handles parsing errors (`;` separators) and cleans the `-200` missing value trap.
* `src/policy.py`: **Decision Logic**. Defines safety thresholds and calculates False Positives/Negatives.
* `pndikuma_DA_PS1.ipynb`: **The Story**. A notebook for stakeholders to visualize the analysis and decision matrix.

## Dataset Summary
**Source:** UCI Machine Learning Repository (S. De Vito et al., 2008)  
**Context:** One year of hourly data (Mar 2004 - April 2005) from an Italian city at road level.

| Feature Type | Description | Key Variables |
| :--- | :--- | :--- |
| **Ground Truth (GT)** | Certified Analyzer (High Accuracy) | `CO(GT)`, `NOx(GT)`, `C6H6(GT)` |
| **Sensor Data (PT08)** | Metal Oxide Sensors (Low Cost, Noisy) | `PT08.S1` (CO), `PT08.S3` (NOx) |
| **Environmental** | Critical for calibration | `T` (Temp), `RH` (Humidity) |

**Critical Data Note:** Missing values in this dataset are tagged as **`-200`**. The `src/loader.py` handles this.. .


## 📚 References
* *Original Paper:* "On field calibration of an electronic nose for benzene estimation...", S. D. Vito et al., Sensors and Actuators B, 2008.