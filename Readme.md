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
