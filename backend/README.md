# Backend

This directory contains the backend for the multi-agent AI system, built with Google's Agent Development Kit (ADK).

## Setup

1.  **Install Poetry:**
    If you don't have Poetry installed, follow the instructions [here](https://python-poetry.org/docs/#installation).

2.  **Install Dependencies:**
    Navigate to this directory and run:
    ```bash
    poetry install
    ```

3.  **Authenticate with google:**
    Run 
    ```
    gcloud auth application-default login
    ```

4.  **Run the Application:**
    ```bash
    poetry run python main.py
    ```
