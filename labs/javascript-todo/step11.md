---
layout: todo
title: Javascript To Do App - Step 11 - Create an add method for our taskList
permalink: /labs/javascript-todo/step11/
menu_hide: 1
codepen_slug: qEoZYO
---

1. As we have seen objects can have properties. For example tasks have a name property (task.name) and an is_complete property (task.is_complete). They can also have functions associated with them, which are called methods. For example array objects have a push method that lets you add items to them. Try this code in the console to see an example. 
  1. var tasks = [‘Task 1’, ‘Task 2’]; 
     tasks.length; 
     tasks.push(‘Task 3’); 
     tasks.length;
1. We can add methods any task lists we create by adding a function to the prototype of the TaskList function we created. TaskList.prototype.add = function() {}. Add a function called add to the TaskList’s prototype. It should accept 1 argument: a task.
2. Within the body of a method we can refer to the current task list using the this variable. Call the push method of this.tasks and pass in the task to add the task to the list.
3. Lets use our new method to add another task to our list. Right after we create our task list with new TaskList() add a line that calls the add method of taskList, passing in new Task(‘Another task’). You should now see our new task displayed in the task list
4. In the onNewTaskFormSubmit function, lets use our new add method to add the task instead of calling tasks.push directly

