from enum import Enum
from tortoise import fields
from tortoise.models import Model


class ProjectStatus(str, Enum):
    '''Model for keep track of project status'''
    project_created = "Project Created"
    designing_overlays = "Designing Overlays"
    designing_ads = "Designs Ads"
    final_checks = "Doing Final Checks"
    posted_online = "Posted Online"
    finished = "Finished Project"


class Project(Model):
    '''Project Model for the database'''
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    modified = fields.DatetimeField(auto_now=True)
    status : ProjectStatus = fields.CharEnumField(ProjectStatus, default=ProjectStatus.project_created, max_length=100)

    def __str__(self):
        return self.name


class ScreenNames(str, Enum):
    '''The different types of screen names'''
    blank = "Blank"
    starting_soon = "Starting_Soon"
    offline = "Offline"
    brb = "Be_Right_Back"
    thanks_for_watching = "Thanks_For_Watching"
    all_scenes = "Blank,Starting_Soon,Offline,Be_Right_Back,Thanks_For_Watching"


class ItemNames(str, Enum):
    '''Names for the grouping the compositions'''
    screens = "Screens"


class ProjectItems(Model):
    '''A Model for keeping track of all the Items in a Project'''
    id = fields.IntField(pk=True)
    items = fields.ManyToManyField('models.Screen', related_name='projectitems', through='items')
    project: fields.ForeignKeyRelation[Project] = fields.ForeignKeyField('models.Project', related_name='project_items')


class Screen(Model):
    '''A Screen Model object to add to a ProjectItems'''
    id = fields.IntField(pk=True)
    item_name : ItemNames = fields.CharEnumField(ItemNames, default=ItemNames.screens)
    screen_names : ScreenNames = fields.CharEnumField(ScreenNames, default=ScreenNames.all_scenes)
    project : fields.ForeignKeyRelation[Project] = fields.ForeignKeyField('models.Project', related_name='screen_names')
