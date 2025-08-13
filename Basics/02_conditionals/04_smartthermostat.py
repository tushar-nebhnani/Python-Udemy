device_status = "active"
temperature = 0 

if device_status == "active":
    if temperature > 35:
        print(f"Warning! High Tempreature.")
    else:
        print(f"Device is working at normal temperature.")
else:
    print(f"Device is offline.")