import os, subprocess
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

def load_standard_import_tool_plugin():
    '''
    Download the 1.2 release of StandardImportToolPlugin from Github and unzip it locally.
    '''
    StandardImportToolPluginDir = os.path.join(".","StandardImportToolPlugin")
    #extra subdir in the archive    
    StandardImportToolPluginExe = os.path.join(StandardImportToolPluginDir,"Release", "StandardImportToolPlugin.exe")
    if not os.path.exists(StandardImportToolPluginExe):
        resp = urlopen('https://github.com/cat-cfs/StandardImportToolPlugin/releases/download/1.2/Release.zip')
        zipfile = ZipFile(BytesIO(resp.read()))

        #os.makedirs(StandardImportToolPluginDir)
        zipfile.extractall(path=StandardImportToolPluginDir)
    return StandardImportToolPluginExe

class SITConfig(object):

    def __init__(self, imported_project_path, initialize_mapping=False):
        self.config = {
            "output_path": imported_project_path,
            "mapping_config": {
                "initialize_mapping": initialize_mapping,
                "spatial_units": {
                    "mapping_mode": None,
                },
                "disturbance_types": None,
                "species": {
                    "species_classifier": None,
                },
                "nonforest": None
            }
        }

    def set_species_classifier(name):
        self.config["mapping_config"]["species"]["species_classifier"] = name

    def set_single_spatial_unit(id):
        self.config["mapping_config"]["spatial_units"] = {}
        self.config["mapping_config"]["spatial_units"]["mapping_mode"] = "SingleDefaultSpatialUnit"
        self.config["mapping_config"]["spatial_units"]["default_spuid"] = 42

    def set_admin_eco_mapping(admin_classifier, eco_classifier):
        self.config["mapping_config"]["spatial_units"] = {}
        self.config["mapping_config"]["spatial_units"]["mapping_mode"] = "SeperateAdminEcoClassifiers"
        self.config["mapping_config"]["spatial_units"]["admin_classifier"] = admin_classifier
        self.config["mapping_config"]["spatial_units"]["eco_classifier"] = eco_classifier

    def set_spatial_unit_mapping(spatial_unit_classifier):
        self.config["mapping_config"]["spatial_units"] = {}
        self.config["mapping_config"]["spatial_units"]["mapping_mode"] = "JoinedAdminEcoClassifier"
        self.config["mapping_config"]["spatial_units"]["spu_classifier"] = spatial_unit_classifier

    def set_non_forest_classifier(non_forest_classifier):
        self.config["mapping_config"]["nonforest"] = {}
        self.config["mapping_config"]["nonforest"]["nonforest_classifier"] = non_forest_classifier

    def map_disturbance_type(user, default):
        if self.config["mapping_config"]["disturbance_types"] is None:
            self.config["mapping_config"]["disturbance_types"] = {}
            self.config["mapping_config"]["disturbance_types"]["disturbance_type_mapping"] = []
        self.config["mapping_config"]["disturbance_types"]["disturbance_type_mapping"].append({
            "user_dist_type": user,
            "default_dist_type": default
        })
        
        

    def text_file_paths(self, ageclass_path, classifiers_path,
        disturbance_events_path, disturbance_types_path, inventory_path,
        transition_rules_path, yield_path):
        self.config["import_config"] = {
            "ageclass_path": ageclass_path,
            "classifiers_path": classifiers_path,
            "disturbance_events_path": disturbance_events_path,
            "disturbance_types_path": disturbance_types_path,
            "inventory_path": inventory_path,
            "transition_rules_path": transition_rules_path,
            "yield_path": yield_path
        }

    def database_path(self, db_path, age_class_table_name, classifiers_table_name,
        disturbance_events_table_name, disturbance_types_table_name,
        inventory_table_name, transition_rules_table_name, yield_table_name):
        
        self.config["import_config"] = {
            "path": db_path,
            "ageclass_table_name": age_class_table_name,
            "classifiers_table_name": classifiers_table_name,
            "disturbance_events_table_name": disturbance_events_table_name,
            "disturbance_types_table_name": disturbance_types_table_name,
            "inventory_table_name": inventory_table_name,
            "transition_rules_table_name": transition_rules_table_name,
            "yield_table_name": yield_table_name
        }
    
    def data_config(self, age_class_size, num_age_classes, classifiers):
        self.config["data"] = {
            "age_class": {"age_class_size":age_class_size, "num_age_classes":num_age_classes},
            "classifiers": classifiers
            "disturbance_events": [],
            "inventory": [],
            "transition_rules": [],
            "yield": []
        }

    def add_event(**kwargs):
        self.config["data"]["disturbance_events"].append(kwargs)

    def add_inventory(**kwargs):
        self.config["data"]["inventory"].append(kwargs)

    def add_transition_rule(**kwargs):
        self.config["data"]["transition_rules"].append(kwargs)

    def add_yield(**kwargs):
        self.config["data"]["yield"].append(kwargs)