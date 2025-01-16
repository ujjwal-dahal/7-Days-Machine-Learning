import requests
import os

def fetchAndSaveToFile(url , path):
  try:
    r = requests.get(url)
    
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    with open(path , "wb") as f:
      f.write(r.content)
    print("Successfully Fetched Data!")
  except Exception as e:
    print(f"Error : {e}")  
    

url = "https://en.wikipedia.org/wiki/Disease"

fetchAndSaveToFile(url , "data/fetchedData.html")