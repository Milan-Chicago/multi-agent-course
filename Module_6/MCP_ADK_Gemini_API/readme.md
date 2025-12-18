# MCP_ADK_with_Gemini_API Setup Instructions

## Step 0:
Navigate to the project’s parent directory using the terminal:

git clone https://github.com/hamzafarooq/multi-agent-course.git

cd multi-agent-course/Module_6/MCP (non-adk)

## Step 1:
Create and activate a conda environment with Python 3.10 or greater:

conda create -n mcp_env python=3.10

conda activate mcp_env

Then install the required dependencies:

pip install -r requirements.txt

## Step 2:

export GOOGLE_GENAI_USE_VERTEXAI=false

export GOOGLE_API_KEY="your_api_key_here"

## Step 3:
Open the file `servers\server_mcp.py` and update the dataset path:

Load dataset and create database. Add the path to 'walmart_sales.csv'.

This file is located in the 'data' folder.

df = pd.read_csv(r"/content/multi-agent-course/Module_6/MCP (non-adk)/data/walmart_sales.csv")

## Step 4:
Run the client script to start querying:

python main.py

## Workflow
![a2a_mcp](https://github.com/user-attachments/assets/afc4cabe-4a52-44ee-84e3-72dae4198b91)
