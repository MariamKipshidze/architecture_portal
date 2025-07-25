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

## Deployment

1. **Create Amazon EC2 instance**
   
   - Use the Ubuntu operating system.

2. **Create security groups**
