from typing import Union

from fastapi import FastAPI
import time
import random

app = FastAPI()
N = 10 **4

@app.get("/")
def read_root():
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]

    result = []
    for x, y in zip(a, b): 
        result.append(x+y)
        
    return {"Hello": result}


@app.get("/two-dimensional-array")
def two_dimensional_array():
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    b = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[i])):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return {"result": result}

@app.get("/two-one-array")
def two_one_array():
    start_time = time.time()
    arr1 = [random.random() for _ in range(1000000)]
    arr2 = [random.random() for _ in range(1000000)]
    end_time = time.time()
    create_time = end_time - start_time

    start_time = time.time()
    result = [a + b for a, b in zip(arr1, arr2)]
    end_time = time.time()
    cal_time = end_time - start_time
    return {"result1": create_time, "result2": cal_time}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
    

# def add_large_arrays():
#     N = 10**6
    
#     start_creation_time = time.time()
#     a = [random.choices(random.randint(0, 100) for _ in range(N))]
#     b = [random.choices(random.randint(0, 100) for _ in range(N))]
#     end_creation_time = time.time()
    
#     start_cal_time = time.time()
#     result = []
#     for x, y in zip(a, b):
#         result.append(x + y)
#     end_cal_time = time.time()
    
#     return {"create_time": end_creation_time - start_creation_time,
#              "cal_time": end_cal_time - start_cal_time}
    

@app.get("/add-large-arrays")
def add_large_arrays():
    array_creation_time, addition_time = add_arrays(generate_random_array_with_randint, N)
    return{
        "array_creation_time": array_creation_time,
        "addition_time": addition_time
    }




def add_arrays(generate_random_array, N = 10 **6):
    start_creation_time = time.time()
    a = generate_random_array(N)
    b = generate_random_array(N)
    end_creation_time = time.time()
    
    start_cal_time = time.time()
    result = [x + y for x, y in zip(a, b)]
    end_cal_time = time.time()
    
    array_creation_time = end_creation_time - start_creation_time
    addition_time = end_cal_time - start_cal_time
    return array_creation_time, addition_time
    
    
def generate_random_array_with_randint(N):
    a = [random.randint(0, 100) for _ in range(N)]
    return a
    
def generate_random_array_with_choices(N):
    a = [random.choices(range(101), k=N)]
    return a