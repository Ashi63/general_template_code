import os

class DataScienceProjectGenerator:
    def __init__(self, project_name, root_dir='.'):
        self.project_name = project_name
        self.root_dir = root_dir
        
    def create_project_structure(self):
        project_path = os.path.join(self.root_dir,self.project_name)
        os.makedirs(project_path,exist_ok=True)
        
        folders = [
            'artifacts',
            'logs',
            'data',
            'notebooks',
            'scripts',
            'models',
            'reports'
        ]

        
        for folder in folders:
            folder_path = os.path.join(project_path,folder)
            os.makedirs(folder_path,exist_ok=True)
            with open(os.path.join(folder_path,'.gitkeep'),'w') as f:
                pass
            with open(os.path.join(folder_path,'__init__.py'),'w') as f:
                pass
            
        self.create_readme(project_path)
        
    def create_readme(self,project_path):
        readme_content = f'# {self.project_name}\n\nProject structure for the {self.project_name} data science project. '
        with open(os.path.join(project_path,"README.md"),'w') as f:
            f.write(readme_content)
            
if __name__ == '__main__':
    project_name = input('Enter project name: ')
    project_generator = DataScienceProjectGenerator(project_name)
    project_generator.create_project_structure()
        
        
        
    
            
    
        
        