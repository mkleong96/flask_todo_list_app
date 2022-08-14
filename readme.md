## Instruction for building the app
#Method One using Github Repository
1. Clone this repository.
```bash
# Clone this repo
git clone https://github.com/mkleong96/flask_todo_list_app
cd flask_todo_list_app
```

2. Create virtual environment and install dependencies.
```bash
# Conda create venv
conda create --name flask_env python=3.9.7
pip install -r requirements.txt
```

3. Activate venv and run the server.
```bash
# Conda activate venv
conda activate flask_env
flask run --cert=adhoc #to make sure the app running using https protocol
```

#Method Two using Docker
1. Clone this repository.
```bash
# Clone this repo
git clone https://github.com/mkleong96/flask_todo_list_app
cd flask_todo_list_app
```

2. Build using Docker Compose
```bash
docker-compose up
```

## Instruction for running the app
1. To login to the app
```bash
curl -k https://127.0.0.1:5000/login/github
```
![image](https://user-images.githubusercontent.com/81457132/184542033-927b39bc-7c48-40e6-b74f-7988e744925a.png)
Then, copy the link and open in browser to login
![image](https://user-images.githubusercontent.com/81457132/184542712-314e660a-bae1-4560-b59c-edbc9f60d07d.png)



2. To Show the all To-Do List added
```bash
curl -k https://127.0.0.1:5000/list_all
```
Example output:
![image](https://user-images.githubusercontent.com/81457132/184542378-df52ede2-63d8-446f-b84f-931832cc07d9.png)


3. To Add New To-Do List
```bash
curl -k -H "Content-Type: application/json" -X POST -d "{\"title\":\"Read a book\", \"description\":\"Read a book on Monday\", \"status\":\"not complete\"  }" https://127.0.0.1:5000/add_to_do_list
```
Example output:
![image](https://user-images.githubusercontent.com/81457132/184542427-b59db58f-bcbd-4e78-88e0-6783bba727ce.png)


4. To Delete a To-Do List
```bash
curl -k -H "Content-Type: application/json" -X POST -d "{\"id\":\"3\"}" https://127.0.0.1:5000/delete_list
```
Example output:
![image](https://user-images.githubusercontent.com/81457132/184542466-5631df10-eb9b-4198-b49f-ba6ddb0caa22.png)


5. To Mark a To-Do List Complete
```bash
curl -k -H "Content-Type: application/json" -X POST -d "{\"id\":\"3\" ,\"status\":\"done\"}" https://127.0.0.1:5000/mark_list_done
```
Example output:
![image](https://user-images.githubusercontent.com/81457132/184542504-39a71b01-ff22-4a0a-99ce-19fccaf838e6.png)

## Interface documentation.


