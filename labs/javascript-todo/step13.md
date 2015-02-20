---
layout: todo
title: Javascript To Do App - Step 13 - Add TaskList.remove method
permalink: /labs/javascript-todo/step13/
menu_hide: 1
codepen_slug: Ggxqjd
---


1. Add a method called remove to the TaskList prototype just like we did earlier with the add function. The remove function should accept a single argument: id, which is the id of the task to remove
2. There are a nubuildmber of different ways to remove an item from an array. Perhaps the easiest is to create a new array that only include the items you want. Inside the remove function, create a variable called newTasks and assign it a value of an empty array (e.g. [])
3. Create a for loop to loop over each of the tasks for the current task list using this.tasks, remember that the this variable refers to the current task list. You can look at the code for renderTaskList function see how we loop over the tasks
4. Within the body of the loop, create a variable called task and assign it the value of the current task.id in the loop
5. Use console.log to inspect the value of task.id as well as the id that was passed into the function
6. If the id of the current task is not equal to the id that was passed into the remove function, then use the push method of the newTasks array to add the task to the newTask array
7. Outside of the for loop, set this.tasks equal to the newTasks variable, which no longer contains the task with the id that we wanted to remove
8. In the console, Experiment with the new remove method of the TaskList by creating a task list, adding a few tasks and removing those tasks
var taskList = new TaskList(‘My List’, []);
taskList.add(new Task(‘Item 1’))
taskList.add(new Task(‘Item 2’))
taskList
taskList.tasks
taskList.tasks[0]
taskList.remove(taskList.tasks[0].id)
taskList.tasks
taskList.tasks.length
