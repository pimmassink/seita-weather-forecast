# Pims log.
This file logs my journey through this exercise. I will write it as I go along. 

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

