FROM dleunji/kantmodel
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0","--without-threads"]
