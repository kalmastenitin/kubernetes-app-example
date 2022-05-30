FROM python:3.9

# RUN useradd -ms /bin/bash diycam
# USER diycam

# declare workdirectory 
WORKDIR /home/diycam/code

COPY . /home/diycam/code
# install dependancies
COPY ./requirements.txt .
RUN pip install --user -r requirements.txt  

# add code
ADD . .

# make sciprt executable
# RUN ["chmod", "+x", "wait-for-it.sh"]

# expose port
EXPOSE 8000

CMD ["python3", "run.py"]