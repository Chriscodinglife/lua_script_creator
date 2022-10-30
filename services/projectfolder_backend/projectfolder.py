import os
import shutil

from lockfile import Error

class Projectfolder():
    '''Class for downloading a Project Folder Template'''


    def __init__(self, project_name: str, include_icons: bool) -> None:
        '''Constructor to initialize the class'''
        self.project_name = project_name
        self.include_icons = include_icons
        self.this_dir = os.path.dirname(os.path.abspath(__file__))
        self.projects_container = os.path.join(self.this_dir, 'projects')

        try:
            os.mkdir(self.projects_container)
        except FileExistsError:
            pass

        self.project_folder = os.path.join(self.projects_container, project_name)
    
        self.local_icons = os.path.join(self.this_dir, 'icons')
        
        self.folders_to_create = ['after_effects',
                                  'fonts',
                                  'images',
                                  'advertisement',
                                  'renders_for_ads',
                                  'renders_for_package']

    
    def create_project_folder(self):
        '''Creates the project folder and subfolders
        return true or flase if the folder was created or not'''
        try:
            # Create the project folder
            os.mkdir(self.project_folder)


            # Crate the subfolders
            for folder in self.folders_to_create:
                create_folder = os.path.join(self.project_folder, folder)
                keep_folder = os.path.join(create_folder, '.keep')
                os.mkdir(create_folder)
                with open(keep_folder, 'w') as keep_file:
                    keep_file.write('')
                # Create the icons folder if needed
                if os.path.basename(folder) == 'images' and self.include_icons:
                    icons_in_images_dir = os.path.join(self.project_folder, folder, 'icons')
                    # No need to create the icons folder, copytree will do it
                    shutil.copytree(self.local_icons, icons_in_images_dir)
            return True
        except FileExistsError:
            return False


    def delete_project_folder(self):
        '''Deletes the project folder and subfolders'''
        shutil.rmtree(self.project_folder)


    def get_project_folder(self):
        '''Returns the project folder path'''
        project_folder_created = self.create_project_folder()

        try:
            if project_folder_created:
                return self.project_folder
        except Error as e:
            return { 'error': e }


def main():
    '''Main function'''
    project_name = 'Test'
    include_icons = True
    project_folder = Projectfolder(project_name, include_icons)
    print(project_folder.get_project_folder())


if __name__ == '__main__':
    main()