---
layout: todo
title: Javascript To Do App - Step 9 - Add Task to the List
permalink: /labs/javascript-todo/step9/
menu_hide: 1
codepen_slug: xbWKKe
---

1. At the end of our onNewTaskFormSubmit function, add the newly created task to the task list by calling the tasks.push method and passing in our newTask variable
2. Use console.log to view the value of the tasks variable
3. Why dont we see our new task in the HTML? Its because the HTML was already rendered when the page load. We need to re-render the HTML again when the task is added. We could copy the entire for loop into our onNewTaskFormSubmit function but that would be messy. Lets wrap it into a function called renderTasks
4. Create a function called renderTasks which task 2 arguments: taskListElement (the HTML element to render the task list to) and tasks (an array of tasks). Make sure you place the numTasks variable inside this function. 
5. Our task list disappears on page load because this code is no longer being run. We need to add a call to renderTasks at the very bottom of our javascript. Call renderTasks and pass in the taskListElement and the tasks array
6. Now we want to also render the task list when a new task is added, so copy the call to renderTasks to the bottom of our onNewTaskFormSubmit function
7. Try to add a new task, it duplicated our task list! We need to make sure we clear out the task list HTML when we begin rendering. On the first line of the renderTasks function add code that will set the innerHTML of the taskListElement to an empty string
8. Finally lets reset the form after submitting so the text field will be emptied. At the end of onNewTaskFormSubmit add a call to this.reset(); remember that this refers to the html element on which the event is occurring so in this case its the <form> tag. form tags have a special method called reset() which resets all of their fields to their original values
