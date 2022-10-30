import os
import shutil
import zipfile
class ProjectFolder():
    '''Class for downloading a Project Folder Template'''


    def __init__(self, project_name: str, include_icons: bool) -> None:
        '''Constructor to initialize the class'''
        self.project_name = project_name.replace(" ", "_") + '_project'
        self.zip_file_name = project_name + '.zip' 
        self.include_icons = include_icons
        self.this_dir = os.path.dirname(os.path.abspath(__file__))
        self.projects_container = os.path.join(self.this_dir, 'projects')
        self.zip_file_path = os.path.join(self.projects_container, self.zip_file_name)

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
        '''Creates the project folder and subfolders and returns the project folder path'''
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
            return self.project_folder
        except FileExistsError:
            return {'response': 'Project folder already exists'}


    def delete_project_folder(self):
        '''Deletes the project folder and subfolders'''
        shutil.rmtree(self.project_folder)


    def zip_project_folder(self):
        '''Zips the project folder and returns the zip file path'''
        zf = zipfile.ZipFile(self.zip_file_path, "w", zipfile.ZIP_DEFLATED)
        for dirname, subdirs, files in os.walk(self.project_folder):
            for filename in files:
                absname = os.path.abspath(os.path.join(dirname, filename))
                arcname = absname[len(self.project_folder) + 1:]
                zf.write(absname, arcname)
        zf.close()

        return self.zip_file_path


    def get_project_folder(self):
        '''Returns the project folder path'''
        return self.project_folder