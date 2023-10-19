import json
import os

app_data = os.getenv("APPDATA")

appdata_dir_path = app_data + "/farchive"
settings_path = appdata_dir_path + "/settings.json"
temp_settings_path = appdata_dir_path + "/settings_tmp.json"

# For valid options for each setting that are not boolean or integer types
app_settings_options = {
    "auto_backup_type": [
        # After specified interval time has passed, a backup will be performed on listed files/directories.
        "interval", 

        # Watches every backup file/directory for changes, and only performs backup on ones that have changed.
        # Pros:
        # - Uses minimal resources.
        # - Takes the least storage over time
        # - Reduces overral bandwith usage if using google drive 
        #
        # Cons:
        # - If changes happen while program is off, it will not detect changes and will not run backup
        "watch",

        # At the specified time(s) when PC is on, backups will be performed.
        "set_time"
    ],

}

default_app_settings = {
    "auto_backup_type": "watch",
    "enable_auto_backup": False,
    "backup_paths": [],
    "running_program_backup_paths": []
}

def load_settings():
    if not os.path.exists(appdata_dir_path):
        os.mkdir(appdata_dir_path)
    
    if not os.path.exists(settings_path):
        create_settings()

    try:
        with open(settings_path) as json_settings:
            return json.load(json_settings)
    except FileNotFoundError:
        create_settings()

def create_settings():
    print("Required settings.json file was not found, so a default was created.")

    with open(settings_path, "w") as new_settings:
        json.dump(default_app_settings, new_settings, indent=4)

app_settings = load_settings()