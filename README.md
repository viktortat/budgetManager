# DjangoAndVueBoilerplate
This is boilerplate for Vue and Django SPA app.

## How to use:
1. Create folder for your project and open it
```
mkdir myproject
cd myproject
```
2. Clone this repo
```
git clone https://github.com/panzelva/DjangoAndVueBoilerplate.git .
```
3. Create virtual enviroment for python.
```
virtualenv venv
```
4. Activate virtual enviroment
```
.\venv\Scripts\activate
```
5. Install requirements and run Django server
```
cd backend
pip install -r requirements.txt
python manage.py runserver
```
6. Install node_modules (you must open new terminal)
```
cd ..
cd frontend
npm install
```
7. Run Vue server
```
npm run serve
```
8. Profit!