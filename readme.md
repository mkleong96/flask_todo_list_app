## Instruction for building the app
1. Clone this repository.
```bash
# Clone this repo
git clone https://github.com/mkleong96/flask_todo_list_app
cd flask_todo_list_app
```

2. Create virtual environment and install dependencies.
```bash
$ # Conda create venv
$ conda create --name flask_env python=3.9.7
$ pip install -r requirements.txt
```

3. Activate venv and run the server.
```bash
$ # Conda activate venv
$ conda activate flask_env
$ flask run --cert=adhoc #to make sure the app running using https protocol
```

## Instruction for running the app
1. To login to the app
```bash
curl -k https://127.0.0.1:5000/login/github
```
![image](https://user-images.githubusercontent.com/81457132/184542033-927b39bc-7c48-40e6-b74f-7988e744925a.png)
# Copy the link and open the Github sign in page to login


2. To show the to-do list added
```bash
curl -k https://127.0.0.1:5000/list_all
```

3. To add new to-do list
curl -k -i -H "Content-Type: application/json" -X POST -d "{\"title\":\"Read a book\", \"description\":\"Read a book on Monday\", \"status\":\"not complete\"  }" https://127.0.0.1:5000/add_to_do_list

#To delete a to-do list
curl -k -H "Content-Type: application/json" -X POST -d "{\"id\":\"3\"}" https://127.0.0.1:5000/delete_list

#To mark a to-do list done
curl -k -H "Content-Type: application/json" -X POST -d "{\"id\":\"3\" ,\"status\":\"done\"}" https://127.0.0.1:5000/mark_list_done

flask run --cert=adhoc