import requests
import os

base_dir=os.path.dirname(os.path.abspath(__file__))
url="https://www.nawpic.com/media/2020/kakashi-nawpic-15.jpg"
base_name=os.path.basename(url)
destination=os.path.join(base_dir,"downloads")
os.makedirs(destination,exist_ok=True)

with requests.get(url,stream=True) as r:  
    final_path=os.path.join(destination, base_name)
    with open(final_path,'wb') as file:
        file.write(r.content)
