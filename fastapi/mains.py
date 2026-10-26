from fastapi import FastAPI , HTTPException , Path
import json

app = FastAPI()



@app.get("/view")
def load_data():
    try:
        with open("myfile.json", "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="myfile.json file not found!" )
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="JSON format is wrong!")



@app.get("/")
def hello():
    return {"message" : "Data of Employee Working in Company! "}

@app.get("/About")
def About():
    return {"My_New_Message" , "Gather Data of all Employee Working in Company...."}





@app.get("/myfile/{employee_id}")
def employee_view(employee_id: str = Path(... , desc = "Enter the employee id in Required Field..." , example="emp1 , emp2 and so on...." , min_length= 1 , max_length=100 , description="Enter the ID of Employee in given format..." )):
    data = load_data()
    if employee_id in data:
        return data[employee_id]
    if employee_id not in data:
        raise HTTPException(status_code= 404 , detail="Employee not found..." , )



@app.put("/")

def My_Hello():
    return {"message" : "Hello Hisaan How are you! "}
