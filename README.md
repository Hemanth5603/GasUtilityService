# Gas Utility Service - Django Application

A web-based application developed using Django to manage consumer services for a gas utility company. This application allows customers to submit service requests, 
track the status of their requests, and view their account information. It also provides tools for customer support representatives to manage and resolve customer requests.



## **Project Description**
The Gas Utility Service application aims to streamline the management of customer service requests for gas utilities. Customers can submit various service requests such as installations, repairs, and maintenance directly through the web portal. The platform allows them to track the status of their requests, while customer support representatives have a dedicated interface to handle and resolve the requests efficiently.

## **Features**
- **User Registration**: New users can register an account using a simple registration form.
- **User Login**: Registered users can log in to access their service request history.
- **Submit Service Requests**: Customers can submit service requests by selecting the type of service, providing a description, and attaching relevant documents.
- **Track Service Requests**: Customers can view and track the status of their submitted service requests.
- **Admin Interface**: A powerful admin panel for customer support representatives to manage service requests.
- **File Uploads**: Customers can upload attachments when submitting service requests.
- **Responsive Design**: Clean and user-friendly interface for both desktop and mobile devices.

## **Installation**

### **Prerequisites**
- Python 3.8+
- Pip
- Git

### **Step-by-Step Setup**
1. **Clone the Repository**
   
```bash
   git clone https://github.com/Hemanth5603/GasUtilityService.git
```

```bash
   cd gas-utility-service
```

2. Apply Database Miigrations

```bash
python manage.py makemigrations
python manage.py migrate
```

3. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

4. Run the Server

```bash
python manage.py runserver
```

5. Access the Applicaton

 - Customer Portal: http://127.0.0.1:8000/service/login/
 - Admin Panel: http://127.0.0.1:8000/admin/



## **Usage**
**Register a New Account**
 - Visit the registration page: http://127.0.0.1:8000/service/register/.
 - Fill in the registration form to create a new account.
   
**Login**
 - Go to the login page: http://127.0.0.1:8000/service/login/.
 - Enter your credentials to access the service dashboard.

**Submit a Service Request**
 - After logging in, navigate to the "Submit Request" page.
 - Choose the service type, provide a description, and upload any necessary files.
**Track Service Requests**
 - Check the status of submitted requests on the "Track Requests" page.

**Demo Video** 


https://github.com/user-attachments/assets/59fe4689-a1bc-42b9-9b18-32ffba7d9ef5



## **Screenshots**
![Tracking](https://github.com/user-attachments/assets/b3b5995c-7fff-456a-8aca-6d83569553f3)
![Submit Request](https://github.com/user-attachments/assets/f257db22-4984-4518-a098-5eebd7915978)
![login](https://github.com/user-attachments/assets/1e9bceac-b593-45a7-af59-d1de4bad82a1)
![Register](https://github.com/user-attachments/assets/f0743d68-ed1b-4f95-a18c-29ad4eb3fc51)



