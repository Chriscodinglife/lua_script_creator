from enum import Enum
from tortoise import fields
from pydantic import BaseModel
from tortoise.models import Model


class ProjectStatus(str, Enum):
    '''Model for keep track of project status'''
    project_created = "Project Created"
    designing_overlays = "Designing Overlays"
    designing_ads = "Designs Ads"
    final_checks = "Doing Final Checks"
    posted_online = "Posted Online"
    finished = "Finished Project"

class CompTypes(Enum):
    '''Types of comps'''
    alert = "Alert"
    banner = "Banner"
    camera_overlay = "Camera_Overlay"
    icon = "Icon"
    long_support_bar = "Long_Support_Bar"
    main_design_title = "Main_Design_Title"
    panel = "Panel"
    screen = "Screen"
    short_support_bar = "Short_Support_Bar"
    social_bar = "Social_Bar"
    social_bar_stack = "Social_Bar_Stack"
    stinger = "Stinger"

    def __str__(self):
        return self.value


class ScreenTypes(str, Enum):
    '''Types of Comps'''
    blank: str = "Blank"
    starting_soon: str = "Starting_Soon"
    offline: str = "Offline"
    be_right_back: str = "Be_Right_Back"
    thanks_for_watching: str = "Thanks_For_Watching"


class CompsModel(BaseModel):
    '''Basic Model for Comps'''
    comp_name: str
    width: int
    height: int
    screen_types: str


class Project(Model):
    '''Project Model for the database'''
    id = fields.IntField(pk=True)
    project_name = fields.CharField(max_length=255)
    project_description = fields.TextField()
    modified_time = fields.DatetimeField(auto_now=True)
    project_status : ProjectStatus = fields.CharEnumField(ProjectStatus, default=ProjectStatus.project_created, max_length=100)
    project_comps : fields.JSONField = fields.JSONField(default={"Comps": []})

    def __str__(self):
        return self.name