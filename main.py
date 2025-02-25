from typing import Union

from fastapi import FastAPI
import time
import random

app = FastAPI()


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

