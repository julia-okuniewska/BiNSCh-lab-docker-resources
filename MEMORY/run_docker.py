import json
import subprocess

# Modify variables below:
INDEX_NUMBER = 123456
EXERCISE_NAME = "Docker_Memory_04"
options = "--memory 10m --memory-swap 12m"
# ----------------------


CONTAINER_NAME = "docker-memory-container"


def parse_inspect_output(output: dict) -> str:
    return f"""Is container OOM Killed = {output["State"]["OOMKilled"]}
RAM Memory Bytes Allocated = {output["HostConfig"]["Memory"]}
RAM Memory Bytes Allocated = {output["HostConfig"]["MemorySwap"]}"""


def cleanup() -> None:
    cleanup_command = f"docker container rm {CONTAINER_NAME}"
    cleanup_result = subprocess.run(cleanup_command)
    if cleanup_result.returncode == 0:
        print("Docker container cleanup completed successfully")


run_command = f"docker run {options} --name {CONTAINER_NAME} docker-memory"
print(f"Running command: {run_command}")
run_result = subprocess.run(run_command, capture_output=True)
if run_result.returncode != 0:
    print(f"Cleaning up previous {CONTAINER_NAME} container")
    cleanup()
    run_result = subprocess.run(run_command, capture_output=True)

print("Inspecting container")
inspect_command = [f"docker", "container", "inspect", CONTAINER_NAME]
inspect_raw_result = subprocess.run(inspect_command, capture_output=True)
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
