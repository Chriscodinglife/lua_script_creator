from models import CompTypes, ScreenTypes, CompsModel

class CreateComps():
    '''Generater for Comps to add to Projects'''

    def __init__(self):
        pass

    def create_screen_comp(self, comp_name: CompTypes, types: list[ScreenTypes]):
        '''Create a screen comp'''
        width = 1920
        height = 1080
        comp = CompsModel(comp_name=comp_name, width=width, height=height, types=types)
        return comp.dict()