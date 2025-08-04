INSTRUCTION = "Now you are at the kitchen table, pick up the apple from the kitchen table, navigate to the serving table, place the apple on the serving table, pick up the bowl from the serving table, navigate to the kitchen table, place the bowl on the kitchen table."

SYSTEM_PROMPT = '''
'\n\nPlease only use [\'demo_robot\'] with skills 
{
    \'demo_robot\': \'{
        "robot_name": "demo_robot", 
        "robot_tool": [
            {
                "function": {
                    "name": "navigate_to_target", 
                    "description": "Navigate to target, do not call when Navigation to target has been successfully performed.\\\\n    Args:\\\\n        target: String, Represents the navigation destination.\\\\n    "
                }, 
                "input_schema": {
                    "properties": {
                        "target": {"title": "Target", "type": "string"}
                    },
                    "required": ["target"], 
                    "title": "navigate_to_targetArguments", 
                    "type": "object"
                }
            },
            {
                "function": {
                    "name": "grasp_object", 
                    "description": "Pick up the object, do not call when object has been successfully grasped.\\\\n    Args:\\\\n        object: String, Represents which to grasp.\\\\n    "
                }, 
                "input_schema": {
                    "properties": {
                        "object": {"title": "Object", "type": "string"}
                    }, 
                    "required": ["object"], 
                    "title": "grasp_objectArguments", 
                    "type": "object"
                }
            },
            {
                "function": {
                    "name": "place_to_affordance", 
                    "description": "Place the grasped object in affordance, do not call when object has been successfully placed on affordance.\\\\"\\\\n    Args:\\\\n        affordance: String, Represents where the object to place.\\\\n        object: String, Represents the object has been grasped.\\\\n    "}, 
                "input_schema": {
                    "properties": {
                        "affordance": {"title": "Affordance", "type": "string"}, 
                        "object": {"default": null, "title": "Object", "type": "string"}
                    }, 
                    "required": ["affordance"], 
                    "title": "place_to_affordanceArguments", 
                    "type": "object"
                }
            }
        ], 
        "robot_state": "idle", 
        "timestamp": 1751276327
    }\'
}.\n
Please break down the given task into sub-tasks, each of which cannot be too complex, make sure that a single robot can do it. \n
It can\'t be too simple either, e.g. it can\'t be a sub-task that can be done by a single step robot tool. \n
Each sub-task in the output needs a concise name of the sub-task, which includes the robots that need to complete the sub-task. \n
Additionally you need to give a 200+ word reasoning explanation on subtask decomposition and analyze if each step can be done by a single robot based on each robot\'s tools!\n\n

## The output format is as follows, in the form of a JSON structure:\n
{\n
    "reasoning_explanation": xxx,\n    
    "subtask_list": [\n
        {
            "robot_name": xxx, 
            "subtask": xxx, 
            "subtask_order": xxx
        },\n
        {
            "robot_name": xxx, 
            "subtask": xxx, 
            "subtask_order": xxx
        },\n
        {
            "robot_name": xxx, 
            "subtask": xxx, 
            "subtask_order": xxx
        },\n
    ]\n
}\n\n

## Note: \'subtask_order\' means the order of the sub-task. \n
# If the tasks are not sequential, please set the same \'task_order\' for the same task. For example, if two robots are assigned to the two tasks, both of which are independance, they should share the same \'task_order\'.\n
# If the tasks are sequential, the \'task_order\' should be set in the order of execution. For example, if the task_2 should be started after task_1, they should have different \'task_order\'.\n\n
# 
# # The task to be completed is: [\'Now you are at the kitchen table, pick up the apple from the kitchen table, navigate to the serving table, place the apple on the serving table, pick up the bowl from the serving table, navigate to the kitchen table, place the bowl on the kitchen table.\']. Your output answer:\n',
'''