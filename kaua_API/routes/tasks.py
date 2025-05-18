from fastapi import APIRouter, HTTPException, status
from app.models import TaskModel, TaskResponse
from app.database import task_collection
from bson import ObjectId

router = APIRouter()

# Utilitário para converter ObjectId em string
def task_helper(task) -> dict:
    return {
        "id": str(task["_id"]),
        "title": task["title"],
        "description": task["description"]
    }

@router.get("/", response_model=list[TaskResponse])
async def list_tasks():
    tasks_cursor = task_collection.find()
    tasks = []
    async for task in tasks_cursor:
        tasks.append(task_helper(task))
    return tasks

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskModel):
    new_task = task.dict()
    result = await task_collection.insert_one(new_task)
    new_task["_id"] = result.inserted_id
    return task_helper(new_task)

@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(task_id: str):
    task = await task_collection.find_one({"_id": ObjectId(task_id)})
    if task:
        return task_helper(task)
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(task_id: str, updated_task: TaskModel):
    result = await task_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": updated_task.dict()}
    )
    if result.modified_count == 1:
        task = await task_collection.find_one({"_id": ObjectId(task_id)})
        return task_helper(task)
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: str):
    result = await task_collection.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
