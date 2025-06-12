import subprocess

class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

any_typ = AnyType("*")

class CommandExecNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input": (any_typ,),
                "command": ("STRING", {
                    "multiline": True,
                    "default": "echo Hello World"
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output",)
    FUNCTION = "run_command"
    CATEGORY = "Custom/Utility"

    def run_command(self, input, command):
        import subprocess
        try:
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
