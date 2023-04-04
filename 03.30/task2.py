# Task Nr.3:

# Create a class called TimeUtils that has a static method called time_to_seconds that takes a time string
#  in the format hh:mm:ss and returns the total number of seconds represented by that time. Use functional programming paradigm.

# Sukurkite klasę, pavadintą TimeUtils, kuri turi statinį metodą, vadinamą time_to_seconds,
# kuri paima laiko eilutę formatu hh:mm:ss ir grąžina bendrą to laiko sekundžių skaičių. Naudokite funkcinio programavimo paradigmą.


class TimeUtils:
    @staticmethod
    def time_to_seconds(time_string) -> int:
        hours, minutes, seconds = map(int, time_string.split(':'))
        return (hours * 60 * 60) + (minutes * 60) + seconds


    
    


print(TimeUtils.time_to_seconds(time_string= "51:63:65"))
        