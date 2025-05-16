from flask      import Flask
from flask      import render_template
from supabase   import create_client
from dotenv     import load_dotenv
import os

# Get enviroment variables
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Connect to supabase as a client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Create the Flask app
app = Flask(__name__)


@app.get("/")
def home():
    response = supabase.table("things").select().execute()
    records = response.data

    print(response)

    return render_template("pages/home.jinja", things=records)


@app.errorhandler(404)
def notFound(error):
    return render_template("pages/404.jinja")