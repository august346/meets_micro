FROM python:3.8
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn
WORKDIR /app
COPY . /app
EXPOSE 5000
CMD ["gunicorn", "app:app", "-w", "4", "-b", "0.0.0.0:5000"]