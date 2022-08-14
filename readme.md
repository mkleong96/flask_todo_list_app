## Introduction for running the app
1. Clone this repository.
2. cd to the directory where run.py located.



# To login to the app
curl -k https://127.0.0.1:5000/login/github

#To show the to-do list added
curl -k https://127.0.0.1:5000/list_all

#To add new to-do list
curl -k -i -H "Content-Type: application/json" -X POST -d "{\"title\":\"Read a book\", \"description\":\"Read a book on Monday\", \"status\":\"not complete\"  }" https://127.0.0.1:5000/add_to_do_list

#To delete a to-do list
curl -k -H "Content-Type: application/json" -X POST -d "{\"id\":\"3\"}" https://127.0.0.1:5000/delete_list

#To mark a to-do list done
curl -k -H "Content-Type: application/json" -X POST -d "{\"id\":\"3\" ,\"status\":\"done\"}" https://127.0.0.1:5000/mark_list_done

flask run --cert=adhoc
