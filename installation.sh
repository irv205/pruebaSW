#!/bin/bash

echo ""
echo "Welcome..."
echo "This is my Django example"

#Buscando el .env
ENVFILE="./.env"

#Verificando si existe, en caso de que no, generarlo den .env.example
if [ ! -f "$ENVFILE" ]; then
  echo "File not found!"
  cp -v .env.example .env
fi

if [ -f "$ENVFILE" ];
then

  #Configurar el .env
  echo "Add basic config in .env"
  read -p "You want to activate debug mode [default True]: " debug
  if [[($debug=="")]];
  then 
    DEBUG=True
  
  else
    DEBUG=False
  fi

  SECRET_KEY=$(openssl rand -base64 32)
  echo "Secret key: ${SECRET_KEY}"

  read -p "App name [default MyApplication]: " appname
  if [[($appname=="")]];
  then 
    APP_NAME="MyApplication"
  else
    APP_NAME=$appname
  fi

  read -p "Website url [default http://127.0.0.1:8000]: " web_url
  if [[($web_url=="")]];
  then
    WEBSITE_URL="http://127.0.0.1:8000"
  else 
    WEBSITE_URL=$web_url
  fi
  
  read -p "Website url [default http://127.0.0.1:8000]: " server_url
  if [[($server_url=="")]];
  then
    SERVER_URL="http://127.0.0.1:8000"
  else 
    SERVER_URL=$server_url
  fi

  read -p "Time zone [default UTC]: " timezone
  if [[($timezone=="")]];
  then
    TIME_ZONE="UTC"
  else
    TIME_ZONE=$timezone
  fi

  read -p "Pagination [default 10]: " pagination
  if [[($pagination == "")]];
  then
    PAGINATION="10"
  else
    PAGINATION=$pagination
  fi


  read -p "Database HOST [default localhost]: " db_host
  if [[($db_host=="")]];
  then
    DB_HOST="localhost"
  else
    DB_HOST=$db_host
  fi

  read -p "Database NAME [default empty]: " db_name
  if [[($db_name=="")]];
  then
    DB_NAME=""
  else
    DB_NAME=$db_name
  fi

  read -p "Database USER [default postgres]: " db_owner
  if [[($db_owner=="")]];
  then
    DB_OWNER="postgres"
  else
    DB_OWNER=$db_owner
  fi

  read -p "Database PASSWORD [default empty]: " db_password
  if [[($db_password=="")]];
  then
    DB_PASSWORD=""
  else
    DB_PASSWORD=$db_password
  fi

  read -p "Database PORT [default 5432]: " db_port
  if [[($db_port=="")]];
  then
    DB_PORT="5432"
  else
    DB_PORT=$db_port
  fi

  read -p "Email [default example@example.com]: " email
  if [[($email=="")]];
  then
    EMAIL="example@example.com"
  else
    EMAIL=$email
  fi

  read -p "Email HOST [smtp.gmail.com]: " email_host
  if [[($email_host=="")]];
  then
    EMAIL_HOST="smtp.gmail.com"
  else
    EMAIL_HOST=$email_host
  fi

  read -p "Email User [example@example.com]: " email_user
  if [[($email_user=="")]];
  then
    EMAIL_USER="example@example.com"
  else
    EMAIL_USER=$email_user
  fi

  read -p "Email Password [12345678]: " email_password
  if [[($email_password=="")]];
  then
    EMAIL_PASSWORD="12345678"
  else
    EMAIL_PASSWORD=$email_password
  fi

  echo "DEBUG=$DEBUG" > "$ENVFILE"
  echo "SECRET_KEY=${SECRET_KEY}" >> "$ENVFILE"
  echo "APP_NAME=${APP_NAME}" >> "$ENVFILE"
  echo "WEBSITE_URL=${WEBSITE_URL}" >> "$ENVFILE"
  echo "SERVER_URL=${SERVER_URL}" >> "$ENVFILE"
  echo "TIME_ZONE=${TIME_ZONE}" >> "$ENVFILE"
  echo "DB_HOST=${DB_HOST}" >> "$ENVFILE"
  echo "DB_NAME=${DB_NAME}" >> "$ENVFILE"
  echo "DB_OWNER=${DB_OWNER}" >> "$ENVFILE"
  echo "DB_PASSWORD=${DB_PASSWORD}" >> "$ENVFILE"
  echo "DB_PORT=${DB_PORT}" >> "$ENVFILE"
  echo "EMAIL_USE_TLS=True" >> "$ENVFILE"
  echo "EMAIL=${EMAIL}" >> "$ENVFILE"
  echo "EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend" >> "$ENVFILE"
  echo "EMAIL_HOST=${EMAIL_HOST}" >> "$ENVFILE"
  echo "EMAIL_USER=${EMAIL_USER}" >> "$ENVFILE"
  echo "EMAIL_PASSWORD=${EMAIL_PASSWORD}" >> "$ENVFILE"
  echo "EMAIL_PORT=587" >> "$ENVFILE"
  echo "PAGINATION=${PAGINATION}" >> "$ENVFILE"
fi

#Entorno virtual
ENVIRONMENT="./venv"

if [ ! -d "$ENVIRONMENT" ];
then
  echo "-"
  read -p "Creating virtual environment and install requirements? (y/n): " create

  if [[($create == "y")]];
  then
    echo "Creating virtual environment"
    python3 -m venv venv
    echo "virtual environment created"
    source venv/bin/activate
    echo "Virtual environment active"

    echo "Install requirements"
    pip install -r requirements.txt
  fi

  read -p "Run command collectstatic? (y/n): " collectstatic
  if [[($collectstatic == "y")]];
  then
    echo "Creating static files"
    python manage.py collectstatic
  fi

fi

echo "-------------"
echo "Complete, Welcome to Django"
echo "-------------"

exit 404

__ARCHIVE__
