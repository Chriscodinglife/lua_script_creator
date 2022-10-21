from app.models import Project, ScreenNames, Screen, ProjectItems
from fastapi import FastAPI, status, Form
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

app = FastAPI()

project_pydantic = pydantic_model_creator(Project)
screen_pydantic = pydantic_model_creator(Screen)
screen_pydantic_list = pydantic_queryset_creator(Screen)
project_items_pydantic = pydantic_model_creator(ProjectItems)
project_items_pydantic_list = pydantic_queryset_creator(ProjectItems)


@app.get("/ping")
async def ping():
    return {"Hello": "World"}


@app.post("/project/create/", status_code=status.HTTP_201_CREATED)
async def create_project(name=Form(...), description=Form(...)):
    project = await Project.create(name=name, description=description)
    return await project_pydantic.from_tortoise_orm(project)


@app.get("/projects/", status_code=status.HTTP_200_OK)
async def get_projects():
    list = await project_pydantic.from_queryset(Project.all())
    if len(list) == 0:
        return {'Response': "No Projects"}
    else:
        return list


@app.post("/project/screens/add/", status_code=status.HTTP_202_ACCEPTED)
async def add_screen(screen_names: ScreenNames, project_id: int):
    project = await Project.get(id=project_id)
    screen_item = await Screen.create(screen_names=screen_names, project=project)
    project_items = await ProjectItems.get_or_none(project=project)
    if project_items == None:
        project_items = await ProjectItems.create(project=project)

    await project_items.items.add(screen_item)
    await project_items.save()

    return await screen_pydantic.from_tortoise_orm(screen_item)


@app.get("/project/screens/", status_code=status.HTTP_202_ACCEPTED)
async def get_project_screens(project_id: int):
    project = await Project.get(id=project_id)
    return await screen_pydantic_list.from_queryset(Screen.filter(project=project))


@app.get("/project/items/", status_code=status.HTTP_202_ACCEPTED)
async def get_project_items(project_id: int):
    project = await Project.get(id=project_id)
    project_items = await ProjectItems.get(project=project)
    return await project_items.items.all()


    
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": {"app.models"}},
    generate_schemas=True,
    add_exception_handlers=True,
)