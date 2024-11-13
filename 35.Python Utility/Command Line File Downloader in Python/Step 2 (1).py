def check_unit(length): # length in bytes
    if length < units['KB']['size']:
        return 'B'

    elif length >= units['KB']['size'] and length <= units['MB']['size']:
        return 'KB'
    elif length >= units['MB']['size'] and length <= units['GB']['size']:
        return 'MB'
    elif length > units['GB']['size']:
        return 'GB'
