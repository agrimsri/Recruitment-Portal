from dotenv import load_dotenv
from app import create_app

# Load environment variables at the very start of the application
load_dotenv()

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
