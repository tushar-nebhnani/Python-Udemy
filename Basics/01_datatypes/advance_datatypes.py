"""
    when you bring someone else code to your program.
    NOT THE PART OF CORE PYTHON
    Advance Datatypes: datetime, time, calandar
    timedelta: duration/arthmatic operations used with time
    utitlies: arrow, dateutil 
"""
import arrow

current_time = arrow.utcnow()
print(f"current time: {current_time}")