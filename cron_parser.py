from sys import argv
from abc import abstractmethod


values = {
        'week': [i for i in range(0, 7)],
        'month': [i for i in range(1, 13)],
        'hour': [i for i in range(0, 24)],
        'day': [i for i in range(1, 32)],
        'minute': [i for i in range(0, 60)]
    }

# word conversions for months of the year
months = {
    'JAN': 1, 
    'FEB': 2,
    'MAR': 3,
    'APR': 4, 
    'MAY': 5, 
    'JUN': 6,
    'JUL': 7, 
    'AUG': 8, 
    'SEP': 9,
    'OCT': 10, 
    'NOV': 11, 
    'DEC': 12
}

# word conversions for days of the week
days = {
    'SUN': 0, 
    'MON': 1, 
    'TUE': 2,
    'WED': 3, 
    'THU': 4, 
    'FRI': 5,
    'SAT': 6
}

class CronUtils:

    @classmethod
    def handle_range(cls, string, values, datatype):
        """
        INPUT: string = Value of parameter, values = Array of possible values for
        parameter, datatype = Type of the parameter.
        OUTPUT: String of all values in the range given. If word form was used
        (e.g. JAN instead of 1), it returns a word-formatted range.
        """
        start, end = string.split('-')
        try:
            start, end = int(start), int(end)
        except ValueError:
            # try:
            #     start, end = values.index(start), values.index(end)
            #     return ' '.join(values[start:end + 1])
            # except ValueError:
            raise Exception('{} input combination is not valid. Please use either string or number syntax.'.format(datatype))
        if start not in values[datatype] or end not in values[datatype] or start > end:
            raise Exception('{} input combination is not within the proper range. Please check.'.format(datatype))
        return ' '.join(map(str, [i for i in range(start, end + 1)]))

    @classmethod
    def handle_intervals(cls, string, values, datatype):
        """
        INPUT: string = Value of parameter, values = Array of possible value for
        parameter.
        OUTPUT: String of all the values matching the specified interval in the
        possible range.
        """
        first, second = string.split("/")
        if first == "*":
            if int(second) not in values:
                raise Exception('{} input combination is not within the proper range. Please check.'.format(datatype))
            return ' '.join(
                map(str, [i for i in values
                    if i % int(second) == 0])
                )
        try:
            first = int(first)
            second = int(second)
        except Exception as e:
            raise Exception(f"Exception occured in handle_intervals = {e}")
        if first not in values or second not in values:
            raise Exception('{} input combination is not within the proper range. Please check.'.format(datatype))
        return ' '.join(
            map(str, [i for i in range(first, values[-1]+1, second)])
            )

class StandardCronDisplay:

    @classmethod
    def display_cron(cls, expanded_minute_parameter, expanded_hour_parameter, expanded_day_of_month_parameter, 
                        expanded_month_parameter, expanded_day_of_week_parameter, user_command):
        print('\n'.join([
            "minutes ".ljust(14,' ') + "{}".format(expanded_minute_parameter),
            "hours ".ljust(14,' ') + "{}".format(expanded_hour_parameter),
            "day of month ".ljust(14,' ') + "{}".format(expanded_day_of_month_parameter),
            "month ".ljust(14,' ') + "{}".format(expanded_month_parameter),
            "day of Week ".ljust(14,' ') + "{}".format(expanded_day_of_week_parameter),
            "command ".ljust(14,' ') + "{}".format(user_command),
        ]))

class BaseCronParserClass:

    minute_parameter = ""
    hour_parameter = ""
    day_of_month_parameter = ""
    month_parameter = ""
    day_of_week_parameter = ""
    user_command = ""
    display_class = None

    def describe_minute_parameter(self, minute_parameter=None):
        if not minute_parameter:
            minute_parameter = self.minute_parameter
        if minute_parameter == "*":
            return ' '.join(map(str, values['minute']))

        if "," in minute_parameter:
            multiple_parameters = minute_parameter.split(',')
            complete_minute_response = None
            for par in multiple_parameters:
                single_response = self.describe_minute_parameter(par)
                if single_response:
                    if not complete_minute_response:
                        complete_minute_response = single_response
                    else:
                        complete_minute_response = complete_minute_response + ' ' + single_response
            complete_data = [int(x) for x in complete_minute_response.split(' ')]
            # removing duplicates some online cron explainers do not do this. example: https://crontab.guru/
            complete_data = list(set(complete_data)) 
            complete_data.sort()
            minute_parameter = ' '.join(map(str, complete_data))
            return minute_parameter

        # handle ranges
        elif "-" in minute_parameter:
            return CronUtils.handle_range(minute_parameter, values, datatype='minute')

        # handle intervals
        elif "/" in minute_parameter:
            return CronUtils.handle_intervals(minute_parameter, values['minute'], datatype='minute')

        if int(minute_parameter) in values['minute']:
            return minute_parameter 
        raise Exception('{} minute parameter is not valid. Please check')

    def describe_hour_parameter(self, hour_parameter=None):
        if not hour_parameter:
            hour_parameter = self.hour_parameter
        if hour_parameter == "*":
            return ' '.join(map(str, values['hour']))

        if "," in hour_parameter:
            multiple_parameters = hour_parameter.split(',')
            complete_hour_response = None
            for par in multiple_parameters:
                single_response = self.describe_hour_parameter(par)
                if single_response:
                    if not complete_hour_response:
                        complete_hour_response = single_response
                    else:
                        complete_hour_response = complete_hour_response + ' ' + single_response
            complete_data = [int(x) for x in complete_hour_response.split(' ')]
            complete_data = list(set(complete_data))
            complete_data.sort()
            hour_parameter = ' '.join(map(str, complete_data))
            return hour_parameter

        # handle ranges
        elif "-" in hour_parameter:
            return CronUtils.handle_range(hour_parameter, values, datatype='hour')

        # handle intervals
        elif "/" in hour_parameter:
            return CronUtils.handle_intervals(hour_parameter, values['hour'], datatype='hour')

        if int(hour_parameter) in values['hour']:
            return hour_parameter 
        raise Exception('{} hour parameter is not valid. Please check')

    def describe_day_of_month_parameter(self, day_of_month_parameter=None):
        if not day_of_month_parameter:
            day_of_month_parameter = self.day_of_month_parameter
        if day_of_month_parameter == "*":
            return ' '.join(map(str, values['day']))

        if "," in day_of_month_parameter:
            multiple_parameters = day_of_month_parameter.split(',')
            complete_day_of_month_response = None
            for par in multiple_parameters:
                single_response = self.describe_day_of_month_parameter(par)
                if single_response:
                    if not complete_day_of_month_response:
                        complete_day_of_month_response = single_response
                    else:
                        complete_day_of_month_response = complete_day_of_month_response + ' ' + single_response
            complete_data = [int(x) for x in complete_day_of_month_response.split(' ')]
            complete_data = list(set(complete_data))
            complete_data.sort()
            day_of_month_parameter = ' '.join(map(str, complete_data))
            return day_of_month_parameter

        # handle ranges
        elif "-" in day_of_month_parameter:
            return CronUtils.handle_range(day_of_month_parameter, values, datatype='day')

        # handle intervals
        elif "/" in day_of_month_parameter:
            return CronUtils.handle_intervals(day_of_month_parameter, values['day'], datatype='day')

        if int(day_of_month_parameter) in values['day']:
            return day_of_month_parameter 
        raise Exception('{} day of month parameter is not valid. Please check')

    def describe_month_parameter(self, month_parameter=None):
        if not month_parameter:
            month_parameter = self.month_parameter
        if month_parameter == "*":
            return ' '.join(map(str, values['month']))

        if "," in month_parameter:
            multiple_parameters = month_parameter.split(',')
            complete_month_response = None
            for par in multiple_parameters:
                single_response = self.describe_month_parameter(par)
                if single_response:
                    if not complete_month_response:
                        complete_month_response = single_response
                    else:
                        complete_month_response = complete_month_response + ' ' + single_response
            complete_data = [int(x) for x in complete_month_response.split(' ')]
            complete_data = list(set(complete_data))
            complete_data.sort()
            month_parameter = ' '.join(map(str, complete_data))
            return month_parameter

        # handle ranges
        elif "-" in month_parameter:
            start, end = month_parameter.split('-')
            if (start in months.keys()) and (end in months.keys()):
                start = months[start]
                end = months[end]
                month_parameter = str(start)+'-'+str(end)
            return CronUtils.handle_range(month_parameter, values, datatype='month')

        # handle intervals
        elif "/" in month_parameter:
            start, end = month_parameter.split('/')
            if (start in months.keys()) and (end in months.keys()):
                start = months[start]
                end = months[end]
                month_parameter = str(start)+'/'+str(end)
            return CronUtils.handle_intervals(month_parameter, values['month'], datatype='month')

        if month_parameter in months.keys():
            return str(months[month_parameter])

        if int(month_parameter) in values['month']:
            return month_parameter 
        raise Exception('{} month parameter is not valid. Please check')

    def describe_day_of_week_parameter(self, day_of_week_parameter=None):
        if not day_of_week_parameter:
            day_of_week_parameter = self.day_of_week_parameter
        if day_of_week_parameter == "*":
            return ' '.join(map(str, values['week']))

        if "," in day_of_week_parameter:
            multiple_parameters = day_of_week_parameter.split(',')
            complete_week_response = None
            for par in multiple_parameters:
                single_response = self.describe_day_of_week_parameter(par)
                if single_response:
                    if not complete_week_response:
                        complete_week_response = single_response
                    else:
                        complete_week_response = complete_week_response + ' ' + single_response
            complete_data = [int(x) for x in complete_week_response.split(' ')]
            complete_data = list(set(complete_data))
            complete_data.sort()
            day_of_week_parameter = ' '.join(map(str, complete_data))
            return day_of_week_parameter

        # handle ranges
        elif "-" in day_of_week_parameter:
            start, end = day_of_week_parameter.split('-')
            if (start in days.keys()) and (end in days.keys()):
                start = days[start]
                end = days[end]
                day_of_week_parameter = str(start)+'-'+str(end)
            return CronUtils.handle_range(day_of_week_parameter, values, datatype='week')

        # handle intervals
        elif "/" in day_of_week_parameter:
            start, end = day_of_week_parameter.split('/')
            if (start in days.keys()) and (end in days.keys()):
                start = days[start]
                end = days[end]
                day_of_week_parameter = str(start)+'/'+str(end)
            return CronUtils.handle_intervals(day_of_week_parameter, values['week'], datatype='week')

        if day_of_week_parameter in days.keys():
            return str(days[day_of_week_parameter])

        if int(day_of_week_parameter) in values['week']:
            return day_of_week_parameter 
        raise Exception('{} day of week parameter is not valid. Please check')

    @abstractmethod
    def describe_expression(self):
        pass
        
    @abstractmethod
    def describe_expression(self):
        pass

class FiveParamterCronParserService(BaseCronParserClass):

    def __init__(self, parameters, user_command, display_type):
        self.minute_parameter = parameters[0]
        self.hour_parameter = parameters[1]
        self.day_of_month_parameter = parameters[2]
        self.month_parameter = parameters[3]
        self.day_of_week_parameter = parameters[4]
        self.user_command = user_command
        self.display_class = get_display_class(display_type)

    def describe_expression(self):
        minute_described = self.describe_minute_parameter(),
        minute_described = minute_described[0]
        hour_described = self.describe_hour_parameter(), 
        hour_described = hour_described[0]
        day_of_month_described = self.describe_day_of_month_parameter(), 
        day_of_month_described = day_of_month_described[0]
        month_described = self.describe_month_parameter(), 
        month_described = month_described[0]
        day_of_week_described = self.describe_day_of_week_parameter(), 
        day_of_week_described = day_of_week_described[0]
        user_command = self.user_command
        self.display_class.display_cron(minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command)
        return minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command


length_to_class_mapping = {
    5: FiveParamterCronParserService,
    # 7: SevenParamterCronParserService
}

cron_display_class_mapping = {
    "standard_display": StandardCronDisplay,
    # "Customized_display": CustomizedCronDisplay
}

def get_class(no_of_parameters):
    return length_to_class_mapping.get(no_of_parameters)

def get_display_class(key):
    return cron_display_class_mapping.get(key)

def cron_parser(input):
    parameters = input.split(' ')
    no_of_parameters = len(parameters) - 1

    user_command = parameters[-1]
    parameters = parameters[:-1]
    
    parser_class = get_class(no_of_parameters)

    if parser_class is None:
        raise Exception('Please check the number of paramters sent to the cron parser')

    parser_obj = parser_class(parameters, user_command, "standard_display")

    return parser_obj.describe_expression()

def main():
    cron_parser(argv[1])


if __name__ == '__main__':
    main()
