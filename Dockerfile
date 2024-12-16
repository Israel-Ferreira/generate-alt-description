FROM python:3.12

WORKDIR /usr/app

COPY  requirements.txt .


RUN pip install --no-cache-dir --upgrade -r requirements.txt


RUN mkdir temp

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]