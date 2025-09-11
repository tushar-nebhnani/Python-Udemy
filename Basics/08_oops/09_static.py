class ChaiUtils:
    @staticmethod
    # Static method are those methods which does not require any object creation.
    def clean_ingedients(text):
        return [item.strip() for item in text.split(',')]
    
raw = " water,  milk  , ginger, honey"

# obj = ChaiUtils()
# print(obj.clean_ingedients(raw))

print(ChaiUtils.clean_ingedients(raw))