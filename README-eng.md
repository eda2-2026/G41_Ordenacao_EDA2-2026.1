[🇧🇷 Português](README.md) | 🇺🇸 **English**
<H1> Sorting Algorithms Project - Library System (SB) 📚 </H1>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Completed-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Sorting-Quick%20%7C%20Heap%20%7C%20Radix-purple?style=flat-square" alt="Sorting">
</p>

<p align="center">
  <img src="https://i.postimg.cc/YCsvxJLN/Captura-de-Tela-2026-04-04-a-s-02-39-39.png" width="500">
</p>

---
## 📹 Video explaining the project
[Vídeo do youtube](https://youtu.be/dPdShpI-ZTY)


## 📝 Description

The **Library System (SB)** is a Python application designed to be fast and user-friendly. Featuring a modern dark mode interface, it was built to ensure fluid navigation and catalog organization, without freezing or unnecessary wait times.

In this new version, the main focus of the system is the **dynamic structuring and sorting of data**. To handle different types of information (text, integers, decimals, and dates), the system applies specific approaches to each table column. This includes using **Quick Sort** for alphabetical categorization, **Heap Sort** for precise rating rankings, and **Radix Sort (MSD)** for chronological sorting.

Ultimately, the system can instantly list, reorganize, and reverse large amounts of books, maintaining a perfect balance between algorithmic efficiency and a simple, pleasant everyday user experience.

## 💡 Technical Differentials - Sorting Algorithms

The major highlight of this update is the Sorting Module, which utilizes different algorithmic strategies depending on the column selected by the user in the interface:

- **Quick Sort:** Implemented as the primary (all-rounder) algorithm for sorting *strings* (Title, Author, Genre) and simple integers (ID Numbering and Loan Count). It ensures speed in alphabetical and popularity organization.
- **Heap Sort:** Structured specifically to organize books based on floating-point numbers (*floats*). It is triggered when the user wants to view the highest or lowest Average Rating scores in the catalog.
- **Radix Sort (MSD):** Implemented with the *Most Significant Digit* recursive approach using *buckets* separation. It is the ideal algorithm for sorting fixed-size integers, applied exclusively to sort Publication Years.
- **Merge Sort:** A divide-and-conquer algorithm implemented in the system's core library, ensuring flexibility and stability as a baseline alternative for data processing.


## 🌐 Sorting Demonstration

<p align="center">
  <img src="https://i.postimg.cc/SQrYLNBB/image.png" width="600">
  <br></br>
  <img src="https://i.postimg.cc/nVRccjbv/image.png" width="600">
  <br></br>
  <img src="https://i.postimg.cc/tJwjd6pS/image.png" width="600">
</p>

## 🎯 Features

- **Dynamic Table Sorting:** Click on any table header to instantly organize the catalog, with support for reverse sorting (Ascending/Descending or A-Z/Z-A).
- **Catalog Management:** Detailed book registration, including title, author, genre, and stock.
- **Student Registration:** Centralized user control, securely storing enrollment and contact data.
- **Dynamic Editing:** Allows updating information for already registered books and students, keeping the database always up to date.
- **Loan and Popularity Control:** Agile checkout logging, associating the student with the book and automatically counting the number of times the work has been borrowed.
- **Returns and Ratings Management:** Automatic loan discharge with an integrated feature for the student to register a 0 to 5-star rating for the returned work.

---

## 💻 Prerequisites

Before running the program, make sure you have the following requirements installed:

**1. Python 3.10 or higher.**

**2. Dependencies:**

- PySide6; and 
- qdarktheme.

**3.Operating System: Windows, macOS, or Linux**

 ---

## 🚀 Running the Project

**1. Instalar o python**

Check if you have Python 3.10 or higher installed. To do this, follow these steps:

Open the Terminal (on Windows, use Command Prompt or PowerShell).

Type the following command to check the version:

```bash
python --version
```

**Or**

```bash
python3 --version
```

If you don't have Python 3.10, you can download it [here](https://www.python.org/downloads/).

**2. Clone the Repository**

First, clone the project repository to your machine. Open the terminal and run:

```bash
git clone https://github.com/eda2-2026/G41_Ordenacao_EDA2-2026.1.git
```

**3. Install Dependencies:**

Navigate to the project directory in the terminal and run the following command to install all dependencies:

```bash
pip install -r requirements.txt
```

If the **requirements.txt** file is not present, you can install the dependencies manually:* **Install Pyside6**

```bash
pip install pyside6 
```

- **Install qdarktheme**

```bash
pip install qdarktheme
```

**4. Run the Program**

With the environment configured and dependencies installed, you can now run the system:

```bash
python biblioteca.py
```

**Or**

```bash
python3 biblioteca.py
```

**⚠️ Note:**
If the code presents any error during execution, verify if all necessary files are present (especially the .json files in the db_files directory).

---

## 🫂 Contributors

| <span style="color:black;">[Camila Cavalcante - 2320133944](https://github.com/CamilaSilvaC)</span> | <span style="color:black;">[Luísa Ferreira - 232014807](https://github.com/luisa12ll)</span> |
| :---: | :---: |
| <div align="center"><img src="https://github.com/CamilaSilvaC.png" alt="camila" width="400"></div> | <div align="center"><img src="https://github.com/luisa12ll.png" alt="luisa" width="400"></div> |
