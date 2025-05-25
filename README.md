# GFET Fabrication & Characterization Project

This project documents the fabrication and electrical characterization of a Graphene Field-Effect Transistor (GFET). Emphasis is placed on reproducible analysis, precise documentation, and cross-tool workflows using both Excel and Python. The data and insights here reflect good engineering practice relevant to semiconductor process monitoring and quality control.

The GFET device was fabricated using:

* **Photolithography** for patterning electrodes
* **E-beam PVD** for metal deposition
* **Bubbling transfer** of CVD-grown graphene onto SiO₂/Si substrate

---

## 🎯 Objective

To extract and visualize the **transfer characteristics** (Drain Current vs. Gate Voltage) of a fabricated GFET using both manual (Excel) and automated (Python) workflows.

---

## 📄 Reports

* 📘 [Lab Report (PDF)](Report/Lab_Report_MicroNano.pdf)
* 📊 [Final Presentation (Slides)](Report/LMAN_Presentation_Final.pdf)

---

## 🔬 Microscope Images

### Full Contact View – Device III-25

<img src="Images/GFET_Top_View.jpg" alt="GFET Contact View" width="600"/>
> Contact pads and channel structure after successful lithography and metal lift-off.

### Zoomed-In Graphene Channel

<img src="Images/GFET_Channel_Dimensions.jpg" alt="GFET Channel Dimensions" width="600"/>
> Channel dimensions: **Length = 15 µm**, **Width = 50 µm**. Used in carrier mobility calculation.

---

## 📊 Transfer Characteristics

### Excel Analysis

<img src="Images/IV Curve (Plotted in Excel).png" alt="IV Curve Excel Plot" width="600"/>
> Excel plot showing transfer characteristics of the GFET using converted µA values.

### Python Plot

<img src="Images/gfet_transfer_plot.png" alt="GFET Transfer Characteristics" width="600"/>
> Matplotlib plot generated from `IV_Data_Charted.xlsx` using Python for automation.

---

## 🔧  Engineering Relevance for Process Monitoring and Data Analysis

This project demonstrates:

* 📊 **Data normalization and scientific plotting**
* 🧾 **Documentation alignment with traceability & reproducibility standards**
* 🧪 **Semiconductor test equipment usage (e.g., KEITHLEY 4200)**
* 🛠️ **Microscopy for device structure verification**
* 📁 **Cross-tool workflow integration (Excel + Python)**
* ⚙️ **Use of version control for lab data and analysis artifacts**

---

## 📁 Folder Structure

```
GFET-Fabrication-Characterization-Project/
├── Analysis/
│   └── plot_iv_characteristics.py
├── Data/
│   └── IV_Data.xls
│   └── IV_Data_Charted.xlsx
├── Images/
│   └── GFET_Top_View.jpg
│   └── GFET_Channel_Dimensions.jpg
│   └── gfet_transfer_plot.png
│   └── IV Curve (Plotted in Excel).png
├── Report/
│   └── Lab_Report_MicroNano.pdf
│   └── LMAN_Presentation_Final.pdf
├── README.md
```

---

## 📜 License

This repository is open for academic and demonstration purposes.

---

## 👤 Author

**Mainak Roy**
[LinkedIn](https://www.linkedin.com/in/roy-mainak) 
