import requests

def download_video(video_id):
  url = "https://www.youtube.com/watch?v=" + video_id
  response = requests.get(url, stream=True)
  with open(video_id + ".mp4", "wb") as f:
    for chunk in response.iter_content(chunk_size=1024):
      f.write(chunk)

if __name__ == "__main__":
  video_id = input("Enter the YouTube video ID: ")
  download_video(video_id)