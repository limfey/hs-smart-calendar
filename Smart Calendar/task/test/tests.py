from hstest import StageTest, TestedProgram, dynamic_test, WrongAnswer, TestPassed
import datetime

class CalendarTest(StageTest):
    @dynamic_test
    def test_note(self):
        pr = TestedProgram()
        output = pr.start().lower()
        date = datetime.datetime.now()
        date_str = str(date)
        date_str = date_str[:-11]
        if 'current date and time' not in output:
            raise WrongAnswer("Your program should print: 'Current date and time:'")
        elif date_str not in output:
            raise WrongAnswer("It's not current date and time.")
        elif "let's add a note to the calendar" not in output:
            raise WrongAnswer("Your program should print: 'Let's add a note to the calendar'")
        elif "enter year" not in output:
            raise WrongAnswer("Your program should print: 'Enter year'")
        first_note = date + datetime.timedelta(days=10)
        year = str(first_note.year)
        month_output = pr.execute(year).lower()
        if "enter month" not in month_output:
            raise WrongAnswer("Your program should print: 'Enter month'")
        month = str(first_note.month)
        day_output = pr.execute(month).lower()
        if "enter day" not in day_output:
            raise WrongAnswer("Your program should print: 'Enter day'")
        day = str(first_note.day)
        hour_output = pr.execute(day).lower()
        if "enter hour" not in hour_output:
            raise WrongAnswer("Your program should print: 'Enter hour'")
        hour = str(first_note.hour)
        minute_output = pr.execute(hour).lower()
        if "enter minute" not in minute_output:
            raise WrongAnswer("Your program should print: 'Enter minute'")
        minute = str(first_note.minute)
        note_output = pr.execute(minute).lower()
        if "enter a text" not in note_output:
            raise WrongAnswer("Your program should print: 'Enter a text'")
        note = 'Visit a doctor'
        final_output = pr.execute(note).lower()
        if 'before the event note' not in final_output:
            raise WrongAnswer("Your program should print: 'Before the event note...'")
        elif 'visit a doctor' not in final_output:
            raise WrongAnswer("Your program should print the note")
        elif 'day(s)' not in final_output:
            raise WrongAnswer("Your program should print: 'day(s)', but it doesn't")
        elif '9 day(s)' not in final_output:
            raise WrongAnswer("Wrong number of days")
        elif 'hour(s)' not in final_output:
            raise WrongAnswer("Your program should print: 'hour(s)', but it doesn't")
        elif '23 hour(s)' not in final_output:
            raise WrongAnswer("Wrong number of hours")
        elif 'minute(s)' not in final_output:
            raise WrongAnswer("Your program should print: 'minute(s)', but it doesn't")
        elif '59 minute(s)' not in final_output:
            raise WrongAnswer("Wrong number of minutes")
        else:
            raise TestPassed()

