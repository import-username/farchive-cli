import json
import os
import settings
import datetime
import shutil

backup_path = settings.appdata_dir_path + "/bak"

if not os.path.exists(backup_path):
    os.mkdir(backup_path)

def get_iso_stamp():
    return datetime.datetime.utcnow().isoformat().replace(":", "-").replace(".", "_")

def execute_backup():
    new_bak_dir = backup_path + "/" + get_iso_stamp()

    if not os.path.exists(new_bak_dir):
        os.mkdir(new_bak_dir)

    print("Executing backup...")

    for bak_path in settings.app_settings["backup_paths"]:
        if not os.path.exists(bak_path):
            print(bak_path + " does not exist. skipping...")

            continue
    
        if os.path.isdir(bak_path):
            new_dir = new_bak_dir + "/" + os.path.basename(bak_path)

            if os.path.exists(new_dir):
                new_dir = new_bak_dir + "/" + get_iso_stamp() + "__" + os.path.basename(bak_path)

            shutil.copytree(bak_path, new_dir)

        elif os.path.isfile(bak_path):
            bak_file_path = new_bak_dir + "/" + os.path.basename(bak_path)

            if os.path.exists(bak_file_path):
                bak_file_path = new_bak_dir + "/" + get_iso_stamp() + "__" + os.path.basename(bak_path)

            shutil.copyfile(bak_path, bak_file_path)
    
    print("Finished generating backups.")

def execute_partial_backup(paths: list) -> bool:
    print("Executing partial backup...")

def execute_program_backup(program: str) -> bool:
    print("Executing backup of program files...")

def add_backup_path(path: str) -> bool:
    if not os.path.exists(path):
        return False

    # with open(temp_settings_path, "w") as tmp_settings:
    #     app_settings["backup_paths"].append(path)

    #     json.dump(app_settings, tmp_settings)

    with open(settings.settings_path, "w") as bak_settings:
        settings.app_settings["backup_paths"].append(path)

        json.dump(settings.app_settings, bak_settings)

    return True