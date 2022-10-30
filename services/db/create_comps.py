import csv
import json
from app.models import CompTypes, ScreenTypes, CompsModel

class CreateComps():
    '''Generater for Comps to add to Projects'''

    def __init__(self):
        pass


    def add_screen_comps(self, project_comps: list, screen_types: list):
        '''Create a screen comp'''
        width = 1920
        height = 1080
        comp_name = CompTypes.screen.value

        if project_comps == []:

            comp = CompsModel(comp_name=comp_name, width=width, height=height, types=screen_types)
            project_comps.append(comp.dict())

        else:

            for comp in project_comps:
                if comp['comp_name'] == comp_name:

                    for screen_type in screen_types:
                        type_checker = False
                        for this_type in comp['types']:
                            if screen_type == this_type:
                                type_checker = True
                        if not type_checker:
                            comp['types'].append(screen_type)
                break

        return {"Comps" : project_comps}


    def add_all_screens(self, project_comps: list):
        '''Create all screen comps'''
        width = 1920
        height = 1080
        comp_name = CompTypes.screen.value

        screen_types = [screen_type for screen_type in ScreenTypes]
        
        if project_comps == []:

            comp = CompsModel(comp_name=comp_name, width=width, height=height, types=screen_types)
            project_comps.append(comp.dict())

        else:

            for comp in project_comps:
                if comp['comp_name'] == comp_name:

                    for screen_type in screen_types:
                        type_checker = False
                        for this_type in comp['types']:
                            if screen_type == this_type:
                                type_checker = True
                        if not type_checker:
                            comp['types'].append(screen_type)
                break

        return {"Comps" : project_comps}
        

    def create_csv(self, project_name: str, project_comps: dict):
        '''Create a CSV file from the project_comps dict'''
        comp_data = project_comps['Comps']

        for comps in comp_data:
            types_converted = str(comps['types']).replace('"', '').replace("'", '').replace(", ", "|")
            comps['types'] = types_converted

        # Create a CSV file
        csv_file_name = f"{project_name}_comps.csv"
        csv_file = open(csv_file_name, 'w', newline='')

        csv_writer = csv.writer(csv_file)
        count = 0

        for comp in comp_data:
            if count == 0:
                header = comp.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(comp.values())

        csv_file.close()

        return csv_file_name