FROM python:3.8-slim-buster

RUN apt-get update -y
RUN apt install libgl1-mesa-glx wget libglib2.0-0 -y

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY index.html /usr/local/lib/python3.8/site-packages/streamlit/static/index.html

COPY . .

WORKDIR .

EXPOSE 8501

ENTRYPOINT [ "streamlit", "run" ]
CMD [ "app.py", "--server.headless", "true", "--server.fileWatcherType", "none", "--browser.gatherUsageStats", "false"]
