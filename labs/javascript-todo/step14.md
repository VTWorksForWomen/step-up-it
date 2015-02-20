---
layout: todo
title: Javascript To Do App - Step 14 - Add a Delete Button
permalink: /labs/javascript-todo/step14/
menu_hide: 1
codepen_slug: XJEKpd
---

1. Lets add a delete button in the form of an X to the HTML for each of our tasks
2. To begin lets move our code that builds the HTML for a checkbox into a function called buildTaskHtml. Our function should accept a single argument, the task, and return the HTML to display the task
3. Inside the buildTaskHtml, return a string of HTML that looks like this
<div class=”task”>Task Name <button value=”4” class=”btn-remove-task”>X</button></div>
Be sure to insert the task.name and to set the value of the button to the task.id
4. Inside of the for loop in our renderTaskList function, we will now call our buildTaskHTML function to generate the html for our task list. Replace the contents of the for loop with:
var task = tasks[i];
taskListElement.innerHTML += buildTaskHtml(task);
5. Now all of our logic for how to build the html for a task is contained in a function, making it easier to locate and update
