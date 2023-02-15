FROM python:3.10.10-alpine3.17

#copy
COPY . /api

#defining work directory 
WORKDIR /api

RUN pip install -r python_req.txt 
#--no-cache-dir
# can also added for  no cache in dir  

EXPOSE 5000 6379

#if not executable than have to use ENTERYPOINT LIKE
#ENTRYPOINT [ "python" ]

#CMD [ "executable", "parameter", ... ]
CMD [ "python", "app.py" ]  