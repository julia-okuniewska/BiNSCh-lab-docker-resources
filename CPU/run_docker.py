import json
import subprocess

# Modify variables below:
INDEX_NUMBER = 123456
EXERCISE_NAME = "Docker_CPU_01"
# to avoid use of " it is possible to pass value as
# --option <value> instead of --option="<value>"
options = ""
# ----------------------


CONTAINER_NAME = "docker-cpu-container"


def parse_inspect_output(output: dict) -> str:
    return f'CPU Shares used = {output["HostConfig"]["NanoCpus"]/(1*10e8)}'


def cleanup() -> None:
    cleanup_command = f"docker container rm {CONTAINER_NAME}"
    cleanup_result = subprocess.run(cleanup_command)
    if cleanup_result.returncode == 0:
        print("Docker container cleanup completed successfully")


run_command = f"docker run {options} --name {CONTAINER_NAME} docker-cpu"
print(f"Running command: {run_command}")
run_result = subprocess.run(run_command, capture_output=True)
if run_result.returncode != 0:
    print(f"Cleaning up previous {CONTAINER_NAME} container")
    cleanup()
    run_result = subprocess.run(run_command, capture_output=True)


print("Inspecting container")
inspect_command = [f"docker", "container", "inspect", CONTAINER_NAME]
inspect_raw_result = subprocess.run(inspect_command, capture_output=True)
if inspect_raw_result.returncode != 0:
    raise Exception("Container did not run successfully! Check options value!")
inspect_result = parse_inspect_output(json.loads(inspect_raw_result.stdout)[0])

cleanup()


print("\n \n \n ------------ SUMMARY -----------")
summary = f"""{INDEX_NUMBER} summary of {EXERCISE_NAME} exercise
Executed Command = {run_command}
{inspect_result}
Logs from container: {run_result.stdout}"""

print(summary)

with open(f'{EXERCISE_NAME}.txt', 'w') as file:
    file.write(summary)
