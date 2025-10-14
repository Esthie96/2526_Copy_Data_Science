import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
api_key = os.getenv('OPENAI_API_KEY')
db_host = os.getenv('DB_HOST', 'localhost')  # 'localhost' is the default value
debug_mode = os.getenv('DEBUG', 'False').lower() == 'true'

# Example usage
if api_key:
    print("API key loaded successfully")
else:
    print("Warning: API key not found in environment variables")




