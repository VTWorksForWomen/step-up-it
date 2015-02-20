---
layout: todo
title: Javascript To Do App - Step 12 - Give our tasks a unique ID
permalink: /labs/javascript-todo/step12/
menu_hide: 1
codepen_slug: MYVyZR
---

1. In order to write a remove method for our taskList that deletes tasks, we need a way to be able to identify which task to delete. We could use the name of the task, but its possible that there could be two tasks on the list with the same name. Lets make sure whenever a new task is created that we assign it a unique number. This is often referred to as an id in programming and serves as a unique non-meaningful identifier for an item
2. Inside our Task function we want to add an id property to our newly created tasks. We need a way to ensure this number is always unique, so we will create a global variable called TASK_ID and start it with a value of 1, which will be our first task’s id. Each time we create a task we will add 1 to this number and that will be the id of our new task. At the very top of the file create a variable named TASK_ID and set the value to 1
3. Inside our Task function we can refer to the new task being created used the this variable. Set this.id equal to TASK_ID. Our first task will have an id of 1
4. If we left it at this then we would end up assigning 1 as the id of all of our tasks. We need to make sure we update TASK_ID to add 1 to it so the next time we create a task it will have a unique id. On the last line inside our Task function, set TASK_ID equal to its current value plus 1.
5. Use the console to create some new tasks and look at the ids being assigned
