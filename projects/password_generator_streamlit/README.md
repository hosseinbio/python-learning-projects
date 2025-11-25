# Password Generator (Streamlit App)

A simple and user-friendly **Streamlit-based GUI application** for generating different types of secure passwords.  
This tool provides three password-generation methods:

- **Random Password**
- **Memorable Password**
- **PIN Code**

---

## Features

### Random Password
- Adjustable password length  
- Option to include numbers  
- Option to include symbols  
- Fully randomized output  

### Memorable Password
- Choose the number of words  
- Customizable word separator  
- Optional capitalization  
- Uses a predefined vocabulary list  

### PIN
- Select PIN length  
- Generates a numeric-only password  

---

## Installation & Setup

### Install required packages
```bash
pip install -r requirements.txt
```

### Run the Streamlit app
From the project root:
```bash
streamlit run src/run.py
```

Or from inside the src folder:
```bash
streamlit run run.py
```

---

## Technologies Used
- Python 3.x
- Streamlit
- Built-in Python libraries
-   os
-   random
-   string
-   typing
