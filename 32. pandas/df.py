import pandas as pd 

employee = {
    'id': [1,2,3,4,5,6,7,8,9], 
    'names': ['a' ,'b' ,'c' ,'d' ,'e' ,'f' ,'g' ,'h' ,'i'], 
    
}



emp = pd.DataFrame(employee); 
emp.loc[0, 'names']
print(emp)


ser = ['ahmad' , 'khalil' , 'mahmood', 'kazim']



