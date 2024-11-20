MODEL_CONFIGS = {
    'GPT-4o': {
        'provider': 'openai',
        'model_name': 'gpt-4o',
        'max_tokens': 4096
    },

    'GPT-4': {
        'provider': 'openai',
        'model_name': 'gpt-4',
        'max_tokens': 4096
    },
    'GPT-3.5': {
        'provider': 'openai',
        'model_name': 'gpt-3.5-turbo',
        'max_tokens': 4096
    },
    'Claude-3': {
        'provider': 'anthropic',
        'model_name': 'claude-3-opus-20240229',
        'max_tokens': 4096
    },
    'PaLM': {
        'provider': 'google',
        'model_name': 'chat-bison',
        'max_tokens': 2048
    }
}
