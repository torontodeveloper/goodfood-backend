from fastapi import FastAPI
from routers.recipes import all_recipes,heat_eat,family,value
from routers.price_plans import price_plans

app = FastAPI()



@app.get('/all_recipes')
def get_all_recipes():
    '''
    Return all the recepies
    '''
    return all_recipes

@app.get('/heat_eat')
def get_heat_eat():
    '''
    Return Heat and eat recipes
    '''
    return heat_eat


@app.get('/price_plans')
def get_price_plans():
    '''
    Return the price plans
    '''
    return price_plans

@app.get('/family_plan')
def get_family_plan():
    '''
    Return the Family Plan
    '''
    return family

@app.get('/value')
def get_value():
    '''
    Return the Value Plan
    '''
    return family