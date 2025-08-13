def update_order():
    chai_type = "elaichi"
    def kitchen():
        nonlocal chai_type # access above scope
        chai_type = "kesar"
    kitchen()
    print(f"{chai_type}")

update_order()
# non local just look at the outer function/ just above the function
chai_type = "plain"

def front_desk():
    def kitchen():
        global chai_type 
        chai_type = "Irani chai"
    kitchen()
    print(chai_type)
front_desk()