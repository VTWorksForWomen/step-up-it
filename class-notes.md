---
layout: default
title: Class Notes
permalink: /class-notes/
---

## Class 5: Introduction to HTML

We covered HTML tags and attributes, Brackets and developer tools.

### What's What?

- Web Design
    + The process of planning, structuring and creating a website.
- Web Development
    + The process of programming dynamic web applications (remember, that just means websites).
- Front End
    + The outwardly visible elements of a website or application.
- Back End
    + The inner workings and functionality of a website.

### Anatomy of an HTML element

- Element
    + An individual component of HTML
    + heading, paragraph, list item, table, image, etc
- Tag
    + Marks the beginning and end of an element (usually)
    + `<tagexample>Stuff n Junk </tagexample>`
- Types of elements
    + Container element
        * A paragraph element contains text <p>some text</p>
- Stand alone element
    + Cannot contain anything else
        * `<br>`
        * `<img src="http://placekitten.com/300/350" alt="what else but a kitten">`
- Attribute
    + Provides additional information about an element
        * Class, ID, style, source
    + Goes inside the opening tag, before the right angle bracket (see the img example above)
    + Global attributes are available to all elements
        * <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes" title="Global Attributes">Global Attributes</a>
- Value
    + The value assigned to an attribute
    + The value is in side the quotation marks
        * `<a href="http://google.com" title="Google">Link to Google</a>` in this case both http://google.com and Google are values assigned to the href and title attributes.

### HTML Structure

<img src="../images/html-structure.png" alt="the basic html layout of a page">

- Everything visible on your page goes between the `<body>` tags.
- Nesting
    + Some elements can nest inside another element
    + The first element to open must be the last to close.
        * `<p>I love <a href="https://www.petfinder.com/" title="Pet Finder">puppies</a> so much!</p>` The `<p>` is the first to open and the last to close.

### HTML Elements

We covered a ton of elements! To see all the elements available to you check out the <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element" title="Mozilla Developer Network">Mozilla Developer Network</a>.

- Important points to remember:
    + HTML tags are *not* presentational. They mean something and should be used to appropriately attribute that meaning to content. <a href="http://codepen.io/e-to-the-m/pen/QwMVRX?editors=110" title="An example about semantic HTML at CodePen">Example</a>
    + `<em>` emphasizes text. If your text doesn't need emphasis but just needs to be italic, we will do that with CSS.

- Elements we covered
    + Paragraph `<p>`
    + Headings `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`
    + Emphasized text `<em>`
    + Important text `<strong>`
    + Anchor `<a>`
        * Learn more about relative and absolute paths
            - <a href="http://www.coffeecup.com/help/articles/absolute-vs-relative-pathslinks/" title="Absolute Vs. Relative Paths/Links">Absolute Vs. Relative Paths/Links</a>
            - <a href="http://css-tricks.com/quick-reminder-about-file-paths/" title="Quick Reminder About File Paths">Quick Reminder About File Paths</a>
    + Images `<img>`
        * Remember that the Internet is made up of <del>cats</del> <ins>squares</ins>. <a href="http://codepen.io/e-to-the-m/pen/zyljo?editors=110" title="An illustrative image experiment in CodePen">See an example</a>.
    + Line Break `<br>`
    + Lists
        * Ordered Lists `<ol>`
        * Unordered Lists `<ul>`
        * List Items (for both ordered and unordered lists) `<li>`
    + <a href="https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Sections_and_Outlines_of_an_HTML5_document" title="Sections and Outlines of an HTML5 Document">Sections and Outlines of an HTML5 Document</a>
        * Header `<header>`
        * Navigation `<nav>`
        * Main `<main>`
        * Section `<section>`
            - A logical or thematic grouping of content that usually contains a heading.
        * Article `<article>`
            - A self-contained piece of content. It would still make sense if it was removed from the context of the page.
        * Footer `<footer>`

### Developer Tools

You can use what works for you, Chrome has built in developer tools as does Firefox, Safari and Internet Explorer. You can also download Firebug for Firefox.

- Developer tools allow you to:
    + See the HTML of a page
    + Edit and rearrange the HTML elements
    + Examine the box model of an element (we'll talk more about box model in next Saturday's class)
    + Edit the CSS
    + And more, all without damaging anything.
- <a href="http://www.html5rocks.com/en/tutorials/developertools/part1/" title="Introduction to Chrome Developer Tools, Part 1">Introduction to Chrome Developer Tools, Part 1</a>

### Accessibility

You all heard me talk about accessibility several times. Now is the time to get in the habit of building your sites with all your users in mind. Remember, the more people that can consume your content, the better. <a href="http://a11yproject.com/" title="The Accessibility Project">The Accessibility Project</a> is a great place to start.