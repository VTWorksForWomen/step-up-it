---
layout: todo
title: Javascript To Do App - Step 7 - New Task Form
permalink: /labs/javascript-todo/step7/
menu_hide: 1
codepen_slug: GgQVbZ
---

1. In your HTML Add a form tag above the task-list div with an id of ‘new-task-form’
2. Inside the form add an input with a type of text, a name of ‘task_name’ and a placeholder of ‘Type to add a task’
3. In your javascript use document.getElementById to select the new task form and store it in a variable called newTaskForm
4. Create a function called onNewTaskFormSubmit and put in the body of it a call to alert with the message ‘Submitted’
5. Set up our function to be called whenever the form is submitted. Call the addEventListener method of newTaskForm passing it the first argument ‘submit’ (the name of the event we want to listen to) and the second argument onNewTaskFormSubmit which is the name of our listener function
6. Submit the form and see the alert
