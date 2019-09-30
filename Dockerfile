FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app_dir
WORKDIR /app_dir
ADD requirements.txt /app_dir/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /app_dir/
