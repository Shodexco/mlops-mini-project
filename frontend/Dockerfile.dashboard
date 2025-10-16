FROM python:3.12-slim

WORKDIR /app

# Copy frontend files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir streamlit requests joblib numpy pandas

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
