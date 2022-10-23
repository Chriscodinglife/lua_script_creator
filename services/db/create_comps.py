import csv
import json
from app.models import CompTypes, ScreenTypes, CompsModel

class CreateComps():
    '''Generater for Comps to add to Projects'''

    def __init__(self):
        pass

    def add_screen_comp(self, project_comps: list, screen_type: ScreenTypes):
        '''Create a screen comp'''
        width = 1920
        height = 1080
        comp_name = CompTypes.screen.value
        
        if project_comps == []:
            # If there is nothing in the project_comps list, add the first comp
            screen_types_list = []
            screen_types_list.append(screen_type.value)
            screen_types = str([comma.replace(",", "|") for comma in screen_types_list]).replace("'", "")
            comp = CompsModel(comp_name=comp_name, width=width, height=height, screen_types=screen_types)
            project_comps.append(comp.dict())
        else:
            # If there is something in the project_comps list, convert the screen_types to a list
            for comp in project_comps:
                # Iterate through each comp in the project_comps list
                if comp['comp_name'] == comp_name:
                    current_screen_types = str(comp['screen_types']).replace("[", "").replace("]", "")
                    current_screen_types = current_screen_types.split("|")
                    type_flag = False
                    # Check if the screen_type is already in the list
                    for this_type in current_screen_types:
                        if screen_type in this_type:
                            type_flag = True
                    if type_flag == False:
                        # If the screen_type is not in the list, add it
                        current_screen_types.append(screen_type.value)
                        screen_types = str(current_screen_types).replace("'", "").replace(",", "|").replace(" ", "")
                        # Update the screen_types in the comp
                        comp['screen_types'] = screen_types

        return {"Comps" : project_comps}

    def add_all_screens(self, project_comps: list):
        '''Create all screen comps'''
        width = 1920
        height = 1080
        comp_name = CompTypes.screen.value

        for screen_type in ScreenTypes:
            if project_comps == []:
                # If there is nothing in the project_comps list, add the first comp
                screen_types_list = []
                screen_types_list.append(screen_type.value)
                screen_types = str([comma.replace(",", "|") for comma in screen_types_list]).replace("'", "")
                comp = CompsModel(comp_name=comp_name, width=width, height=height, screen_types=screen_types)
                project_comps.append(comp.dict())
            else:
                # If there is something in the project_comps list, convert the screen_types to a list
                for comp in project_comps:
                    # Iterate through each comp in the project_comps list
                    if comp['comp_name'] == comp_name:
                        current_screen_types = str(comp['screen_types']).replace("[", "").replace("]", "")
                        current_screen_types = current_screen_types.split("|")
                        type_flag = False
                        # Check if the screen_type is already in the list
                        for this_type in current_screen_types:
                            if screen_type in this_type:
                                type_flag = True
                        if type_flag == False:
                            # If the screen_type is not in the list, add it
                            current_screen_types.append(screen_type.value)
                            screen_types = str(current_screen_types).replace("'", "").replace(",", "|").replace(" ", "")
                            # Update the screen_types in the comp
                            comp['screen_types'] = screen_types
            
        return {"Comps" : project_comps}

    def create_csv(self, project_name: str, project_comps: dict):
        '''Create a CSV file from the project_comps dict'''
        comp_data = project_comps['Comps']

        # Create a CSV file
        csv_file_name = f"{project_name}_comps.csv"
        csv_file = open(csv_file_name, 'w')

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