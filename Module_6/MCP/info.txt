===========================
MCP_ADK_with_Gemini_API Setup Instructions
===========================

Step 0:
Navigate to the project’s parent directory using the terminal:
cd MCP_ADK_with_Gemini_API

Step 1:
Create and activate a conda environment with Python 3.10 or greater:

conda create -n mcp_env python=3.10
conda activate mcp_env

Then install the required dependencies:
pip install -r requirements.txt

Step 2:
Update the `.env` file with your Google API key:

GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY="your_api_key_here"

Step 3:
Open the file `servers\server_mcp.py` and update the dataset path:

# Load dataset and create database. Add the path to 'walmart_sales.csv'.
# This file is located in the 'data' folder.
df = pd.read_csv(r"C:\Users\alish\Documents\google_adk\non_adk_mcp_walmart_sales_db\data\walmart_sales.csv")

Step 4:
Run the client script to start querying:

python .\clients\query_MCP_ADK.py
