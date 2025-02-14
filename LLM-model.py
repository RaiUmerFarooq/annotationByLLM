import os
import pandas as pd
import time
from tqdm import tqdm
from google import genai

client = genai.Client(api_key="api-key")


categories = ["Deep Learning", "Computer Vision", "Reinforcement Learning", "Natural Language Processing", "Optimization"]

csv_file_path = "extracted_papers.csv"

df = pd.read_csv(csv_file_path)


def retry_on_quota_error(func, *args, **kwargs):
    for _ in range(3):  # Retry 3 times
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if "RESOURCE_EXHAUSTED" in str(e):
                print("Quota exceeded, retrying in 10 seconds...")
                time.sleep(10)
            else:
                raise e  # Raise other exceptions
    return "Error after retries"


def classify_paper(title, abstract):
    prompt = f"""
    Classify the following research paper into one of these categories:
    {categories}

    Title: {title}
    Abstract: {abstract}

    Return only the category name.
    """

    try:
        # Throttle requests by adding a 1-second delay between requests
        time.sleep(1)  # Adjust the delay as needed

        # Use retry logic to handle resource exhaustion errors
        response = retry_on_quota_error(client.models.generate_content, model="gemini-2.0-flash", contents=prompt)

        # Process the response
        if isinstance(response, str):  # If retry logic failed
            return response

        category = response.text.strip()
        if category not in categories:
            return "Uncategorized"
        return category
    except Exception as e:
        print(f"Error: {e}")
        return "Error"


tqdm.pandas()
df["Category"] = df.progress_apply(lambda row: classify_paper(row["Title"], row["Abstract"]), axis=1)


output_file = "/content/annotated_papers.csv"
df.to_csv(output_file, index=False)
print(f"Annotated dataset saved at: {output_file}")
