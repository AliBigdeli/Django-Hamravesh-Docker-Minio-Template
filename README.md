<div align="center">
<img loading="lazy" style="width:700px" src="./docs/hamravesh-banner.png">
<h1 align="center">Django3.2 Hamravesh Template</h1>
<h3 align="center">Sample Project to use hamravesh service provider for django app</h3>
</div>
<p align="center">
<a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://www.djangoproject.com/" target="_blank"> <img src="https://user-images.githubusercontent.com/29748439/177030588-a1916efd-384b-439a-9b30-24dd24dd48b6.png" alt="django" width="60" height="40"/> </a> 
<a href="https://www.docker.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a>
<a href="https://www.postgresql.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a>
<a href="https://www.nginx.com" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nginx/nginx-original.svg" alt="nginx" width="40" height="40"/> </a>
<a href="https://git-scm.com/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a>
<a href="https://hamravesh.com/" target="_blank"> <img src="https://avatars.githubusercontent.com/u/24360374?s=200&v=4" alt="git" width="40" height="40"/> </a>
</p>

# Guideline
- [Guideline](#guideline)
- [Goal](#goal)
- [Video Instructions](#video-instructions)
- [Development usage](#development-usage)
  - [Clone the repo](#clone-the-repo)
  - [Enviroment Varibales](#enviroment-varibales)
  - [Build everything](#build-everything)
  - [Note](#note)
  - [Check it out in a browser](#check-it-out-in-a-browser)
- [Testing Usage](#testing-usage)
  - [running all tests](#running-all-tests)
- [Hamravesh deployment](#hamravesh-deployment)
  - [0- Create an account](#0--create-an-account)
  - [1- Create a repo app](#1--create-a-repo-app)
  - [2- Setup database](#2--setup-database)
  - [3- Setup django app](#3--setup-django-app)
    - [1- General info](#1--general-info)
    - [2- Environment Variables](#2--environment-variables)
    - [3- Domain Address](#3--domain-address)
    - [4- Pick a plan](#4--pick-a-plan)
    - [5- wait until its deployed](#5--wait-until-its-deployed)
- [CICD Deployment](#cicd-deployment)
  - [Github CICD](#github-cicd)
  - [Gitlab/Hamgit CICD](#gitlabhamgit-cicd)
- [Sentry Logger](#sentry-logger)
  - [0- Create an account](#0--create-an-account-1)
  - [1- Create Project](#1--create-project)
  - [2- Implement configs](#2--implement-configs)
  - [3- Throw an Error](#3--throw-an-error)
  - [4- Test logging mechanism](#4--test-logging-mechanism)
- [License](#license)
- [Bugs](#bugs)

# Goal
This project main goal is to provide a simple way to deploy a django project into hamravesh service provider.

# Video Instructions
<div align="center" ><img loading="lazy" style="width:700px" src="./docs/video.png"></div>

# Development usage
You'll need to have [Docker installed](https://docs.docker.com/get-docker/).
It's available on Windows, macOS and most distros of Linux. 

If you're using Windows, it will be expected that you're following along inside
of [WSL or WSL
2](https://nickjanetakis.com/blog/a-linux-dev-environment-on-windows-with-wsl-2-docker-desktop-and-more).

That's because we're going to be running shell commands. You can always modify
these commands for PowerShell if you want.


## Clone the repo
Clone this repo anywhere you want and move into the directory:
```bash
git clone https://github.com/AliBigdeli/Django-Hamravesh-Docker-Template.git
```

## Enviroment Varibales
enviroment varibales are included in docker-compose.yml file for debugging mode and you are free to change commands inside:

```yaml
services:
  backend:
    command: sh -c "python manage.py check_database && \ 
                    yes | python manage.py makemigrations  && \
                    yes | python manage.py migrate  && \
                    python manage.py runserver 0.0.0.0:8000"
    environment:      
      - DEBUG=True
```

## Build everything

*The first time you run this it's going to take 5-10 minutes depending on your
internet connection speed and computer's hardware specs. That's because it's
going to download a few Docker images and build the Python + requirements dependencies.*

```bash
docker compose up --build
```

Now that everything is built and running we can treat it like any other Django
app.

## Note

If you receive an error about a port being in use? Chances are it's because
something on your machine is already running on port 8000. then you have to change the docker-compose.yml file according to your needs.
## Check it out in a browser

Visit <http://localhost:8000> in your favorite browser.

# Testing Usage
## running all tests
```bash
docker compose run --rm backend sh -c " black -l 79 && flake8 && python manage.py test" -v core:/app
```
or
```bash
docker compose exec backend sh -c sh -c " black -l 79 && flake8 && python manage.py test" 
```

# Hamravesh deployment

## 0- Create an account
in order to deploy your project inside hamravesh first you need to create an account. so please go to the following url and create your account.

<https://console.hamravesh.com/signup>

after that you need to sign in to your console panel. which is going to be like this.
<div align="center" ><img loading="lazy" style="width:700px" src="./docs/hamravesh-console.png"></div>

## 1- Create a repo app
in order to deploy your project you can use repo mode (or منبع گیت) after clicking on the item. you will see a panel like this below:

<div align="center" ><img loading="lazy" style="width:700px" src="./docs/hamravesh-repo-step1.png"></div>

as you can see you have to provide your github/gitlab/hamgit repo address for deployment. 
in our case the configuration will be as follow:

``` properties
repo_address: https://github.com/AliBigdeli/Django-Hamravesh-Docker-Template.git
# if you are just testing without cicd use main or if you want to use cicd script to delpoy create a prod branch and then add it here
branch_name: main
build_context: .
docker_file_address: ./dockerfiles/prod/django/Dockerfile
```
Note: as we are going to implement ci/cd and other stuffs we avoid auto deployment or even uploading file.

after your done with the inputs just click on (تنظیمات اپ) and go for next step.

## 2- Setup database
follow the provided steps to finish this section.



surely you are going to need a postgres database for your deployment so all you have to do is to create a postgres app first.
in the app section click on the PostgreSQL database.

<div align="center" ><img loading="lazy" style="width:700px" src="./docs/hamravesh-repo-step0-1.png"></div>

then in the next window pick a name for the database service name.

<div align="center" ><img loading="lazy" style="width:700px" src="./docs/hamravesh-repo-step0-2.png"></div>

Note: in our case we dont need to access the database through the internet.

after that just choose a plan for it and create the database instance.
<div align="center" ><img loading="lazy" style="width:700px" src="./docs/hamravesh-repo-step0-3.png"></div>

now that your database is created you can use it for connecting other apps to it.
<div align="center" ><img loading="lazy" style="width:700px" src="./docs/hamravesh-repo-step0-4.png"></div>

the provided database credentials and url are as follows:
``` properties
PGDB_address: my-site-postgre.bigdeliali3.svc:5432
PGDB_username: postgres
PGDB_password: ddGrZM7u3BsduXm5ph3WzPYlMWSMTXbu
```
Note: if you dont want to use the default database by the name of postgres,
you just have to head to the terminal tab and create a another database for your project you can call it anything you want.

<div align="center" ><img loading="lazy" style="width:700px" src="./docs/hamravesh-repo-step0-5.png"></div>

```shell
psql -U postgres -c "create database <PGDB_name>"
```




## 3- Setup django app
follow the provided steps to finish this section.

### 1- General info
<div align="center" ><img loading="lazy" style="width:700px" src="./docs/hamravesh-repo-step2-1.png"></div>

in this page you have to provide general information's about the app you are about to create, which in my case are as follows:

```properties
app_name: my-site # name of the app which is going to be called inside the portal
service_port: 8000 # which is based on the gunicorn port
execute_command: gunicorn --bind 0.0.0.0:8000 core.wsgi:application
```
Note: provided information is just enough to run our program for more details please visit this url 
<https://docs.hamravesh.com/darkube/create/git-repo/settings/general/>

### 2- Environment Variables
<div align="center" ><img loading="lazy" style="width:700px" src="./docs/hamravesh-repo-step2-2.png"></div>

in this section you have to provide the environment variables which are going to be used in the project. you can switch to editor and pase our template that is placed in /envs/prod/.env.sample

Note: provided information is just enough to run our program for more details please visit this url <https://docs.hamravesh.com/darkube/create/git-repo/settings/envs/>

### 3- Domain Address
<div align="center" ><img loading="lazy" style="width:700px" src="./docs/hamravesh-repo-step2-3.png"></div>

pick a name for you app which is going to be accessed through the web and for better security please enable https redirect.
keep in mind that you can give a different dns name through a provider like arvan or cloudflare.(we will provide more details for this matter later)

Note: provided information is just enough to run our program for more details please visit this url <https://docs.hamravesh.com/darkube/create/git-repo/settings/domain-address/>


### 4- Pick a plan 
<div align="center" ><img loading="lazy" style="width:700px" src="./docs/hamravesh-repo-step3-1.png"></div>

for launching purposes you have to pick a plan for resources. based on the scale and traffic of your project you have to pick one.

Note: at the moment we are not using disks and we are just using the static files being served by the Whitenoise.

### 5- wait until its deployed
<div align="center" ><img loading="lazy" style="width:700px" src="./docs/hamravesh-repo-step4-1.png"></div>

now all you have to do is to wait util the project is fully deployed.

after its done you can access the website through the url you picked in stage 3 of the setup.


# CICD Deployment
For the sake of continuous integration and deployment i have provided two samples for github and gitlab/hamgit for you.
but there will be some configurations to be added for building and deploying purposes.

## Github CICD
will be provided soon

## Gitlab/Hamgit CICD
in order to do ci/cd in the sample project for gitlab/hamgit you have to create a duplicate of the ```.gitlab-ci.yml.sample``` but with different name as ```.gitlab-ci.yml``` in the root directory.

after that our pipeline will be always listening to the prod branch. if you commit in this branch it will go through the process.


note that you have to declare 5 or more environment variables in your gitlab/hamgit project repo, which you can add it by going to ```Settings>CI/CD>Variables```, and in this section try to add all the needed variables.

<div align="center" ><img loading="lazy" style="width:700px" src="./docs/gitlab-envs.png"></div>

these variables should be included:
- DARKUBE_APP_ID - ``` which can be found in app info page ```
- DARKUBE_DEPLOY_TOKEN - ``` which can be found in app info page ```
- IMAGE -  ``` registry.hamdocker.ir/<USERNAME>/<APPNAME> ```
- REGISTERY - ``` registry.hamdocker.ir/<USERNAME> ```
- REGISTERY_PASSWORD - ``` registry password ```
- REGISTERY_USER - ``` username like 'bigdeliali3' ```


for having ```DARKUBE_APP_ID``` and ```DARKUB_DEPLOY_TOKEN``` head to the app page and use the following parameters in the picture.

<div align="center" ><img loading="lazy" style="width:700px" src="./docs/hamravesh-app-info.png"></div>
 
for having ```REGISTRY``` and ```REGISTRY_USER``` and ```REGISTRY_PASSWORD``` head to the app page and use the following parameters in the picture.
REGISTRY will be the url like this: ```registry.hamdocker.ir/<USERNAME>```
and for getting the username and passwords just go to the app section and click on docker image. you will see something like this, after that click on registries.
<div align="center" ><img loading="lazy" style="width:700px" src="./docs/docker-app.png"></div>

On top of the page you can find the credentials for registry that you need.
<div align="center" ><img loading="lazy" style="width:700px" src="./docs/docker-registry.png"></div>
after that if everything goes well you can see that the jobs are working.

# Sentry Logger
if you need to use sentry logging as a logger for your project all you need to do is to have an account and do modifications in environments cause i have already added the scripts that you need.

## 0- Create an account
first of all head to the link below and follow instructions to create an account. until you see the dashboard.
<https://sentry.hamravesh.com/>
<div align="center" ><img loading="lazy" style="width:700px" src="./docs/sentry-dashboard-step-0.png"></div>

## 1- Create Project
Now in order to connect your django application to the sentry you have to create a project. so click on creating project and then choose django as your project base, in Setup your default alert settings you can create the alerts you need or you can do it later, and at the end of config just choose a name and select a team and hit Create Project when your done.
<div align="center" ><img loading="lazy" style="width:700px" src="./docs/sentry-dashboard-step-1.png"></div>

## 2- Implement configs
for ease of use i have already added the scripts plus the requirements that you need for your project as below:

- requirements.txt
  ```bash
  ...
  sentry-sdk
  ```
- core/core/settings.py
  ```python
  SENTRY_ENABLE = config("SENTRY_ENABLE", cast=bool, default=False)
  if SENTRY_ENABLE:
    SENTRY_DNS = config("SENTRY_DNS")
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=SENTRY_DNS,
        integrations=[
            DjangoIntegration(),
        ],

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True
    )
  ```
- envs/prod/django/.env.sample
  ```properties
  SENTRY_ENABLE=True
  SENTRY_DNS=https://xxxx@sentry.hamravesh.com/xxx
  ```
as you can see all you have to do is to enable the sentry with putting env in ```True``` and replace the ```dns``` with the correct url.

## 3- Throw an Error
for testing purposes i already had put a url inside project to create an error to log it inside the sentry for checking the configuration you can uncomment it again after test.

- core/core/urls.py
  ```python
  from django.urls import path

  def trigger_error(request):
      division_by_zero = 1 / 0

  urlpatterns = [
      path('sentry-debug/', trigger_error),
      # ...
  ]
  ```
## 4- Test logging mechanism
now just head to the url that we have as ```https://app_name.darkube.app/sentry-debug/``` nd create a purposely error. then inside the project page you can see the log of error which happened in your project to get a 500 error.
<div align="center" ><img loading="lazy" style="width:700px" src="./docs/sentry-dashboard-step-4-1.png"></div>
then head to the dashboard and inside project page you can see an issue
<div align="center" ><img loading="lazy" style="width:700px" src="./docs/sentry-dashboard-step-4-2.png"></div>
# License
MIT.


# Bugs
Feel free to let me know if something needs to be fixed. or even any features seems to be needed in this repo.
