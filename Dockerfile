FROM tensorflow/tensorflow:1.15.5-gpu-py3
RUN mkdir -p /app
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0","--without-threads"]
