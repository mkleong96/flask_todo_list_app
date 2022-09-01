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
# Clone this repo and cd to the directory
git clone https://github.com/mkleong96/flask_todo_list_app
cd flask_todo_list_app
```

2. Important: Make sure Docker is running!

3. Build using Docker-Compose 
```bash
docker-compose build
```
4. Run the app using Docker-Compose Up
```bash
docker-compose up
```

![image](https://user-images.githubusercontent.com/81457132/184544779-eb946b46-638a-4e7d-af22-df528c0b159a.png)


## Instruction for running the app
1. To login to the app
```bash
curl -k https://127.0.0.1:5000/login/github
```
![image](https://user-images.githubusercontent.com/81457132/184542033-927b39bc-7c48-40e6-b74f-7988e744925a.png)
Then, copy the link and open in browser to login

![image](https://user-images.githubusercontent.com/81457132/184544349-8fdea432-0456-491b-8875-ad600259efaf.png)

![image](https://user-images.githubusercontent.com/81457132/184561985-fe46affc-1420-4d7a-98fd-0ed6bbd59a02.png)

![image](https://user-images.githubusercontent.com/81457132/187874984-19a9c4df-3c5a-4c90-855a-e29153e1ec9d.png)


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

6. To upload a Image
```bash
curl -k -F file=@/filepath/ https://127.0.0.1:5000/add_img
```

Final list after adding/remove/update:
![image](https://user-images.githubusercontent.com/81457132/184543110-85e67e86-65ad-46c7-b6d7-0d2d832e6e26.png)

## Interface documentation.
1. API for Login with GitHub Account.

![image](https://user-images.githubusercontent.com/81457132/184544447-abd3306e-c4c7-4071-b4fd-f78c0121b0e6.png)

2. API for checking authentication.

![image](https://user-images.githubusercontent.com/81457132/184544465-5b01ec21-f662-47e6-b966-40f7ba00624c.png)

3. API for list all To-Do-List.

![image](https://user-images.githubusercontent.com/81457132/184544477-ed0ab5c3-7ca0-4608-a109-c8d8dc4a4d8e.png)

4. API for adding a new To-Do-List.

![image](https://user-images.githubusercontent.com/81457132/184544495-61c7d9f4-fd62-4f13-8d38-837a8aba4002.png)

5. API for delete a To-Do-List.

![image](https://user-images.githubusercontent.com/81457132/184544506-043e8d72-274f-471d-a5a5-15c2fbed7f16.png)

6. API for marking a To-Do-List complete.

![image](https://user-images.githubusercontent.com/81457132/184544534-8129d661-6ea1-4023-8abb-59381c4eb561.png)


