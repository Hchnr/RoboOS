{
    'messages': [
        {
            'role': 'user', 
            'content': 'Navigate to kitchen table'
        }
    ], 
    'model': '/share/project/liangdong/Qwen/Qwen2.5-7B-Instruct', 
    'n': 1, 
    'temperature': 0, 
    'top_p': 1.0, 
    'max_tokens': 8192, 
    'stop': ['Observation:'], 
    'tools': [
        {
            'function': {
                'name': 'navigate_to_target', 
                'description': 'Navigate to target, do not call when Navigation to target has been successfully performed.\n    Args:\n        target: String, Represents the navigation destination.\n    '
            }, 
            'input_schema': {
                'properties': {
                    'target': {'title': 'Target', 'type': 'string'}
                }, 
                'required': ['target'], 
                'title': 'navigate_to_targetArguments', 
                'type': 'object'
            }
        }, {
            'function': {
                'name': 'grasp_object', 
                'description': 'Pick up the object, do not call when object has been successfully grasped.\n    Args:\n        object: String, Represents which to grasp.\n    '
            }, 
            'input_schema': {
                'properties': {
                    'object': {'title': 'Object', 'type': 'string'}
                }, 
                'required': ['object'], 
                'title': 'grasp_objectArguments', 
                'type': 'object'
            }
        }, {
            'function': {
                'name': 'place_to_affordance', 
                'description': 'Place the grasped object in affordance, do not call when object has been successfully placed on affordance."\n    Args:\n        affordance: String, Represents where the object to place.\n        object: String, Represents the object has been grasped.\n    '
            }, 
            'input_schema': {
                'properties': {
                    'affordance': {'title': 'Affordance', 'type': 'string'}, 
                    'object': {'default': None, 'title': 'Object', 'type': 'string'}
                }, 
                'required': ['affordance'], 
                'title': 'place_to_affordanceArguments', 
                'type': 'object'
            }
        }
    ]
}