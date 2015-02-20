---
layout: todo
title: Javascript To Do App - Step 10 - Give your task list a name
permalink: /labs/javascript-todo/step10/
menu_hide: 1
codepen_slug: radepb
---

1. Define a function for creating a new task list called TaskList which takes 2 arguments: name and tasks
2. Inside the function set this.name equal to the name
3. Inside the function set this.tasks equal to the tasks
4. In the console, try creating a new task list by running the code new TaskList(‘My Task List’, [new Task(‘A task’)]) to see what is created
5. Below the variable tasks where we create our array of tasks, create a new TaskList passing in the name ‘My Task List’ and as well as the tasks variable assign it to the variable taskList
6. Rename our function renderTasks to renderTaskList and change the secondary argument name from tasks to taskList
7. On the first line Inside the renderTaskList function, create a variable called tasks and assign it to taskLists.tasks
8. There are 2 places in our code where we are calling renderTasks. Change them both to call renderTaskList instead and change the second argument from tasks to taskList to pass in the taskList object instead of the tasks themselves
9. Inside our renderTaskList function on the line where we create the heading, add the name of the task list to the heading by referencing taskList.name so the heading displays ‘My Task List: There are X tasks’
