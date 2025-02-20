import os

def load_env_file(path=".env"):
    """Load key=value pairs from a .env file into os.environ."""
    if not os.path.exists(path):
        print(f"Warning: {path} does not exist.")
        return

    with open(path) as f:
        for line in f:
            line = line.strip()
            # Skip empty lines and comments
            if not line or line.startswith('#'):
                continue

            # Split on the first '='
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")  # remove surrounding quotes if any
            os.environ[key] = value
