# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 17:28:25 2021

@author: User
"""
person = 5
cook_book =[
           [ 'calad',[
            
            ['картофель', 100,'гр'],
            ['морковь', 50,'гр'],
            ['огурцы', 50,'гр'],
            ['горошек', 30,'гр'],
            ['майонез', 70,'гр'],
            
            ],],
    
            ['пица', 
            
             [
            ['сыр', 50,'гр'],
            ['товаты', 50,'гр'],
            ['тесто', 100,'гр'],
            ['бекон', 30, 'гр'],
            ['колбаса', 30,'гр'],
            ['грибы', 20,'гр']
            
            ]
            ]]       


for dish, item  in cook_book:
    print ( dish.capitalize())
    for size in item:
        print (size[-3], size[-2]*person, size [2])

  


 
        
        
        