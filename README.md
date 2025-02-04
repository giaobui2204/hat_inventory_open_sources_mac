# General Information
Hat Inventory Open Source Beginner-Friendly Workshop

Author: WiCS Exec | 
Owner: Laura Bui | 
Contributors: You all!

## Brief Description: 
This program is beginner-friendly and allows for coders to learn how to debug and improve a project using git, FastAPI, Streamlit, and SQLite. The web application allows users to ADD, UPDATE, DELETE, and SELL hats, but the code, however, has various bugs in the frontend, backend, and database for participants to contribute to and fix. 

## Contributing 
Pull requests are welcome. To make changes, please open an issue on GitHub to discuss what you would like to change.

**Here is how to contribute:**

1. Check the Open Issues List

2. Create a New Branch    
    <span style="color: green;">git checkout -b fix-bug-< bug-number > </span>

3. Fix the Bug and Run the Code     
    <span style="color: green;">uvicorn backend:app --reload --port 8000	      
    streamlit run frontend.py </span>

4. Commit and Push       
    <span style="color: green;">git add .        
    git commit -m "Fix: Resolved bug < bug-number >"       
    git push origin fix-bug-< bug-number ></span>     

5. Submit a Pull Request
    - Go to **GitHub** and click **"Compare & pull Request."**   
    - Add a description    
    - Click **"Create pull request."**  





## How to Install the Programs Needed
The installation is different for Microsoft and MacOS users.
## How to Install the Programs Needed

### **Prerequisites**
Before starting, ensure you have the following installed:
- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [Visual Studio Code](https://code.visualstudio.com/)

The installation is different for Microsoft and MacOS users.

### **For Microsoft Users**

Follow these steps to install and set up the necessary programs:

### **1. Clone the Repository**
1. Open **Visual Studio Code** and create a new folder for the project.
2. Open the **terminal** in VS Code and run the following command to clone the repository:
   ```sh
   git clone https://github.com/giaobui2204/hat_inventory_open_sources_mac
3. After cloning the repository, navigate to the project folder:
   ```sh
   cd hat_inventory_open_sources_mac

### **2. Create the Virtual Environment**
1. In the terminal type:
    ```sh
    py -m venv venv
    ```
    ```sh
    venv\Scripts\activate.ps1

### **3. Installing dependencies**
    pip install fastapi uvicorn streamlit requests pydantic

### **4. Run the backend**
    py -m uvicorn backend:app --reload --port 8000

### **5. Run the frontend**
    streamlit run frontend.py

### **For MacOS Users**

Follow these steps to install and set up the necessary programs:

### **1. Clone the Repository**
1. Open **Visual Studio Code** and create a new folder for the project.
2. Open the **terminal** in VS Code and run the following command to clone the repository:
   ```sh
   git clone https://github.com/giaobui2204/hat_inventory_open_sources_mac
3. After cloning the repository, navigate to the project folder:
   ```sh
   cd hat_inventory_open_sources_mac

### **2. Create the Virtual Environment**
1. In the terminal type:
    ```sh
    python3 -m venv venv
    ```
    ```sh
    source venv/bin/activate

### **3. Installing dependencies**
    pip install fastapi uvicorn streamlit requests pydantic

### **4. Run the backend**
    python3 -m uvicorn backend:app --reload --port 8000

### **5. Run the frontend**
1. In the terminal type:
   ```sh
    source venv/bin/activate
    ```
    ```sh
   streamlit run frontend.py



