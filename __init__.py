# from .SpaceFlower_Nodes,  import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
# from .SpaceFlower_Sampler import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

# __all__ = ['NODE_CLASS_MAPPINGS', '[NODE_DISPLAY_NAME_MAPPINGS']

import importlib

node_list = [
    "SpaceFlower_Prompt",
    "SpaceFlower_HangulPrompt" 
    # "SpaceFlower_SD_Loader",
    # "SpaceFlower_SDXL_Loader",
    # "SpaceFlower_SD_Sampler",
    # "SpaceFlower_SDXL_Sampler",
    # "SpaceFlower_ControlNet",
    # "SpaceFlower_Lora",
    # "SpaceFlower_Upscale",          
    # "SpaceFlower_MaskAreaLatent",   
    # "SpaceFlower_VideoData",    
]

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

for module_name in node_list:
    imported_module = importlib.import_module(".{}".format(module_name), __name__)

    NODE_CLASS_MAPPINGS = {**NODE_CLASS_MAPPINGS, **imported_module.NODE_CLASS_MAPPINGS}
    NODE_DISPLAY_NAME_MAPPINGS = {**NODE_DISPLAY_NAME_MAPPINGS, **imported_module.NODE_DISPLAY_NAME_MAPPINGS}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
