FROM python:2.7
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
CMD gunicorn -w4 -b0.0.0.0 library_response:app
EXPOSE 8000