FROM ubuntu:latest

ENV ENV=${ENV} \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/src/ 
    
RUN apt-get update && apt-get install -y \
    python3-pip 

COPY ./server/requirements.txt /

RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

ADD ./server/src /src

WORKDIR /src

VOLUME [.]

ENTRYPOINT ["python", "manage.py"]
