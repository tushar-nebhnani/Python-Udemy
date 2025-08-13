def server_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("We don't know the flavor.")
    except ValueError as e:
        print("Error: ", e)
    else: # if try run is successfull
        print(f"{flavor} chai is served.")
    finally: # free-up resources
        print("Next customer please!")

server_chai("masala")
server_chai("unknown")