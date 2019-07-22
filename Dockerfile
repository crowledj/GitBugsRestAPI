FROM python:alpine3.7
COPY . /rubikAssigfn
WORKDIR /rubikAssigfn
RUN pip install -r requirements.txt
EXPOSE 8080
CMD  python ./create_localStore.py 
CMD  python ./app.py
