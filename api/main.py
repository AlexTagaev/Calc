# импорт библиотек
from fastapi import FastAPI     # библиотека FastAPI
from pydantic import BaseModel  # модуль для объявления структуры данных

# создаем объект приложения FastAPI
app = FastAPI()
   
# класс параметров калькулятора
class ModelCalc(BaseModel):
    a: float
    b: float        

# класс с типами данных для метода api/get_answer
class ModelAnswer(BaseModel):
    text: str    

# функция, которая будет обрабатывать запрос по пути "/"
# полный путь запроса http://127.0.0.1:8000/
@app.get("/")
def root(): 
    return {"message": "Hello FastAPI"}

# функция, которая обрабатывает запрос по пути "/about"
@app.get("/about")
def about():
    return {"message": "Страница API калькулятора"}

# функция-обработчик post запроса с параметрами
@app.post('/summ')
def post_summ(data:ModelCalc):
    result = data.a + data.b
    return {'result': result}

@app.post('/diff')
def post_diff(data: ModelCalc):
    result = data.a - data.b
    return {'result': result}

@app.post('/mltpl')
def post_mltpl(data: ModelCalc):
    result = data.a * data.b
    return {'result': result}

@app.post('/div')
def post_div(data: ModelCalc):
    result = data.a / data.b
    return {'result': result}