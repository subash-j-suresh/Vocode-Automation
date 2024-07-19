webhook_handlers = {}


def register_webhook_handler(endpoint, expected_keys):
    def decorator(func):
        if endpoint in webhook_handlers:
            raise ValueError(f"Handler for endpoint '{endpoint}' is already registered")
        print(endpoint)
        webhook_handlers[endpoint] = (func, expected_keys)
        return func

    return decorator


def get_handler(endpoint):
    return webhook_handlers.get(endpoint)
