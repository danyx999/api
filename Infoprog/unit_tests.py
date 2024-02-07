import unittest
from event import Event
from event_checker import EventChecker
from event_handler import EventHandler
from event_editor import EventEditor
from event_deletor import EventDeletor


class EventCheckerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.target = EventChecker()

    def test_CheckTextLength_WhenTextIsLongerThanMaxTextLength_ReturnsFalse(
        self,
    ) -> None:
        text = 251 * "1"

        self.assertFalse(EventChecker.CheckTextLength(text))

    def test_CheckTextLength_WhenTextIsShorterThanMaxTextLength_ReturnsTrue(
        self,
    ) -> None:
        text = 249 * "1"

        self.assertTrue(EventChecker.CheckTextLength(text))

    def test_CheckDate_WhenDateIsIncorrect_ReturnsFalse(self) -> None:
        date1 = "29.2.2023"
        date2 = "6-6-2023"
        date3 = "90.6.2023"

        self.assertFalse(EventChecker.CheckDate(date1))
        self.assertFalse(EventChecker.CheckDate(date2))
        self.assertFalse(EventChecker.CheckDate(date3))

    def test_CheckDate_WhenDateIsCorrect_ReturnsTrue(self) -> None:
        date = "6.6.2006"

        self.assertTrue(EventChecker.CheckDate(date))

    def test_CheckTime_WhenTimeIsIncorrect_ReturnsFalse(self) -> None:
        time1 = "10:61"
        time2 = "25:00"
        time3 = "12;15"

        self.assertFalse(EventChecker.CheckTime(time1))
        self.assertFalse(EventChecker.CheckTime(time2))
        self.assertFalse(EventChecker.CheckTime(time3))

    def test_CheckTime_WhenTimeIsCorrect_ReturnsTrue(self) -> None:
        time = "14:00"

        self.assertTrue(EventChecker.CheckTime(time))

    def test_CompareTimes_WhenEndTimeIsSoonerThanStartTime_ReturnsFalse(self) -> None:
        startTime = "13:45"
        endTime = "13:00"

        self.assertFalse(EventChecker.CompareTimes(startTime, endTime))

    def test_CompareTimes_WhenEndTimeIsLaterThanEndTime_ReturnsTrue(self) -> None:
        startTime = "14:30"
        endTime = "15:00"

        self.assertTrue(EventChecker.CompareTimes(startTime, endTime))


class EventTests(unittest.TestCase):
    def setUp(self) -> None:
        self.startTime = "09:00"
        self.endTime = "13:00"
        self.date = "17.10.2023"
        self.text = "Zenit v Programovani"
        self.target = Event(self.startTime, self.endTime, self.date, self.text)

    def test_CreateEventStr_WhenEventInformationIsGiven_ReturnsString(self) -> None:
        expectedString = "09:00;13:00;17.10.2023;Zenit v Programovani"

        self.assertEqual(self.target.CreateEventStr(), expectedString)


class EventHandlerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.target = EventHandler()

    def test_CreateEventStrToFile_WhenEventListIsGiven_ReturnsStrToFile(self) -> None:
        events = [
            Event("9:00", "13:00", "17.10.2023", "Zenit v Programovani"),
            Event("17:00", "20:00", "19.10.2023", "Note"),
        ]
        expectedString = (
            "09:00;13:00;17.10.2023;Zenit v Programovani\n17:00;20:00;19.10.2023;Note"
        )

        self.assertEqual(EventHandler.CreateEventStrToFile(events), expectedString)

    def test_CreateEventsFromFile_WhenCorrectStrIsGiven_ReturnsEventList(self) -> None:
        events = (
            "17:00;20:00;19.10.2023;Note\n09:00;13:00;17.10.2023;Zenit v Programovani"
        )
        expectedString1 = "09:00;13:00;17.10.2023;Zenit v Programovani"
        expectedString2 = "17:00;20:00;19.10.2023;Note"

        eventList = EventHandler.CreateEventsFromFile(events)
        self.assertEqual(len(eventList), 2)
        self.assertEqual(eventList[0].CreateEventStr(), expectedString1)
        self.assertEqual(eventList[1].CreateEventStr(), expectedString2)

    def test_CreateEventsFromFile_WhenFileIsEmpty_ReturnsEmptyList(self) -> None:
        events = ""

        eventList = EventHandler.CreateEventsFromFile(events)
        self.assertEqual(len(eventList), 0)
        self.assertEqual(eventList, [])

    def test_SortEventsByDate_WhenCorrectStrIsGiven_ReturnsSortedDateList(
        self,
    ) -> None:
        events = [
            Event("6:53", "14:25", "1.7.2005", "NOTE"),
            Event("12:53", "18:23", "9.10.2001", "NOTE"),
            Event("15:50", "17:30", "10.04.1998", "NOTE"),
        ]

        expectedString1 = "15:50;17:30;10.04.1998;NOTE"
        expectedString2 = "12:53;18:23;09.10.2001;NOTE"
        expectedString3 = "06:53;14:25;01.07.2005;NOTE"

        eventList = EventHandler.SortEventsByDate(events)
        self.assertEqual(len(eventList), 3)
        self.assertEqual(eventList[0].CreateEventStr(), expectedString1)
        self.assertEqual(eventList[1].CreateEventStr(), expectedString2)
        self.assertEqual(eventList[2].CreateEventStr(), expectedString3)

    def test_CreateSearchedDateList_WhenCorrectStrIsGiven_ReturnsSearchedDateList(
        self,
    ) -> None:
        events = [
            Event("6:53", "14:25", "1.7.2005", "NOTE"),
            Event("12:53", "18:23", "9.10.2001", "NOTE"),
            Event("15:50", "17:30", "10.04.1998", "NOTE"),
            Event("7:00", "8:00", "1.7.2005", "NOTE"),
            Event("5:00", "17:00", "15.3.1999", "NOTE"),
        ]

        searchedDate = "1.7.2005"

        expectedString1 = "06:53;14:25;01.07.2005;NOTE"
        expectedString2 = "07:00;08:00;01.07.2005;NOTE"

        eventList = EventHandler.CreateSearchedDateList(events, searchedDate)
        self.assertEqual(len(eventList), 2)
        self.assertEqual(eventList[0].CreateEventStr(), expectedString1)
        self.assertEqual(eventList[1].CreateEventStr(), expectedString2)


class EventEditorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.target = EventEditor()

    def test_EditStartTime_CorrectStrIsGiven_ReturnsEditedEvent(self) -> None:
        eventToEdit = Event("14:00", "15:00", "15.7.2023", "NOTE")
        wantedStartTime = "14:30"

        expectedString = "14:30;15:00;15.07.2023;NOTE"

        editedEvent = EventEditor.EditStartTime(eventToEdit, wantedStartTime)
        self.assertEqual(editedEvent.CreateEventStr(), expectedString)

    def test_EditEndTime_CorrectStrIsGiven_ReturnsEditedEvent(self) -> None:
        eventToEdit = Event("14:00", "15:00", "15.7.2023", "NOTE")
        wantedEndTime = "14:30"

        expectedString = "14:00;14:30;15.07.2023;NOTE"

        editedEvent = EventEditor.EditEndTime(eventToEdit, wantedEndTime)
        self.assertEqual(editedEvent.CreateEventStr(), expectedString)

    def test_EditDate_CorrectStrIsGiven_ReturnsEditedEvent(self) -> None:
        eventToEdit = Event("14:00", "15:00", "15.7.2023", "NOTE")
        wantedDate = "6.6.2006"

        expectedString = "14:00;15:00;06.06.2006;NOTE"

        editedEvent = EventEditor.EditDate(eventToEdit, wantedDate)
        self.assertEqual(editedEvent.CreateEventStr(), expectedString)

    def test_EditNote_CorrectStrIsGiven_ReturnsEditedEvent(self) -> None:
        eventToEdit = Event("14:00", "15:00", "15.7.2023", "NOTE")
        wantedNote = "Different NOTE"

        expectedString = "14:00;15:00;15.07.2023;Different NOTE"

        editedEvent = EventEditor.EditNote(eventToEdit, wantedNote)
        self.assertEqual(editedEvent.CreateEventStr(), expectedString)

    def test_HandleEdit_EventListIsGiven_ReturnsEditedEvent1(self) -> None:
        # Starts with 1
        eventList = [
            Event("14:00", "15:00", "15.7.2023", "NOTE"),
            Event("15:50", "17:30", "10.04.1998", "NOTE"),
            Event("6:53", "14:25", "1.7.2005", "NOTE"),
        ]
        eventNumberToEdit = 2
        mode = 3
        wantedDate = "6.6.2006"

        expectedString3 = "14:00;15:00;15.07.2023;NOTE"
        expectedString2 = "15:50;17:30;06.06.2006;NOTE"
        expectedString1 = "06:53;14:25;01.07.2005;NOTE"

        eventList = EventEditor.HandleEdit(
            eventList, eventNumberToEdit - 1, mode, wantedDate
        )
        self.assertEqual(eventList[0].CreateEventStr(), expectedString1)
        self.assertEqual(eventList[1].CreateEventStr(), expectedString2)
        self.assertEqual(eventList[2].CreateEventStr(), expectedString3)

    def test_HandleEdit_EventListIsGiven_ReturnsEditedEvent2(self) -> None:
        # Starts with 1
        eventList = [
            Event("14:00", "15:00", "15.7.2023", "NOTE"),
            Event("6:53", "14:25", "1.7.2005", "NOTE"),
            Event("15:50", "17:30", "10.04.1998", "NOTE"),
        ]
        eventNumberToEdit = 3
        mode = 3
        wantedDate = "6.6.2006"

        expectedString3 = "14:00;15:00;15.07.2023;NOTE"
        expectedString2 = "15:50;17:30;06.06.2006;NOTE"
        expectedString1 = "06:53;14:25;01.07.2005;NOTE"

        eventList = EventEditor.HandleEdit(
            eventList, eventNumberToEdit - 1, mode, wantedDate
        )
        self.assertEqual(eventList[0].CreateEventStr(), expectedString1)
        self.assertEqual(eventList[1].CreateEventStr(), expectedString2)
        self.assertEqual(eventList[2].CreateEventStr(), expectedString3)


class EventDeletorTests(unittest.TestCase):
    pass


unittest.main()
