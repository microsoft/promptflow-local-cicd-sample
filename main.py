from summarizer import summarize_text
import os

FILE_PATH = "input.txt"

def read_file(file_path):
    """
    Read and return the content of a file.

    Args:
        file_path (str): Path to the file to be read.

    Returns:
        str: Content of the file.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except IOError as e:
        raise Exception(f"Error reading file {file_path}: {e}")

def main():
    """
    Main function to read, summarize, and print the summary of a text file.
    """

    # Check if DEPLOYMENT_NAME, AZURE_OPENAI_ENDPOINT & AZURE_OPENAI_API_KEY are set.
    if not os.environ.get("DEPLOYMENT_NAME"):
        raise Exception("DEPLOYMENT_NAME is not set.")
    if not os.environ.get("AZURE_OPENAI_ENDPOINT"):
        raise Exception("AZURE_OPENAI_ENDPOINT is not set.")
    if not os.environ.get("AZURE_OPENAI_API_KEY"):
        raise Exception("AZURE_OPENAI_API_KEY is not set.")


    try:
        text = read_file(FILE_PATH)
        summary = summarize_text(text)
        print("Summary:\n", summary)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()