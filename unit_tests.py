import unittest
from cron_parser import cron_parser

# I am editing this so that it can be at the top of the folder.

class TestCronParser(unittest.TestCase):

    # POSITIVE TEST CASESE

    def test_basic(self):
        test_input = "* * * * * /usr/bin/find"
        minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        self.assertEqual(minute_described, '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59')
        self.assertEqual(hour_described, '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23')
        self.assertEqual(day_of_month_described, '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31')
        self.assertEqual(month_described, '1 2 3 4 5 6 7 8 9 10 11 12')
        self.assertEqual(day_of_week_described, '0 1 2 3 4 5 6')

    def test_multiple_and_range_and_intervals(self):
        test_input = "1,2,5-9,40/5,30,50 0-5,8,18/2 1-5,10/5 JAN/FEB,12 0,TUE/TUE /usr/bin/find"
        minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        self.assertEqual(minute_described, '1 2 5 6 7 8 9 30 40 45 50 55')
        self.assertEqual(hour_described, '0 1 2 3 4 5 8 18 20 22')
        self.assertEqual(day_of_month_described, '1 2 3 4 5 10 15 20 25 30')
        self.assertEqual(month_described, '1 3 5 7 9 11 12')
        self.assertEqual(day_of_week_described, '0 2 4 6')


    # NEGATIVE TEST CASES

    # WRONG INPUT LENGTH

    def test_wrong_input_length_1(self):
        test_input = "* * * * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'Please check the number of paramters sent to the cron parser')

    def test_wrong_input_length_2(self):
        test_input = "* * * * * * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'Please check the number of paramters sent to the cron parser')


    # WRONG VALUE FOR MINUTE

    def test_wrong_value_for_minute(self):
        test_input = "1,2,60 * * * * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), '{} minute parameter is not valid. Please check')

    def test_wrong_range_for_minute_1(self):
        test_input = "5-3 * * * * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'minute input combination is not within the proper range. Please check.')

    def test_wrong_range_for_minute_2(self):
        test_input = "6-70 * * * * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'minute input combination is not within the proper range. Please check.')

    def test_wrong_interval_for_minute_1(self):
        test_input = "60/5 * * * * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'minute input combination is not within the proper range. Please check.')

    def test_wrong_interval_for_minute_2(self):
        test_input = "40/60 * * * * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'minute input combination is not within the proper range. Please check.')


    # WRONG VALUE FOR HOUR

    def test_wrong_value_for_hour(self):
        test_input = "1,2 24 * * * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), '{} hour parameter is not valid. Please check')

    def test_wrong_range_for_hour_1(self):
        test_input = "5-10 20-10 * * * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'hour input combination is not within the proper range. Please check.')

    def test_wrong_range_for_hour_2(self):
        test_input = "5-10 15-25 * * * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'hour input combination is not within the proper range. Please check.')

    def test_wrong_interval_for_hour_1(self):
        test_input = "30/5 25/5 * * * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'hour input combination is not within the proper range. Please check.')

    def test_wrong_interval_for_hour_2(self):
        test_input = "40/2 10/25 * * * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'hour input combination is not within the proper range. Please check.')


    # WRONG VALUE FOR DAY OF MONTH

    def test_wrong_value_for_day_of_month(self):
        test_input = "1,2 20 32 * * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), '{} day of month parameter is not valid. Please check')

    def test_wrong_range_for_day_of_month_1(self):
        test_input = "5-10 5-10 20-10 * * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'day input combination is not within the proper range. Please check.')

    def test_wrong_range_for_day_of_month_2(self):
        test_input = "5-10 15-20 20-35 * * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'day input combination is not within the proper range. Please check.')

    def test_wrong_interval_for_day_of_month_1(self):
        test_input = "30/5 10/5 35/3 * * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'day input combination is not within the proper range. Please check.')

    def test_wrong_interval_for_day_of_month_2(self):
        test_input = "40/2 10/20 20/35 * * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'day input combination is not within the proper range. Please check.')


    # WRONG VALUE FOR MONTH

    def test_wrong_value_for_month_1(self):
        test_input = "1,2 20 20 JEB * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), "invalid literal for int() with base 10: 'JEB'")

    def test_wrong_value_for_month_2(self):
        test_input = "1,2 20 20 0 * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), '{} month parameter is not valid. Please check')

    def test_wrong_range_for_month_1(self):
        test_input = "5-10 5-10 2-10 JUN-FEB * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'month input combination is not within the proper range. Please check.')

    def test_wrong_range_for_month_2(self):
        test_input = "5-10 5-10 2-10 6-1 * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'month input combination is not within the proper range. Please check.')

    def test_wrong_range_for_month_3(self):
        test_input = "5-10 5-10 2-10 6-AUG * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'month input combination is not valid. Please use either string or number syntax.')

    def test_wrong_range_for_month_4(self):
        test_input = "5-10 15-20 20-30 JAN-FEN * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'month input combination is not valid. Please use either string or number syntax.')

    def test_wrong_range_for_month_5(self):
        test_input = "5-10 5-10 2-10 6-13 * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'month input combination is not within the proper range. Please check.')

    def test_wrong_interval_for_month_1(self):
        test_input = "30/5 10/5 15/3 13/2 * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'month input combination is not within the proper range. Please check.')

    def test_wrong_interval_for_month_2(self):
        test_input = "30/5 10/5 15/3 1/22 * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'month input combination is not within the proper range. Please check.')

    def test_wrong_interval_for_month_3(self):
        test_input = "40/2 10/20 25/3 2/FEB * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), "Exception occured in handle_intervals = invalid literal for int() with base 10: 'FEB'")

    def test_wrong_interval_for_month_4(self):
        test_input = "40/2 10/20 25/3 FAR/MAR * /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), "Exception occured in handle_intervals = invalid literal for int() with base 10: 'FAR'")


    # WRONG VALUE FOR DAY OF WEEK

    def test_wrong_value_for_day_of_week_1(self):
        test_input = "1,2 20 20 JAN SNA /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), "invalid literal for int() with base 10: 'SNA'")

    def test_wrong_value_for_day_of_week_2(self):
        test_input = "1,2 20 20 2 7 /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), '{} day of week parameter is not valid. Please check')

    def test_wrong_range_for_day_of_week_1(self):
        test_input = "5-10 5-10 2-10 JAN-FEB WED-SUN /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'week input combination is not within the proper range. Please check.')

    def test_wrong_range_for_day_of_week_2(self):
        test_input = "5-10 5-10 2-10 2-4 6-1 /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'week input combination is not within the proper range. Please check.')

    def test_wrong_range_for_day_of_week_3(self):
        test_input = "5-10 5-10 2-10 6-10 SUN-4 /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'week input combination is not valid. Please use either string or number syntax.')

    def test_wrong_range_for_day_of_week_4(self):
        test_input = "5-10 15-20 20-30 JAN-FEB SUN-MAN /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'week input combination is not valid. Please use either string or number syntax.')

    def test_wrong_range_for_day_of_week_5(self):
        test_input = "5-10 5-10 2-10 6-11 2-8 /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'week input combination is not within the proper range. Please check.')

    def test_wrong_interval_for_day_of_week_1(self):
        test_input = "30/5 10/5 15/3 3/2 7/3 /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'week input combination is not within the proper range. Please check.')

    def test_wrong_interval_for_day_of_week_2(self):
        test_input = "30/5 10/5 15/3 1/2 3/8 /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), 'week input combination is not within the proper range. Please check.')

    def test_wrong_interval_for_day_of_week_3(self):
        test_input = "40/2 10/20 25/3 2/2 2/TUE /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), "Exception occured in handle_intervals = invalid literal for int() with base 10: 'TUE'")

    def test_wrong_interval_for_day_of_week_4(self):
        test_input = "40/2 10/20 25/3 FEB/MAR SIN/TUE /usr/bin/find"
        try:
            minute_described, hour_described, day_of_month_described, month_described, day_of_week_described, user_command = cron_parser(test_input)
        except Exception as e:
            self.assertEqual(str(e), "Exception occured in handle_intervals = invalid literal for int() with base 10: 'SIN'")

if __name__ == '__main__':
    unittest.main()
