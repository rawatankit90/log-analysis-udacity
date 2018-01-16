#Log Analysis Project
A Udacity Project to create a reporting tool that prints out reports (in plain text) based on the data in the database.

# Getting Started
You can access the files of this project from [ this Github link](https://github.com/rawatankit90/log-analysis-udacity)

## Prerequistes
In order to view these files you must have a

1) A Web broswer(like IE or Chrome) installed on your computer.
2) A working internet connection.
3) A Virtual Machine and Vagrant setup to run

## With the above steps done
1) You can access the files from [ this Github link ] (https://github.com/rawatankit90/log-analysis-udacity) by clicking the green download button on the right.
2) Unzip the downloaded file.
3) Place the above files in Vagrant directory
4) From Vagrant, SSH to VM [Virtual Machine]  and navigate to the folder "log-analysis" under vagrant folder
5) Create the Views
        ```create view error_data as select count(*), time::date from log where  status='404 NOT FOUND' group by time::date;
        create view total_data as select count(*), time::date from log group by time::date;```
6) Run the command to start the python server : python loganalysis.py
7) Open the http://localhost:8000/ to see the output

## Built With love from udacity learner
1) HTML5
2) CSS3
3) Bootstrap 4
4) Python 3
5) Postgresql 9.5
