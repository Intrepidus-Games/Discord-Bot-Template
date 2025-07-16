from lib.debug import Debug
import os, glob, importlib.util, inspect
import asyncio

class FileLoader:
    def __init__(
            self, 
            auto_load: bool = True,
            debug: Debug=Debug(enabled=True), 
            path: str="routes",
        ) -> None:

        # Set Defaults
        self.debug = debug
        self.path = path

        self.debug.log(f"FileLoader initialized with path: {path}")

        if auto_load:
            self.load()

    async def load_file(self, module, filename: str, run_func_name: str="run", *args, **kwargs):
        if hasattr(module, run_func_name):
            func = getattr(module, run_func_name)

            # Get the function parameters
            func_signature = inspect.signature(func)
            func_params = func_signature.parameters

            # Filter kwargs based on the required function parameters
            filtered_kwargs = {
                key: value for key, value in kwargs.items() if key in func_params
            }

            # Provide required arguments
            if "debug" in func_params:
                filtered_kwargs["debug"] = self.debug

            # Call the function with the appropriate arguments
            if inspect.iscoroutinefunction(func):
                await func(**filtered_kwargs)
            else:
                func(**filtered_kwargs)
        else:
            print(f"'{filename}' has no '{run_func_name}()' function.")

    def load(self, run_func_name: str="run", *args, **kwargs):
        failed_endpoints = 0

        self.debug.print("Loading endpoints")

        absolute_path = os.path.join(self.path, '**', '*.py')

        # Check if the directory exists
        #if not os.path.exists(self.path):
        #    self.debug.error(f"Directory does not exist: {self.path}")
        #    return
        
        # Check if there are any .py files in the directory
        files = glob.glob(absolute_path, recursive=True)
        if not files:
            self.debug.error(f"No .py files found in: {absolute_path}")

        for filename in files:
            try:
                spec = importlib.util.spec_from_file_location(filename, filename)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                asyncio.run(
                    self.load_file(module=module, filename=filename, run_func_name=run_func_name, *args, **kwargs)
                )
            except Exception as e:
                self.debug.error(f"Failed to load '{filename}': {e}")

        if failed_endpoints == 0:
            self.debug.print("All endpoints loaded")
        else:
            self.debug.print(f"Endpoints loaded with {failed_endpoints} fails")