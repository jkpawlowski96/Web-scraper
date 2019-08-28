FROM python:3
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN export PYTHONPATH="$PYTHONPATH:./"
COPY . .
CMD [ "python", "app.py" ]