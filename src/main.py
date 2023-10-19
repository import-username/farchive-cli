import argparse
import settings
import backup
import sys

parser = argparse.ArgumentParser(
    prog="Farchive",
    description="CLI program for choosing files and directories to backup on a routine basis."
)

subparser = parser.add_subparsers(help="sub-command help", dest="command")

# RUN command, for running backup manually
subparser_run = subparser.add_parser("run", help="run help")
# subparser_run.add_argument("--only",)
# subparser_run.add_argument("-m", "--max-required-storage")


# set (settings) command, for changing settings
subparser_settings = subparser.add_parser("set", help="set help")
subparser_settings.add_argument("--auto-backup-enabled", dest="auto_backup_enabled", type=bool)
subparser_settings.add_argument("--auto_backup_type", dest="auto_backup_type", choices=settings.app_settings_options["auto_backup_type"])


# add command, for adding backup paths
subparser_add = subparser.add_parser("add", help="add help")
subparser_add.add_argument("-b", "--backup-path", dest="backup_path", type=str, action="append")
subparser_add.add_argument("-p", "--program-backup-path", dest="program_backup_path", type=str, action="append")

def executeCommands():
    parsed = parser.parse_args(sys.argv[1:])

    if (parsed.command == "run"):
        backup.execute_backup()
    elif (parsed.command == "add"):
        for new_path in parsed.backup_path:
            is_successfully_added = backup.add_backup_path(new_path)

            if not is_successfully_added:
                print("Failed to add path: " + new_path)
        
        print("Finished")
    elif (parsed.command == "set"):
        print("set")

if __name__ == "__main__":
    executeCommands()