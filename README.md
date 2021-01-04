<h1 align="center">
<br>
Recycle
</h1>

<p align="center">Projeto de extensão em python</p>
<br>


> Plano de Trabalho de Extensão na modalidade de Grupo de Alunos Voluntários de Extensão (GAVE), intitulado “Sistemas de Informação que auxiliam na autonomia e na sustentabilidade econômica e social de comunidades em estado de vulnerabilidade” sob orientação do Prof. Dr. Fernando Ernesto Kintschner.



## DB Setup
- Download and install MySQL (https://dev.mysql.com/downloads/workbench/)
- Download and install XAMPP (https://www.apachefriends.org/pt_br/index.html)
- Open Xampp
- Start MySQL option

## Project Setup
- Download and install Python (https://www.python.org/downloads/windows/)
- Clone the application
- Go to `master` branch
- Run `python -m pip install pip`
- Run `pip install virtualenv`
- Run `virtualenv venv`
- Run `. venv/bin/activate`
- Run `pip install -r requirements.txt`
- Run `python manage.py makemigrations`
- Run `python manage.py migrate`
- Run `python manage.py runserver`


## Branching
Create new branch based on `master`: 
- Go `master` branch
- Run `git pull origin master`
- Run `git checkout -b <branch_name>` (branch name should be equal task id example: name of the developer)

## Development
Run `python manage.py runserver` for a dev server. The app will automatically open on `http://127.0.0.1:8000/`.If you change any of the source files it will reload automatically as well.

#### Code scaffolding
Run `django-admin startapp <app_name>` to generate a new app.

##  Push your code and make a pull request
Before push you code, make sure you are up to date with development branch:
- `git commit -am "<comment>"`
- Run `git pull origin master`
- If has conflicts file, fix it and make a `commit` again
- Run `git push origin -u <branch_name>`
- Open a pull request on repository website
