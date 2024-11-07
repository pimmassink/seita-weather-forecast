# Pims log.
This file logs my journey through this exercise. I will write it as I go along. It is now 16:48 

### 0. Setting up.
Ok, I just created this repository! Let's get started! The first problem is python and its dependency hell. I will use poetry because that is something I somewhat know. It comes close to NPM. A friend of mine who does more python mentions working with uv and dev containers is now standard. But I don't have the time to look that up.

So poetry it is. ArjanCodes helps me with how to set it up here https://www.youtube.com/watch?v=0f3moPe_bhk

`poetry init`

`poetry config virtualenvs.in-project true`

`poetry install`

`poetry add fastapi uvicorn`

Cool now I create a directory app and a file called main.py.

`poetry run ivucorn app.main:app --reload`

Hurray, hello world works!

Add a launch.json in the .vscode directory. Boom! Now we can launch with F5 in VsCode. Ok fun. That was enough VsCode for now. Time to open up a real tool: PyCharm.

I've added a launchconfig for PyCharm too. Great, now we can start thinking about the assignment. 

### 1. Creating the endpoints

The first thing I'll do is actually create the two endpoints. Then we know exactly what the user will send us. This means we must structure our application.

Personally, I come from a Java Spring background. So I am a big fan of the controller/service/persistence structure. An alternative would be more domain driven design. Also very interesting. I accept criticism that my approach isn't very "Python-y" or maybe very "Java-y". Sure. I would love to take the time and do research on how to set it up the "python way" but I don't have that. This would be a great conversation to have.

I've created a forecasts controller. ACtually I am a little confused. The requirements specified there should be a GET endpoiont for `/tomorrow`. But what would be the base path? Is "tomorrow" a domain? Maybe it is. There can be many customers that want to know things about tomorrow. For now I'll create a tomorrowController, weird as it feals. Because isn't tomorrow just another forecast?

OK. that was now done. I've now also created a postman collection which is nice.

# 2. Setting up the database
OK i've been at this for a while now. I think our data is pretty messy. I've taken the time to conver the CSV to a duckdb. That will be much easier to query. I've done this in a scripts directory. 
In the final application, these scripts will not be deployed, but they may be added to repository. Similarly I've created a jupyter notebook to do some querying. 
I don't have much experience with duckdb. Some googling revealed that it was more performant than SQL light for reading data.
I wanted to just query the db in pycharm. I've added it as a datasource, but it doesn't quite seem to work. Annoying. So i'll use jupyter for now.

OK it is now 18:23. Time for a break. I am not sure if I will continue this tonight. I think I will slowly go crazy. I'll take another ten minutes to push this to github and send a message to Felix. Then he can look at my progress live. I guess it makes sense to at least show some kind of design during the interview tomorrow. 
Man a homework assignment of 4 hours is very demanding. I find it hard to find the time and focus next to a 45 hour job and all the other applications. I wish I was back at university with endless amounts of time...

Wheew. it is now 23 minutes later, 18:46 and I am exhausted. I created a github repository but had problems with access right because this is a work laptop. Messing around with SSH keys takes its toll. More tomorrow!
