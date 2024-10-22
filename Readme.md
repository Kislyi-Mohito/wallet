pip freeze > requirements.txt
pip install -r requirements.txt

нужно создать файл .gitignore это нужно что git игнорировал все папки что в этом файле
----Пример------
.idea
venv
__pycache__
----------------------------------------------------------------------------------------
создаем локальный репозиторий 
git init
теперь работ с гит хаб
git remote add origin https://github.com/Kislyi-Mohito/wallet.git соединнение репозитория
git push -u origin master надо каждый раз пушить после __комита__

----------------------------------------
если новая система
надо установить chockolatie
в win power shell

Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
choco install git
чтоб скопировать приложение на ноут 
git clone __ссылка на приложение в гитхаб__
___________________________________________
чтоб подттянуть изменения с другого ноутбука комагда
git pull
---------------------------------------------------