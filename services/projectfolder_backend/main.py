from fastapi import FastAPI, status
from projectfolder import ProjectFolder
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/ping", status_code=status.HTTP_200_OK)
def ping():
    
    '''Return a hello there for a successful ping'''
    return {"response": "Hello there"}


@app.get("/download", status_code=status.HTTP_200_OK)
def download_project_folder(project_name: str, include_icons: bool = False):
        
        '''Return a project folder to download'''
        project_folder = ProjectFolder(project_name, include_icons)
        project_folder.create_project_folder()
        file = project_folder.zip_project_folder()
        return FileResponse(file, media_type="application/zip", filename=f"{project_folder.project_name}.zip")


@app.get("/delete", status_code=status.HTTP_200_OK)
def delete_project_folder(project_name: str):
    
    '''Delete a project folder'''
    project_folder = ProjectFolder(project_name)
    if project_folder.delete_project_folder():
        return {"response": "Project folder deleted"}
    else:
        return {"response": "Project folder does not exist"}