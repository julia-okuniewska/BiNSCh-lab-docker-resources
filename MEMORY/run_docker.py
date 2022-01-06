import json
import subprocess

# Modify variables below:
INDEX_NUMBER = 123456
EXERCISE_NAME = "Docker_Memory_01"
# to avoid use of " it is possible to pass value as
# --option <value> instead of --option="<value>"
options = ""
# ----------------------


CONTAINER_NAME = "docker-memory-container"


def parse_inspect_output(output: dict) -> str:
    return f"""Is container OOM Killed = {output["State"]["OOMKilled"]}
RAM Memory Bytes Allocated = {output["HostConfig"]["Memory"]}
RAM Memory Bytes Allocated = {output["HostConfig"]["MemorySwap"]}"""


def cleanup() -> None:
    cleanup_command = f"docker container rm {CONTAINER_NAME}"
    cleanup_result = subprocess.run(cleanup_command, shell=True)
    if cleanup_result.returncode == 0:
        print("Docker container cleanup completed successfully")


run_command = f"docker run {options} --name {CONTAINER_NAME} docker-memory"
print(f"Running command: {run_command}")
run_result = subprocess.run(run_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if run_result.returncode != 0:
    print(f"Cleaning up previous {CONTAINER_NAME} container")
    cleanup()
    run_result = subprocess.run(run_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print("Inspecting container")
inspect_command = f"docker container inspect {CONTAINER_NAME}"
inspect_raw_result = subprocess.run(inspect_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
