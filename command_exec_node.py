import subprocess

class CommandExecNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "command": ("STRING", {
                    "multiline": True,
                    "default": "echo Hello World"
                }),
            },
            "optional": {
                "input": ("*", "*")
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output",)
    FUNCTION = "run_command"
    CATEGORY = "Custom/Utility"

    def run_command(self, command):
        try:
            # Executa o comando no shell
            result = subprocess.check_output(
                command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True
            )
        except subprocess.CalledProcessError as e:
            result = f"[ERROR] Code {e.returncode}:\n{e.output}"

        return (result,)

# Registro do node no ComfyUI
NODE_CLASS_MAPPINGS = {
    "CommandExecNode": CommandExecNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CommandExecNode": "Terminal"
}
