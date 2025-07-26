# Architectural Portal

A Django-based web application for architectural companies featuring a project price calculator.

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MariamKipshidze/architectural-portal.git
   cd architectural-portal
   ```

2. **Set up virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to project directory**
   ```bash
   cd architecture_portal
   ```
   
5. **Create your `.env` file**
   ```bash
   cp .env.example .env
   ```

6. **Generate and set Django secret key**
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(f'SECRET_KEY={get_random_secret_key()}')" >> .env
   ```

7. **Run migrations**
   ```bash
   python manage.py migrate
   ```

8. **Create superuser (optional - for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

## Running the Application

1. **Start development server**
   ```bash
   python manage.py runserver
   ```

2. **Access the application**
   Open your browser to:
   ```
   http://localhost:8000/
   ```

3. **Access the price calculator**
   The calculator is available at:
   ```
   http://localhost:8000/calculator/
   ```

## Customizing Prices

To modify the pricing logic, edit these values in `app/views.py`:

```python
# Pricing configuration (modify these values)
BASE_PRICE_PER_SQM = 50  # Base price per square meter
COMPLEXITY_MULTIPLIERS = {
    'simple': 1.0,      # Simple design multiplier
    'medium': 1.3,      # Medium complexity multiplier
    'complex': 1.7      # Complex design multiplier
}
FLOOR_MULTIPLIER = 0.2  # 20% increase per additional floor
```

## Deployment on Amazon EC2 instance

1. **Create Amazon EC2 instance**
   
   - Use the Ubuntu operating system. 

2. **Configure Security Group**  
   Add the following inbound rules to allow necessary traffic:  

   - **First Inbound Rule (SSH Access)**  
     - **Type**: SSH  
     - **Protocol**: TCP  
     - **Port Range**: 22  
     - **Source**: `0.0.0.0/0` (or restrict to your IP for security, e.g., `123.45.67.89/32`)  

   - **Second Inbound Rule (HTTP Access)**  
     - **Type**: HTTP  
     - **Protocol**: TCP  
     - **Port Range**: 80  
     - **Source**: `0.0.0.0/0` (public web traffic)  

   - **Third Inbound Rule (HTTP Access)**  
     - **Type**: HTTP 
     - **Protocol**: TCP  
     - **Port Range**: 80
     - **Source**: `::/0` (secure web traffic)
       
   - **Outbound Rules:**
     - By default, AWS allows all outbound traffic. This means your instance can initiate connections to the internet (e.g., for updates, downloads, or external API calls).
       
3. **Add Security Group to instance**

4. **Update and Upgarde ubuntu**
   ```bash
   sudo apt-get update
   sudo apt-get upgrade
   ```
5. **Check python version**

   If the Python version doesn’t match your project’s requirements, change it (e.g., using pyenv or update-alternatives).

   ```bash
   # Check installed Python versions:
   python3 --version  # or: python --version
   
   # Switch versions (example using pyenv):
   pyenv install 3.9.13  # Install a specific version
   pyenv global 3.9.13   # Set it as default
   ```

6. **Set Up a Python Virtual Environment**  
   1. **Install the `virtualenv` package**:  
      ```bash
      sudo apt update && sudo apt install python3-virtualenv -y
      ```
   
   2. **Create a virtual environment** (e.g., for your project):  
      ```bash
      virtualenv venv --python=python3  # Uses your default Python 3
      ```
      *Replace `python3` with a specific version (e.g., `python3.9`) if needed.*
   
   3. **Activate the environment**:  
      ```bash
      source venv/bin/activate  # Linux/macOS
      ```
      *(For Windows: `.\venv\Scripts\activate`)*  
   
   4. **Verify activation**:  
      Your terminal prompt should now show `(venv)`.

7. **Clone the Project Repository**  
   1. **Navigate to your target directory (optional)** (where the code should live):  
      ```bash
      cd /path/to/your/projects  # Example: ~/projects
      ```
   
   2. **Clone the repository**:  
      ```bash
      git clone https://github.com/MariamKipshidze/architecture_portal.git
      ```
   
   3. **Enter the project directory**:  
      ```bash
      cd architecture_portal
      ```
8. ** Install requirments**
   ```bash
   pip install -r /home/ubuntu/architecture_portal/requirements.txt
   ```
   
9. **Install Nginx**
   ```bash
   sudo apt-get install -y nginx
   ```

10. **Install Gunicorn**
   ```bash
   pip install gunicorn
   ```

11. **Install Supervisor**
   ```bash
   sudo apt-get install supervisor
   ```

12. **Create Gunicorn conf file**
   ```bash
   cd /etc/supervisor/conf.d/
   sudo touch gunicorn.conf
   sudo nano gunicorn.conf
   ```
   Add this to gunicorn.conf file

   ```bash
   [program:gunicorn]
   directory=/home/ubuntu/architecture_portal/architecture_portal  # Parent of manage.py
   command=/home/ubuntu/venv/bin/gunicorn --workers 3 --bind unix:/run/gunicorn/app.sock architecture_portal.wsgi:application
   autostart=true
   autorestart=true
   stderr_logfile=/var/log/gunicorn/gunicorn.err.log
   stdout_logfile=/var/log/gunicorn/gunicorn.out.log
   environment=
       PATH="/home/ubuntu/venv/bin:%(ENV_PATH)s",
       VIRTUAL_ENV="/home/ubuntu/venv"
   
   [group:guni]
   programs:gunicorn 
   ```

13. **Create a directory for Gunicorn logs**
   ```bash
   sudo mkdir /var/log/gunicorn
   ```

14. **Tell supervisor to read from the gunicorn configuration file**
   ```bash
   sudo supervisorctl reread
   ```

15. **Tell supervisor to start gunicorn process in the background**
   ```bash
   sudo supervisorctl update
   ```
