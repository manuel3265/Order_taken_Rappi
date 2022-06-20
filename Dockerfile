FROM python:3.8
ENV LANG C.UTF-8
RUN python3.8 -m pip install pip==21.0.1
RUN apt-get update && apt-get install -y zip gunicorn
# Install requirements
ENV LANG C.UTF-8
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





