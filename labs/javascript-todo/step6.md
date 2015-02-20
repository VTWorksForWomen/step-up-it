---
layout: todo
title: Javascript To Do App - Step 6 - Task Constructor
permalink: /labs/javascript-todo/step6/
menu_hide: 1
codepen_slug: QwmLwa
---

1. Since creating objects with some initial values is such a common task, javascript and most languages provide a shortcut. A function that creates an object is generally called a constructor. Inside of a constructor you can use the special this variable to refer to the object being created (the task).
2. Change the name of createTask function to Task
3. Inside the body set this.name to the name and this.is_complete = false
4. Change calls to createTask to new Task(‘Task name’)
