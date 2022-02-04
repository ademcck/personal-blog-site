# Personal Blog Site

> installation steps
 - install virtualenv and use like below
    * go to your downloaded blog project
   ```bash
    ┌──(ademcck㉿kali)-[~]
    └─$ virtualenv venv
   ```
 - then, activate your created virtualenv
  ```bash
    ┌──(ademcck㉿kali)-[~]
    └─$ source venv/bin/activate

  ```
 - after this point, install all python module from the requirements.txt file
  ```bash
      ┌──(ademcck㉿kali)-[~]
      └─$ pip install -r requirements.txt

  ```
 - for now, everything is installed. Don't forget to install ckeditor
 - as a finally setting. In this /blog/settings/ path, Modify the production.py and base.py files according to you.
 - and finally
  ```bash
     ┌──(ademcck㉿kali)-[~]
     └─$ python manage.py makemigrations
     .
     .
     ┌──(ademcck㉿kali)-[~]
     └─$ python manage.py migrate

  ``` 
  
### **  _this blog site uses the postgresql database._ 
