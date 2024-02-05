FROM nvidia/cuda:12.3.1-devel-ubuntu20.04
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3 python3-pip
RUN apt-get clean

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY script.py .
CMD [ "python3", "script.py" ]
