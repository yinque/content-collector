def success_message(info: str, **kwargs):
    return {
        "success": True,
        "info": info,
        **kwargs
    }


def fail_message(info: str, **kwargs):
    return {
        "success": False,
        "info": info,
        **kwargs
    }

