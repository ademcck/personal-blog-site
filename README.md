# Personal Blog

### Home Page
![Screenshot 1](https://drive.google.com/file/d/1Wv7wmZdv4lhLIqoyJhdUmJK6SWEn3mRX/view?usp=sharing)

### Account Page
![Screenshot 2](https://drive.google.com/file/d/1USE3LhzwVfdVFnbwguoKNgiFpYSwYU_w/view?usp=sharing)

### Public Account Page
![Screenshot 3](https://drive.google.com/file/d/1MQVSYSfjDixBYGzeAs8qkBMW9Ht9SePK/view?usp=sharing)





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
