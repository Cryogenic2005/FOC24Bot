FROM python:3.11.5

RUN mkdir /foc24bot
COPY . /foc24bot
WORKDIR /foc24bot
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]