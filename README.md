# youtube_api
clone main.py file above

go to project folder in terminal
run following command in terminal to install some libraries

pip install flask
pip install google-api-python-client

it is ready to run 
execute following command to run project
python main.py

now look at terminal there is host url ip address like  http://127.0.0.1:5000/

there is following path its working

path -> /api/videos
working -> it get details of videos accroding to publishdatetime, response is in json formatte

path -> /api/videos/title/(title of video but replace space with '-' character)
working -> it get details of video which title match, response is in json formatte

path -> /api/videos/title/(description of video but replace space with '-' character, you can add any prifix part)
working -> it get details of video which description prefix match, response is in json formatte

