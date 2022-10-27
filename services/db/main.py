from ctypes import Union
from turtle import Screen
from typing import List
from app.models import Project
from fastapi import FastAPI, status, Form
from fastapi.responses import FileResponse
from create_comps import CreateComps, ScreenTypes
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

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


@app.get("/project/{project_id}/", status_code=status.HTTP_200_OK)
async def get_project(project_id: int):
    '''Get a single project based on an ID'''
    project = await Project.get(id=project_id)
    if not project:
        raise HTTPNotFoundError
    return await project


@app.get("/screens/types/", status_code=status.HTTP_200_OK)
async def get_screen_comp_types():
    '''Return a list of screen types'''
    screen_type_list = [screen_type.value for screen_type in ScreenTypes]
    return { 'ScreenTypes' : screen_type_list}


@app.post("/project/{project_id}/add_screen_comp/", status_code=status.HTTP_201_CREATED)
async def add_screen_comp_type(project_id: int, screen_types: List[ScreenTypes]):
    ''' Add a screen comp to a project '''
    project = await Project.get(id=project_id)
    if not project:
        raise HTTPNotFoundError
    create_comps = CreateComps()
    screen_comps = create_comps.add_screen_comps(project_comps=project.project_comps['Comps'], screen_types=screen_types)

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


@app.get("/project/{project_id}/get_comps/", status_code=status.HTTP_200_OK)
async def get_comps(project_id: int):
    ''' Get all comps for a project '''
    project = await Project.get(id=project_id)
    if not project:
        raise HTTPNotFoundError
    return project.project_comps


@app.get("/project/{project_id}/get_comps_csv/", status_code=status.HTTP_200_OK)
async def get_comps_csv(project_id: int):
    ''' Get all comps for a project as a csv '''
    project = await Project.get(id=project_id)
    if not project:
        raise HTTPNotFoundError
    create_comps = CreateComps()
    csv = create_comps.create_csv(project_name=project.project_name,
                                    project_comps=project.project_comps)

    headers = {'Access-Control-Expose-Headers': 'Content-Disposition'}
    return FileResponse(csv, filename=csv, headers=headers)

    
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": {"app.models"}},
    generate_schemas=True,
    add_exception_handlers=True,
)