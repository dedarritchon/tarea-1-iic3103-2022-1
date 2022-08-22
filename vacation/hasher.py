from unidecode import unidecode
import hashlib

def generate_id(name):
    m = hashlib.md5()
    safe_name = unidecode(name.lower().replace(' ', '_')).encode('utf-8')
    m.update(safe_name)
    return str(m.hexdigest())
