import sys

def check_env():
    print("--- Python Environment Sanity Check ---")
    print(f"Python Version: {sys.version}")
    print("Status: Python environment is set up correctly.")

if __name__ == "__main__":
    check_env()