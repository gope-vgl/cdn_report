VALID_MAP = {
    "self_test": ["OP_STATUS_OK"],
    "system_health": ["OP_STATUS_OK"],
    "hostpwr_state": ["ON"],
    "fans_status": ["OP_STATUS_OK"],
    "fans_redundancy": ["REDUNDANT"],
    "temperature_status": ["OP_STATUS_OK"],
    "power_supplies_status": ["OP_STATUS_OK"],
    "power_supplies_redundancy": ["REDUNDANT"],
    "power_supplies_mismatch": [0],
    "storage_status": ["OP_STATUS_OK"],
    "nic_status": ["OP_STATUS_OK"],
    "cpu_status": ["OP_STATUS_OK"],
    "mem_status": ["OP_STATUS_OK"],
    "ext_health_status": ["OP_STATUS_OK"]
}

def validate_key(key: str, value):
    if key not in VALID_MAP:
        return None
    return value
