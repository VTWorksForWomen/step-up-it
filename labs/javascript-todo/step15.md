---
layout: todo
title: Javascript To Do App - Step 15 - Add Delete Event Handler
permalink: /labs/javascript-todo/step15/
menu_hide: 1
codepen_slug: JoLKEW
---

1. Now that we have a way of removing tasks based on their id and we have added a delete button to each task, we can add an event handler that is triggered when the user clicks on the delete button and pulls the task id from the button’s value attribute and passes it to the remove method
<div class=”task”>Task #1 <button value=”1” class=”btn-remove-task”>X</button></div>
taskList.remove(1);
2. Create a new function called onRemoveTaskClick which accepts a single argument called event
3. Inside our new function`, console.log the value of the event variable which is an object that contains information about the click event that occurred, including which element was clicked
4. Call the addEventListener method of our taskListElement with 2 arguments: the string ‘click’ and our onRemoveTaskClick function. This tells the taskListElement that when clicks occur within it that it should call the onRemoveTaskClick function
5. Click on the text of the task and look at the event object that was logged to the console. Expand the object and look at the information that it provides. Look at the target property, which is set to div.task. This is because we clicked on the div tag which contains the task, which has a class of task applied to it from our buildTaskHtml function
6. Click on the X button for the task and look at the event object that was logged to the console. Expand the object and look at the information that it provides. Look at the target property, which is set to button.btn-remove-task. This is because we clicked on the button tag, which has a class of btn-remove-task applied to it from our buildTaskHtml function
7. We only want to remove the task if the user clicked on the button with the class of btn-remove-task so we will check if the event.target has a class of btn-remove-task. You can check if an HTML element has a class by using its classList property, which is an object that lets you manage classes for the tag.
8. Lets experiment with the classList object to add/remove classes on the body tag and check if they are there. Open the console in your browser
    1. Type document.body into the console to select the body tag
    2. Call the document.body.classList.add method with a class name to add to the body tag, try the string ‘test’
    3. Type document.body into the console to see the body tag again, it should include your ‘test’ class
    4. Call the document.body.classList.contains method with ‘test’ as the argument, this will return true because the body does have that class (we just added it)
    5. Call the document.body.classList.remove method with ‘test’ as the argument to remove the test class from the body tag
    6. Type document.body into the console to see the body tag again, it should no longer include your ‘test’ class
    7. Call the document.body.classList.contains method with ‘test’ as the argument, this will return false because the body does have that class (we just removed it)
1. Back in our onRemoveTaskClick function, add an if statement that calls event.target.classList.contains to check if the html element the user clicked on contains the class btn-remove-task. If it does, then the user clicked on the remove task button and we need to remove the task. Inside your if statement, console.log(‘Remove it’) and test to see if you see the message in the console when clicking the button but not when clicking the task text
2. Change ‘Remove it’ to event.target.value, which should be the value attribute of the remove button, which contains the id of the task to remove. Check if you see this number logged to the console when you click the button
3. Replace the console.log call with a call to the remove method of the taskList object, passing in event.target.value as the only argument. This passes the id of the task to the remove method and removes it from the task list
4. Click on the button to remove a task. You will notice that nothing happened. This is because we need to re-render the task list after removing the item. Inside our onRemoveTaskClick function at the very end add a call to renderTaskList passing in the taskListElement and taskList variables as arguments
