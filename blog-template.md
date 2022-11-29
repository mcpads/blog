---
title: title
date: 2022-11-20 12:00:00 +0900
author: mcpads
categories: [Computer, Language, OCaml]
tags: [ocaml, programming language]
# math: true
# toc: true
# comments: true
# mermaid: true
# img_path: /img/path/
# image:
#   path: /path/to/image/file
#   width: 1000   # in pixels
#   height: 400   # in pixels
#   alt: image alternative text
# pin: true
# layout: post
---

This is a demo of all styled elements in Jekyll Now.

[View the markdown used to create this post](https://raw.githubusercontent.com/barryclark/www.jekyllnow.com/gh-pages/_posts/2014-6-19-Markdown-Style-Guide.md).

This is a paragraph, it's surrounded by whitespace. Next up are some headers, they're heavily influenced by GitHub's markdown style.

## Header 2 (H1 is reserved for post titles) ##

### Header 3

#### Header 4

A link to [Jekyll Now](http://github.com/barryclark/jekyll-now/). A big ass literal link <http://github.com/barryclark/jekyll-now/>

An image, located within /images

![an image alt text]({{ site.baseurl }}/images/jekyll-logo.png "an image title")
![Desktop View](/assets/img/sample/mockup.png){: w="700" h="400" }
![Desktop View](/assets/img/sample/mockup.png){: .normal }
![Desktop View](/assets/img/sample/mockup.png){: .left }

![Desktop View](/assets/img/sample/mockup.png){: .shadow }

* A bulletted list

- alternative syntax 1

+ alternative syntax 2
  * an indented list item

1. An
2. ordered
3. list

Inline markup styles:

* _italics_
* **bold**
* `code()`

> Blockquote
>> Nested Blockquote

Use two trailing spaces
on the right
to create linebreak tags

Finally, horizontal lines

----
****

> Example line for prompt.
{: .prompt-info }
> Example line for prompt.
{: .prompt-tip }
> Example line for prompt.
{: .prompt-warning }
> Example line for prompt.
{: .prompt-danger }

`/path/to/a/file.extend`{: .filepath}

```shell
echo 'No more line numbers!'
```

{: .nolineno }

```shell
# content
```

{: file="path/to/file" }

{% raw %}

```liquid
{% if product.title contains 'Pack' %}
  This product's title contains the word Pack.
{% endif %}
```

{% endraw %}
