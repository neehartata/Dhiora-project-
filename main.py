from fastapi import FastAPI
from data import Details
from fastapi import HTTPException

app=FastAPI()

# GET /: Welcome message.
@app.get("/")
def greeting():
    return f"Welcome to card management system"

card_details = [
    Details(
        legacy_id=101,
        name="Rahul Sharma",
        age=30,
        aadhar="123456789012",
        card_type="Gold",
        status="Active"
    ),
    Details(
        legacy_id=102,
        name="Anita Verma",
        age=28,
        aadhar="987654321098",
        card_type="Silver",
        status="Inactive"
    ),
    Details(
        legacy_id=103,
        name="Amit Patel",
        age=35,
        aadhar="456789123456",
        card_type="Platinum",
        status="Active"
    ),
]

# GET /details: List all records.
@app.get("/get_details")
def get_details():
    return card_details

# POST /details: Add a new record.
@app.post("/add_details")
def add_details(details:Details):
    for cards in card_details:
        if cards.legacy_id==details.legacy_id:
            raise HTTPException(status_code=404, detail="Legacy ID already exists")
    card_details.append(details)
    return details
    

# PUT /details/{id}: Update a record by Legacy ID.

@app.put("/update_details/{legacy_id}")
def update_details(legacy_id:int,details:Details):
    for i in range(len(card_details)):
        if card_details[i].legacy_id==legacy_id:
            card_details[i]=details
            return "Successfully updated the record"
    raise HTTPException(status_code=404, detail="Legacy ID does not exists")


# DELETE /details/{id}: Remove a record by Legacy ID.

@app.delete("/delete_details/{legacy_id}")
def delete(legacy_id:int):
    for i in range(len(card_details)):
        if card_details[i].legacy_id==legacy_id:
            card_details.pop(i)
            return "Successfully deleted the record"
    raise HTTPException(status_code=404, detail="Legacy ID does not exists")


# Validation: Return a 404 error if the ID doesn't exist during an update or delete.