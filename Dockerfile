FROM python:3.8
ENV LANG C.UTF-
RUN apt-get update && apt-get install -y zip gunicorn
# Install requirements
ENV LANG C.UTF-8
RUN pip3 install --upgrade pip
RUN pip3 install numpy==1.22.4
RUN pip3 install --upgrade setuptools
COPY requirements.txt /
RUN pip3 install -r /requirements.txt

WORKDIR /app
COPY ./app /app
RUN ls /app/pretrained/
RUN cd /app/pretrained/ && unzip order_taken.zip
RUN mkdir /app/temp
CMD ["python3.8", "server.py"]
# CMD uvicorn server:app --reload --port 90
EXPOSE 8998
EXPOSE 9889





