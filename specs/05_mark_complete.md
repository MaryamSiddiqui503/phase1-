# Mark Task as Complete/Incomplete Feature Specification

## Overview
The Mark Task as Complete/Incomplete feature enables users to toggle the completion status of tasks. Users select a task by ID, and the system toggles the completed status from True to False or vice versa.

## User Scenario
1. User selects "Mark Task Complete/Incomplete" from the main menu
2. System displays all tasks with their IDs and current completion status
3. System prompts user to enter the task ID to toggle
4. User enters the task ID
5. System validates that the task exists
6. If task doesn't exist: error message is shown, return to menu
7. If task exists: system toggles the completion status
8. System updates the task in memory with the new completion status
9. System displays confirmation message with the updated status

## Functional Requirements
1. **REQ-MARK-001**: The system SHALL display all existing tasks with their IDs and completion status before prompting for selection
2. **REQ-MARK-002**: The system SHALL accept a task ID from user input
3. **REQ-MARK-003**: The system SHALL validate that the specified task exists in memory
4. **REQ-MARK-004**: The system SHALL display an error message if the task ID is invalid/nonexistent
5. **REQ-MARK-005**: The system SHALL toggle the completion status of the selected task
6. **REQ-MARK-006**: The system SHALL update the task in memory with the new completion status
7. **REQ-MARK-007**: The system SHALL preserve all other task properties during status update
8. **REQ-MARK-008**: The system SHALL display confirmation of the status change
9. **REQ-MARK-009**: The system SHALL support toggling from incomplete to complete
10. **REQ-MARK-010**: The system SHALL support toggling from complete to incomplete
11. **REQ-MARK-011**: The system SHALL handle invalid task ID input gracefully
12. **REQ-MARK-012**: The system SHALL provide clear visual indicators of task status in the display

## Acceptance Criteria
1. Given: User has existing tasks in the system
   When: User selects "Mark Task Complete/Incomplete" and enters a valid task ID
   Then: Task completion status is toggled in memory
   And: Confirmation message shows the new status

2. Given: Task is currently marked as incomplete
   When: User toggles the task status
   Then: Task is marked as complete in memory
   And: Change is reflected in future task displays

3. Given: Task is currently marked as complete
   When: User toggles the task status
   Then: Task is marked as incomplete in memory
   And: Change is reflected in future task displays

4. Given: User enters an invalid/nonexistent task ID
   When: User attempts to toggle the task status
   Then: Error message is displayed indicating task not found
   And: No task status is changed
   And: User is returned to main menu

## Success Criteria
- 100% of valid status toggles successfully update the task in memory
- Invalid task IDs are caught and handled with appropriate error messages
- Task completion status correctly toggles between complete/incomplete states
- All other task properties remain unchanged during status updates
- Status change confirmation is clear and accurate

## Edge Cases
- Non-existent task ID
- Empty task list
- Task with special characters in title/description
- Interruption during status toggle (Ctrl+C)

## Assumptions
- The toggle function switches the boolean completion status from True to False or False to True
- Visual indicators for completion status are consistent with the View Tasks feature
- Memory storage supports updating individual task properties
- Status changes are immediately reflected in memory
- Task IDs remain constant during status updates