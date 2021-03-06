from bs4 import BeautifulSoup
import requests

source=requests.get("http://coreyms.com").text

soup=BeautifulSoup(source,'lxml')

article=soup.find('article')
print(article.prettify())
'''
<article class="post-1642 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-development-environment tag-visual-studio-code tag-visual-studios tag-vs-code tag-vscode entry" itemscope="" itemtype="https://schema.org/CreativeWork">
 <header class="entry-header">
  <h2 class="entry-title" itemprop="headline">
   <a class="entry-title-link" href="https://coreyms.com/development/python/visual-studio-code-windows-setting-up-a-python-development-environment-and-complete-overview" rel="bookmark">
    Visual Studio Code (Windows) – Setting up a Python Development Environment and Complete Overview
   </a>
  </h2>
  <p class="entry-meta">
   <time class="entry-time" datetime="2019-05-01T14:03:24+00:00" itemprop="datePublished">
    May 1, 2019
   </time>
   by
   <span class="entry-author" itemprop="author" itemscope="" itemtype="https://schema.org/Person">
    <a class="entry-author-link" href="https://coreyms.com/author/coreymschafer" itemprop="url" rel="author">
     <span class="entry-author-name" itemprop="name">
      Corey Schafer
     </span>
    </a>
   </span>
   <span class="entry-comments-link">
    <a href="https://coreyms.com/development/python/visual-studio-code-windows-setting-up-a-python-development-environment-and-complete-overview#respond">
     <span class="dsq-postid" data-dsqidentifier="1642 http://coreyms.com/?p=1642">
      Leave a Comment
     </span>
    </a>
   </span>
  </p>
 </header>
 <div class="entry-content" itemprop="text">
  <p>
   In this Python Programming Tutorial, we will be learning how to set up a Python development environment in VSCode on Windows. VSCode is a very nice free editor for writing Python applications and many developers are now switching over to this editor. In this video, we will learn how to install VSCode, get the Python extension installed, how to change Python interpreters, create virtual environments, format/lint our code, how to use Git within VSCode, how to debug our programs, how unit testing works, and more. We have a lot to cover, so let’s go ahead and get started…
  </p>
  <p>
   VSCode on MacOS – https://youtu.be/06I63_p-2A4
  </p>
  <p>
   Timestamps for topics in this tutorial:
   <br/>
   Installation – 1:13
   <br/>
   Python Extension – 5:48
   <br/>
   Switching Interpreters – 10:04
   <br/>
   Changing Color Themes – 12:35
   <br/>
   VSCode Settings – 16:16
   <br/>
   Set Default Python – 21:33
   <br/>
   Using Virtual Environments – 25:10
   <br/>
   IntelliSense – 29:45
   <br/>
   Code Formatting – 32:13
   <br/>
   Code Linting – 37:06
   <br/>
   Code Runner Extension – 39:42
   <br/>
   Git Integration – 47:44
   <br/>
   Use Different Terminal – 51:07
   <br/>
   Debugging – 58:45
   <br/>
   Unit Testing – 1:03:25
   <br/>
   Zen Mode – 1:09:55
  </p>
  <figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio">
   <div class="wp-block-embed__wrapper">
    <span class="embed-youtube" style="text-align:center; display: block;">
     <iframe allowfullscreen="true" class="youtube-player" height="360" src="https://www.youtube.com/embed/-nh9rCzPJ20?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640">
     </iframe>
    </span>
   </div>
  </figure>
 </div>
 <footer class="entry-footer">
  <p class="entry-meta">
   <span class="entry-categories">
    Filed Under:
    <a href="https://coreyms.com/category/development" rel="category tag">
     Development
    </a>
    ,
    <a href="https://coreyms.com/category/development/python" rel="category tag">
     Python
    </a>
   </span>
   <span class="entry-tags">
    Tagged With:
    <a href="https://coreyms.com/tag/development-environment" rel="tag">
     Development Environment
    </a>
    ,
    <a href="https://coreyms.com/tag/visual-studio-code" rel="tag">
     visual studio code
    </a>
    ,
    <a href="https://coreyms.com/tag/visual-studios" rel="tag">
     visual studios
    </a>
    ,
    <a href="https://coreyms.com/tag/vs-code" rel="tag">
     vs code
    </a>
    ,
    <a href="https://coreyms.com/tag/vscode" rel="tag">
     vscode
    </a>
   </span>
  </p>
 </footer>
</article>
'''