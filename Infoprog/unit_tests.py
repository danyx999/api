import unittest
from event import Event
from event_checker import EventChecker
from event_handler import EventHandler


class EventCheckerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.target = EventChecker()

    def test_CheckTextLength_WhenTextIsLongerThanMaxTextLength_ReturnsFalse(
        self,
    ) -> None:
        text = 251 * "1"

        self.assertFalse(self.target.CheckTextLength(text))

    def test_CheckTextLength_WhenTextIsShorterThanMaxTextLength_ReturnsTrue(
        self,
    ) -> None:
        text = 249 * "1"

        self.assertTrue(self.target.CheckTextLength(text))

    def test_CheckDate_WhenDateIsIncorrect_ReturnsFalse(self) -> None:
        date1 = "29.2.2023"
        date2 = "6-6-2023"
        date3 = "90.6.2023"

        self.assertFalse(self.target.CheckDate(date1))
        self.assertFalse(self.target.CheckDate(date2))
        self.assertFalse(self.target.CheckDate(date3))

    def test_CheckDate_WhenDateIsCorrect_ReturnsTrue(self) -> None:
        date = "6.6.2006"

        self.assertTrue(self.target.CheckDate(date))

    def test_CheckTime_WhenTimeIsIncorrect_ReturnsFalse(self) -> None:
        time1 = "10:61"
        time2 = "25:00"
        time3 = "12;15"

        self.assertFalse(self.target.CheckTime(time1))
        self.assertFalse(self.target.CheckTime(time2))
        self.assertFalse(self.target.CheckTime(time3))

    def test_CheckTime_WhenTimeIsCorrect_ReturnsTrue(self) -> None:
        time = "14:00"

        self.assertTrue(self.target.CheckTime(time))

    def test_CompareTimes_WhenEndTimeIsSoonerThanStartTime_ReturnsFalse(self) -> None:
        startTime = "13:45"
        endTime = "13:00"

        self.assertFalse(self.target.CompareTimes(startTime, endTime))

    def test_CompareTimes_WhenEndTimeIsLaterThanEndTime_ReturnsTrue(self) -> None:
        startTime = "14:30"
        endTime = "15:00"

        self.assertTrue(self.target.CompareTimes(startTime, endTime))


class EventTests(unittest.TestCase):
    def setUp(self) -> None:
        self.startTime = "09:00"
        self.endTime = "13:00"
        self.date = "17.10.2023"
        self.text = "Zenit v Programovani"
        self.target = Event(self.startTime, self.endTime, self.date, self.text)

    def test_EventSetUp_WhenEventInformationIsGiven(self) -> None:
        self.assertEqual(self.startTime, self.target.StartTime)
        self.assertEqual(self.endTime, self.target.EndTime)
        self.assertEqual(self.date, self.target.Date)
        self.assertEqual(self.text, self.target.Text)

    def test_CreateEventStr_WhenEventInformationIsGiven_ReturnsString(self) -> None:
        expectedString = "17.10.2023-09:00-13:00-Zenit v Programovani"

        self.assertEqual(self.target.CreateEventStr(), expectedString)


class EventHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.target = EventHandler()


unittest.main()
