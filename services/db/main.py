from app.models import Project
from app.create_comps import CreateComps, ScreenTypes
from fastapi import FastAPI, status, Form
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

app = FastAPI()

project_pydantic = pydantic_model_creator(Project)

@app.get("/ping")
async def ping():
    return {"Hello": "World"}


@app.post("/project/create/", status_code=status.HTTP_201_CREATED)
async def create_project(project_name=Form(...), project_description=Form(...)):
    ''' Create a new project '''
    project = await Project.create(project_name=project_name, 
                                    project_description=project_description)
    return await project_pydantic.from_tortoise_orm(project)


@app.get("/projects/", status_code=status.HTTP_200_OK)
async def get_projects():
    ''' Get all projects '''
    list = await project_pydantic.from_queryset(Project.all())
    if len(list) == 0:
        return {'Response': "No Projects"}
    else:
        return list


@app.post("/project/{project_id}/add_screen_comp/", status_code=status.HTTP_201_CREATED)
async def add_screen_comp(project_id: int, screen_type: ScreenTypes):
    ''' Add a screen comp to a project '''
    project = await Project.get(id=project_id)
    if not project:
        raise HTTPNotFoundError
    create_comps = CreateComps()
    screen_comps = create_comps.add_screen_comp(project_comps=project.project_comps['Comps'], screen_type=screen_type)

    project.project_comps = screen_comps
    await project.save()
    return await project


@app.post("/project/{project_id}/add_all_screens/", status_code=status.HTTP_201_CREATED)
async def add_all_screens(project_id: int):
    ''' Add all screen comps to a project '''
    project = await Project.get(id=project_id)
    if not project:
        raise HTTPNotFoundError
    create_comps = CreateComps()
    screen_comps = create_comps.add_all_screens(project_comps=project.project_comps['Comps'])

    project.project_comps = screen_comps
    await project.save()
    return await project

    
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": {"app.models"}},
    generate_schemas=True,
    add_exception_handlers=True,
)