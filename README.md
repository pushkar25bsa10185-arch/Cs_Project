# 🌐 **Insurance Policy CRUD Manager**

A simple and interactive **Python CLI application** for managing insurance policies using basic **CRUD (Create, Read, Update, Delete)** operations.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

## 📑 **Table of Contents**

* [✨ Features](#-features)
* [📂 Initial Dataset](#-initial-dataset)
* [▶️ How to Run](#️-how-to-run)
* [📘 Application Menu](#-application-menu)
* [🛠 Code Structure](#-code-structure)
* [📌 Notes & Limitations](#-notes--limitations)
* [🚀 Future Enhancements](#-future-enhancements)
* [📜 License](#-license)
* [🤝 Contributing](#-contributing)

---

## ✨ **Features**

✔ **Add New Policy** – Input details for a new insurance policy
✔ **View All Policies** – Displays a neat, numbered list
✔ **Update Existing Policy** – Modify policy by entering its policy number
✔ **Delete Policy** – Remove a policy from the dataset
✔ **Exit Program** – Clean shutdown

---

## 📂 **Initial Dataset**

The program starts with three sample insurance policies:

```python
policies = [
    {
        "policy_number": "P1001",
        "holder_name": "Alice Johnson",
        "policy_type": "Health",
        "premium_amount": "5000"
    },
    {
        "policy_number": "P1002",
        "holder_name": "Bob Smith",
        "policy_type": "Life",
        "premium_amount": "7000"
    },
    {
        "policy_number": "P1003",
        "holder_name": "Carlos Davis",
        "policy_type": "Vehicle",
        "premium_amount": "3000"
    }
]
```

---

## ▶️ **How to Run**

### **1. Install Python**

Ensure you have **Python 3.x** installed.

### **2. Save the Script**

Save the code into a file, for example:

```
insurance_manager.py
```

### **3. Run the Application**

```bash
python insurance_manager.py
```

---

## 📘 **Application Menu**

When launched, the program displays:

```
Insurance Policy CRUD Manager
1. Add Policy
2. View Policies
3. Update Policy
4. Delete Policy
5. Exit
```

Enter the number corresponding to the action you'd like to perform.

---

## 🛠 **Code Structure**

| Function Name     | Description                         |
| ----------------- | ----------------------------------- |
| `add_policy()`    | Adds a new insurance policy         |
| `view_policies()` | Displays all policy records         |
| `update_policy()` | Updates selected policy information |
| `delete_policy()` | Deletes a policy from the list      |
| `main_menu()`     | Runs the interactive CLI            |

---

## 📌 **Notes & Limitations**

⚠️ Policy data is stored **in memory only**
→ All changes reset once the program ends.

⚠️ Basic input handling
→ No duplicate detection or strict validation.

⚠️ CLI-based
→ No GUI, API, or file storage (yet).

---

## 🚀 **Future Enhancements**

Here are some useful improvements you can add:

🔹 Save & load policies using **JSON or CSV**
🔹 Integrate **SQLite or MySQL** database
🔹 Build a **REST API** version using Flask / FastAPI
🔹 Add a **Tkinter or PyQt GUI**
🔹 Include search & filter features
🔹 Add colorized terminal output
🔹 Implement better validation & error handling

---

## 📜 **License**

This project is open-source under the **MIT License**.

---

