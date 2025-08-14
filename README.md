# CASHFLOW-API

A RESTful API built with Flask for managing personal finances and cash flow tracking. This API allows users to register, authenticate, and manage their financial transactions with income and expense tracking capabilities.

## Features

- **User Authentication**: Secure user registration and login with JWT tokens
- **Transaction Management**: Create, read, update, and delete financial transactions
- **Balance Calculation**: Automatic calculation of current balance based on income and expenses
- **User Profile Management**: Complete CRUD operations for user profiles
- **Secure**: JWT-based authentication and authorization
- **CORS Enabled**: Cross-origin resource sharing support

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLAlchemy with SQLite
- **Authentication**: Flask-JWT-Extended
- **CORS**: Flask-CORS
- **Password Security**: Werkzeug security utilities

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/beneditotulio/CASHFLOW-API.git
   cd CASHFLOW-API
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```
   SECRET_KEY=your-secret-key-here
   JWT_SECRET_KEY=your-jwt-secret-key-here
   DATABASE_URL=sqlite:///cashflow.db
   ```

6. **Run the application**
   ```bash
   python run.py
   ```

The API will be available at `http://localhost:5000`

## API Endpoints

### Authentication

#### Register User
- **POST** `/api/register`
- **Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```

#### Login User
- **POST** `/api/login`
- **Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**:
  ```json
  {
    "access_token": "jwt_token_here"
  }
  ```

### User Profile

#### Get Profile
- **GET** `/api/profile`
- **Headers**: `Authorization: Bearer <jwt_token>`

#### Update Profile
- **PUT** `/api/profile`
- **Headers**: `Authorization: Bearer <jwt_token>`
- **Body**:
  ```json
  {
    "username": "string"
  }
  ```

#### Delete Profile
- **DELETE** `/api/profile`
- **Headers**: `Authorization: Bearer <jwt_token>`

### Transactions

#### Get All Transactions
- **GET** `/api/transactions`
- **Headers**: `Authorization: Bearer <jwt_token>`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "description": "Salary",
      "amount": 5000.00,
      "type": "income",
      "date": "2025-08-14T10:30:00",
      "user_id": 1
    }
  ]
  ```

#### Get Single Transaction
- **GET** `/api/transactions/<transaction_id>`
- **Headers**: `Authorization: Bearer <jwt_token>`

#### Update Transaction
- **PUT** `/api/transactions/<transaction_id>`
- **Headers**: `Authorization: Bearer <jwt_token>`
- **Body**:
  ```json
  {
    "description": "string",
    "amount": 0.00
  }
  ```

#### Delete Transaction
- **DELETE** `/api/transactions/<transaction_id>`
- **Headers**: `Authorization: Bearer <jwt_token>`

### Balance

#### Get Current Balance
- **GET** `/api/balance`
- **Headers**: `Authorization: Bearer <jwt_token>`
- **Response**:
  ```json
  {
    "balance": 2500.75
  }
  ```

## Data Models

### User
```python
{
  "id": "integer",
  "username": "string",
  "password_hash": "string",
  "created_at": "datetime",
  "transactions": "relationship"
}
```

### Transaction
```python
{
  "id": "integer",
  "description": "string",
  "amount": "decimal(10,2)",
  "type": "string",  # 'income' or 'expense'
  "date": "datetime",
  "user_id": "integer"
}
```

## Authentication

This API uses JWT (JSON Web Tokens) for authentication. After successful login, include the token in the Authorization header:

```
Authorization: Bearer <your_jwt_token>
```

## Error Handling

The API returns standard HTTP status codes:

- `200`: Success
- `201`: Created
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error

Error responses include a descriptive message:
```json
{
  "msg": "Error description"
}
```

## Project Structure

```
CASHFLOW-API/
├── app/
│   ├── __init__.py          # Application factory
│   ├── extensions.py        # Flask extensions
│   ├── models.py           # Database models
│   ├── routes.py           # API routes
│   ├── security.py         # Authentication logic
│   └── utils.py            # Utility functions
├── instance/               # Instance-specific files
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── run.py                # Application entry point
└── README.md             # This file
```

## Development

### Running in Development Mode

The application runs in debug mode by default when using `python run.py`. This enables:
- Auto-reload on code changes
- Detailed error messages
- Debug toolbar

### Database

The application uses SQLite by default. The database file (`cashflow.db`) will be created automatically in the `instance/` directory when you first run the application.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.