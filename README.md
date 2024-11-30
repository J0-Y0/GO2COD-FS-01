# **JanPost** 📝  
JanPost is a blogging platform designed to foster sharing insights on educational content. Built as part of an internship project at GO2Code, this platform focuses on creating meaningful conversations through posts, comments, and tagging while ensuring a secure and user-friendly experience.

---

## **Features**  

### **User Authentication and Authorization**  
- **Account Email Activation**: Ensure account validity through email activation tokens sent via SMTP.  
- **Password Reset**: Secure password reset functionality using email-based reset tokens via SMTP.  
- **Registration, Login, Logout, and Password Reset**.  
- Secure API access with JWT-based authentication.  

### **Blog Management**  
- Create, update, and delete blog posts with rich content support.  
- Categorization and tagging of posts for better discoverability.  

### **Comment System**  
- Nested comment structure for threaded discussions.  
- Tools to report and moderate user-generated content.  

### **User Profiles**  
- Customizable profiles with bio, profile picture, and social links.  
- Follow and unfollow functionality to track user activities.  

### **Like and Share**  
- Like posts and share content via APIs.  

### **Search and Filtering**  
- Advanced search with filtering by tags, categories, and author.  

---

## **Tech Stack**  

### **Backend**  
- **Framework**: Python (Django)  
- **API**: REST API with Swagger documentation  
- **Database**: PostgreSQL  
  - Chosen for its powerful query optimization, indexing, and scalability, ensuring high performance.  
- **Authentication**:  
  - JWT (JSON Web Tokens) for secure user authentication.  
  - Email-based account activation and password reset using SMTP.  

### **Frontend**  
- **React + TypeScript**: The frontend is currently under development. You can follow the progress here:  
  👉 [JanPost Frontend Repository](https://github.com/J0-Y0/GO2COD-FS-01-Frontend)

---

## **Installation & Setup**  

### **Prerequisites**  
- Python 3.10+
- PostgreSQL
- Pipenv (for dependency management)

### **Backend Setup**  
1. Clone the repository:  
    ```bash
      git clone https://github.com/J0-Y0/GO2COD-FS-01.git
      cd GO2COD-FS-01
    ```

2. Install dependencies:
    ```bash
      pipenv install
    ```
      
3. Set up your database connection:
      Add connection settings in `settings/dev.py` or `settings/prod.py`.
      Create a .env file and include the following fields: 
      ```bash
        DBNAME=<Your Database Name>
        DBUSER=<Your Database User>
        DBPASSWORD=<Your Database Password>
        HOST=<Your Database Host>
        PORT=5432
        SECRET_KEY=<Your Django Secret Key>
        ALLOWED_HOSTS=<Your Allowed Hosts>
        ALLOWED_ORIGINS=<Your Allowed Origins>
        EMAIL_HOST=<Your SMTP Server>
        EMAIL_PORT=<Your SMTP Port>
        EMAIL_USE_TLS=True
        EMAIL_HOST_USER=<Your Email Address>
        EMAIL_HOST_PASSWORD=<Your Email Password>
      ```
4. Apply database migrations:

    ```bash
      py manage.py migrate
    ```
5. Run the server:

    ```bash
    pipenv run p manage.py runserver
    ```
## **(Optional) Load mock data:**

Navigate to the `test_data/` folder and execute the database queries provided to populate your database with sample data.

## **Frontend Setup (In Progress):**  
Frontend development is ongoing. You can track the progress and contribute here:  
👉 [JanPost Frontend Repository](https://github.com/J0-Y0/GO2COD-FS-01-Frontend)

## **API Documentation**  
Swagger documentation is available for all API endpoints.  


## **Contributing**  
I  welcome contributions to improve this project! 🎉  

1. Fork the repository:  
  ```bash
    git fork https://github.com/J0-Y0/GO2COD-FS-01.git
  ```
2. Create your feature branch:
  ```bash
    git checkout -b feature-name
  ```
3.Commit your changes:
  ```bash
    git commit -m "Add a meaningful message"
  ```
4.Push your changes and create a pull request.

---


This project is open-source and available under the [MIT License](LICENSE).

