FROM dleunji/kantmodel
RUN mkdir /app/checkpoint
RUN mv /app/run1 /app/checkpoint
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0","--without-threads"]
