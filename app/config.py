class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///etle.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'
    EMAIL_ADDRESS = 'your_email@example.com'
    EMAIL_PASSWORD = 'your_email_password'
