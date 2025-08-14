# StudyMate Installation Guide

## Quick Start (Recommended)

1. **Navigate to the project directory**
   ```bash
   cd "OneDrive/Desktop/GEN AUGMENT"
   ```

2. **Run the automated setup**
   ```bash
   python setup.py
   ```

3. **Configure your credentials**
   - Edit the `.env` file with your IBM Watsonx AI credentials
   - See "Getting IBM Watsonx Credentials" section below

4. **Test the installation**
   ```bash
   python test_studymate.py
   ```

5. **Start the application**
   ```bash
   streamlit run app.py
   ```

## Getting IBM Watsonx AI Credentials

### Step 1: Create IBM Cloud Account
1. Go to [IBM Cloud](https://cloud.ibm.com/)
2. Sign up for a free account or log in

### Step 2: Create Watsonx AI Service
1. Navigate to the IBM Cloud catalog
2. Search for "Watsonx" or go to AI/Machine Learning section
3. Select "Watsonx.ai"
4. Create a new service instance

### Step 3: Get Your Credentials
1. **API Key**: 
   - Go to IBM Cloud > Manage > Access (IAM)
   - Create or use existing API key
   
2. **Project ID**:
   - In Watsonx.ai, create or select a project
   - Copy the project ID from the project settings
   
3. **Service URL**:
   - Usually: `https://us-south.ml.cloud.ibm.com`
   - Check your service instance for the exact URL

### Step 4: Configure Environment
Edit your `.env` file:
```
IBM_API_KEY=your_actual_api_key_here
IBM_PROJECT_ID=your_actual_project_id_here
IBM_URL=https://us-south.ml.cloud.ibm.com
```

## Manual Installation

If the automated setup doesn't work, follow these steps:

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Internet connection for downloading models

### Step-by-Step Installation

1. **Install Python dependencies**
   ```bash
   pip install streamlit==1.28.1
   pip install PyMuPDF==1.23.8
   pip install sentence-transformers==2.2.2
   pip install faiss-cpu==1.7.4
   pip install ibm-watsonx-ai==1.0.5
   pip install python-dotenv==1.0.0
   pip install numpy==1.24.3
   pip install pandas==2.0.3
   ```

2. **Or install from requirements file**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment file**
   ```bash
   copy .env.example .env
   ```
   Then edit `.env` with your credentials.

## Verification

### Test Individual Components
```bash
# Test PDF processing
python -c "from modules.pdf_processor import create_pdf_processor; print('PDF processor OK')"

# Test embeddings
python -c "from modules.embeddings import create_embedding_manager; print('Embeddings OK')"

# Test LLM integration (requires credentials)
python -c "from modules.llm_integration import create_watsonx_llm; print('LLM integration OK')"
```

### Run Full Test Suite
```bash
python test_studymate.py
```

### Try the Demo
```bash
python demo.py
```

## Troubleshooting

### Common Installation Issues

1. **Python Version Error**
   ```
   Error: Python 3.8 or higher is required
   ```
   **Solution**: Update Python to version 3.8 or higher

2. **Package Installation Fails**
   ```
   Error: Failed to install dependencies
   ```
   **Solutions**:
   - Update pip: `python -m pip install --upgrade pip`
   - Install packages individually
   - Use virtual environment

3. **FAISS Installation Issues**
   ```
   Error: Failed to install faiss-cpu
   ```
   **Solutions**:
   - Try: `pip install faiss-cpu --no-cache-dir`
   - On Windows: Use conda instead: `conda install faiss-cpu -c conda-forge`

4. **SentenceTransformers Download Issues**
   ```
   Error: Failed to download model
   ```
   **Solution**: Ensure stable internet connection and try again

### Runtime Issues

1. **Environment Variables Not Found**
   ```
   Error: Missing environment variables
   ```
   **Solution**: Check that `.env` file exists and contains all required variables

2. **IBM Watsonx Connection Failed**
   ```
   Error: Failed to initialize IBM Watsonx AI
   ```
   **Solutions**:
   - Verify API key is correct
   - Check project ID
   - Ensure service URL is correct
   - Check IBM Cloud service status

3. **Memory Issues**
   ```
   Error: Out of memory
   ```
   **Solutions**:
   - Process smaller PDFs
   - Reduce chunk size in configuration
   - Close other applications

## Performance Optimization

### For Better Performance
- Use SSD storage for faster model loading
- Ensure at least 4GB RAM available
- Process PDFs in batches of 5-10 files
- Use smaller chunk sizes for large documents

### For Lower Resource Usage
- Reduce chunk size to 300 words
- Limit retrieval to top-2 results
- Process one PDF at a time

## Getting Help

1. **Check the logs**: Look in the `logs/` directory for detailed error information
2. **Run diagnostics**: Use `python test_studymate.py` to identify issues
3. **Review documentation**: Check README.md for detailed usage instructions
4. **Verify setup**: Ensure all prerequisites are met
