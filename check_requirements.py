import sys
import yaml
from beautifultable import BeautifulTable
from pathlib import Path


print("CHECK THAT ALL TASKS FOLLOWS THE EXPLAINED STRUCTURE IN DOC")

# As inginious-autotest required a folder where everything is stored, use that
path = Path("LEPL1402")
task_folders = [x for x in path.iterdir() if x.is_dir() and x.name != "$common"]

# Creates a table
table = BeautifulTable()
table.column_headers = ["task folder", "reasons"]

# fill the table
for folder in task_folders:
    files_and_folder_in_task = [x.name for x in folder.iterdir()
                                if
                                x.name in ["src", "templates", "flavour", "feedback_settings.yaml", "run", "task.yaml"]]

    # skip folder with only task ( QCM )
    if len(files_and_folder_in_task) == 1 and "task.yaml" in files_and_folder_in_task:
        continue

    # check if feedback_settings
    if "feedback_settings.yaml" in files_and_folder_in_task:
        feedback_path = str(folder / "feedback_settings.yaml")
        problem = ""

        # check existence of folders src and templates (TODO maybe also check emptiness of folder )
        if "src" not in files_and_folder_in_task or "templates" not in files_and_folder_in_task:
            problem += "Missing any of these critical folder(s) : src / templates" + "\n"

        with open(feedback_path, "r") as stream:
            try:
                result = yaml.safe_load(stream)

                # check if flavour is needed
                if "feedback_kind" in result:
                    if ("has_feedback" not in result) or not result["has_feedback"]:
                        problem += "You must set has_feedback to True in order to have feedback on INGInious" + "\n"
                    if result["feedback_kind"] == "JaCoCo" and "flavour" not in files_and_folder_in_task:
                        problem += "You must have a flavour folder for coverage testing" + "\n"

                if "quorum" in result:
                    if not isinstance(result["quorum"], float):
                        problem += "Quorum should be a float" + "\n"
                    else:
                        if result["quorum"] > 1.0 or result["quorum"] < 0.0:
                            problem += "Quorum should be a float between 0.0 and 1.0" + "\n"

                if "coverage_stats" in result:
                    if not isinstance(result["coverage_stats"], list):
                        problem += "coverage_stats should be a sequence of string" + "\n"
                    else:
                        if any([
                            item not in ["INSTRUCTION", "BRANCH", "LINE", "METHOD", "CLASS"]
                            for item in result["coverage_stats"]]
                        ):
                            problem += "Unknown value inside coverage_stats" + "\n"

                if "prohibited" in result:
                    if not isinstance(result["prohibited"], dict):
                        problem += "prohibited should be a dictionary (String, List/Sequence) " + "\n"
                    else:
                        if any([
                            (not isinstance(problem_id, str)) or (not isinstance(statments, list))
                            for (problem_id, statments) in result["prohibited"].items()
                        ]):
                            problem += "prohibited is improperly constructed" + "\n"

            except yaml.YAMLError as exc:
                problem += "Parsing error in feedback_settings.yaml\n"

        if problem != "":
            table.append_row([folder.name, problem])

# if there is errors(s), tell Travis
if len(table) > 0:
    print(table)
    sys.exit(42)
else:
    print("Nothing wrong : good job :) ")
    sys.exit(0)
