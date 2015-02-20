---
layout: todo
title: Javascript To Do App - Step 8 - Get Task Name
permalink: /labs/javascript-todo/step8/
menu_hide: 1
codepen_slug: jEZggY
---

1. Prevent the form from doing its default action (submitting) by adding an argument called event to the onNewTaskFormSubmit function and calling event.preventDefault(). Now submit the form and notice the page does not refresh.
2. Add a call to console.log which logs the value of the variable called this. What is it? Its the form
3. Add a call to console.log which logs the value of this.task_name. What is it? Its our text input
4. In our console.log, change this.task_name to this.task_name.value. Now we can retrieve the value from the text field
5. Store the task name from the text in a variable called taskName
6. Create a new task with the name by using the new Task(taskName) and store it in a variable called newTask, console.log(newTask) to see our new task with the named we entered
