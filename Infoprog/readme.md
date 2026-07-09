# Infoprog

## Description

Infoprog is a programming exercise originally based on a competition task.
This repository contains a later free-time recreation of the project, not the original competition submission.

The goal of the project was to practice working with event records, dates, editing functionality and command-line interaction.

## Current Features

  * Command-line Interface (CLI)
  * Event creation
  * Event editing
  * Event deletion with confirmation
  * Event sorting by date and start time
  * Event listing/display
  * Basic input handling
  * Object-oriented structure using an `Event` class

## CLI Menu Explanation

The user can choose from these options:

### 1 - Write out events

Displays:

 * All events sorted by date from oldest to newest.
 * All attributes are listed and separated by `;`.
 * All events are numbered from `1` and this number is used for the other operations.

### 2 - Search for events by date

The user enters a date and the program displays:
 * All events for that date sorted from oldest to newest.
 * All events are numbered from `1`, but this number shouldn't be used with the other operations.

### 3 - Add new event

The user is asked to enter:
 * Start time (HH:MM).
 * End time (HH:MM).
 * Date (DD:MM:YYYY).
 * Note/text - a short note that can't exceed the `250` character limit.

### 4 - Edit event

 * The user is asked to enter the number of the event to be edited.
 * The user is then asked what to edit.
 * Only one attribute can be edited at one time.

### 5 - Delete event

 * The user is asked to enter the number of the event to be deleted.
 * The user is then asked to confirm the deletion.

## How Event Creation Works

`Start` and `End` time must satisfy:
 * Time format used must be `HH:MM`.
 * `Start` time must be sooner than `End` time.
 * `End` time must be later than `Start` time.
 * If not satisfied the user will be asked to correct one of the times to satisfy the requirement.

`Date` must follow:
 * Date format must be `DD:MM:YYYY`.
 * If the date is incorrect, the user will be asked to enter a correct date.

`Note` must follow:
 * The length of the text can't exceed `250` characters.
 * If the text length exceeds the `250` character limit, the user will be asked to enter a new note.

Creation flow:
 * The user is asked to enter the start time, end time, date and note, in this order.
 * If any of them are incorrect the user will be asked to reenter that attribute before moving on.
 * The `Event` object is created.
 * Added to the list of events.
 * The event list is sorted.
 * The event list is saved to the `events.txt` file.

## How Event Editing Works

 * The same rules apply to the attributes when editing events.
 * User has to enter a valid event number, which is acquired by using option `1`.
 * If the event number is incorrect the user will be asked again, until it's correct.
 * Then the user has to choose which attribute to edit.
 * If the option is incorrect the user is asked again.
 * The user can `Exit` if needed without any changes.
 * If an option was chosen the user has to enter the correct format for the attribute to edit the event.
 * The event attribute is edited.
 * The event list is sorted.
 * The event list is saved to the `events.txt` file.

## How Event Deletion Works

 * User has to enter a valid event number, which is acquired by using option `1`.
 * If the event number is incorrect the user will be asked again, until it's correct.
 * The user is asked if they want to delete the event.
 * If `No` is chosen, the user is returned to the main interface and nothing will be deleted.
 * If `Yes` is chosen, the event will be deleted from the event list.
 * The event list is saved to the `events.txt` file.

## How Events are Saved

* When creating an event for the first time the program will create a file named `events.txt`.
* The event attributes are separated by a `;` and the events occupy one line each.
* Events are saved after every change (event creation, editing and deletion), the file is rewritten.

## How Events are Loaded

* When the program is started, it reads the `events.txt` file line by line and recreates the `Event` objects using the `;` separator.
* Events are saved into a `list`.

## How to Run

Change the working directory to the project folder:

```bash
cd Infoprog
```

Run the program:

```bash
python main.py
```

On Windows, this also works:

```bash
python .\main.py
```

## How to Run Tests

Change the working directory to the project folder:

```bash
cd Infoprog
```

Run all tests:

```bash
python -m unittest
```

Or run the test file directly:

```bash
python test_event_modules.py
```

On Windows, this also works:

```bash
python .\test_event_modules.py
```

## Known Limitations

  * This version is a later recreation and may differ from the original competition solution.
  * Some parts of the structure reflect an earlier stage of my programming experience.
  * The project would benefit from refactoring before being expanded further.
  * The whole `events.txt` file is rewritten after every change. This is acceptable for a small text-file project, but it would not scale well for larger data.

## Testing notes

 * The project contains tests for some core behavior.
 * The test suite is not complete yet.
 * Some important edge cases are probably missing.
 * Future improvements should include more modular tests, reusable setup helpers and additional cases for invalid input, editing, sorting and missing functionality.

## Possible Future Improvements

  * Improve project structure
  * Improve input validation
  * Add and update unit tests
  * Separate UI logic from event-handling logic more clearly
  * More unit test cases, reusable setup helpers and modular tests

## Status

Completed. This is a recreated version of an earlier competition exercise and further improvements are planned.
