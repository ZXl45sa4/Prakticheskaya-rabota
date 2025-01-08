def introspection_info(obj):
    info = {'type': type(obj).__name__,
            'attributes': [i for i in dir(obj) if i.startswith('') and not callable(getattr(obj, i))],
            'methods': [j for j in dir(obj) if j.startswith('')],
            'module': obj.__class__.__module__}
    return info


number_info = introspection_info(42)
print(number_info)