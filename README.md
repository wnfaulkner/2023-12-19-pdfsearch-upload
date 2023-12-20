# PDF Search

Author: [William Faulkner](https://github.com/wnfaulkner)

---
## **Project Idea and Description**

PDF Search helps users store, organize, and search pdf documents.

---
## **Technology Stack**

Database: SQLite3 (Django default)

Back-End: Django, Django REST Framework (DRF)

Front-End: React

---
## **User Stories**

### MVP
- AAU, I want to be able to import PDFs files.
- AAU, I want the ability to view a list of all of my uploaded PDFs.
- AAU, I want the ability to open/read/view individual PDFs.

### Future Goals
- AAU, I want the ability to sign-up and create a new profile.
- AAU, I want the ability to log-in with an email and password.
- AAU, I want the ability to log-out.
- AAU, I want to be able to import PDFs and have my uploaded PDFs be associated with my user such that other users cannot access them.
- AAU, I want the ability to search the full text content and metadata of my PDFs simultaneously.
- AAU, I want the ability to batch import PDFs.
- AAU, I want to be able to create, view, edit, and delete tags (including metadata tags like 'author').
- AAU, I want the ability to associate tags with documents.
- AAU, I want the ability to filter my list of PDFs to those associated with a particular tag.
- AAU, I want the ability to search both full and filtered lists of my PDFs for exact text matches in both PDF metadata and text content.
- AAU, I want the ability to nest my tags within a hierarchy with ‘parent’ and ‘child’ tags.
- AAU, I want the ability to tag selected text within documents.
- AAU, I want the search results prioritized, with higher priority going to documents where the search term appears in the metadata and documents where the search term appears more frequently in the document text.
- AAU, I want my search results to include a ‘search snippet,’ i.e. preview(s) of the text surrounding the search term within the doc.
- AAU, I want my search results to live update with each new character typed into the search query.
- AAU, I want results to appear snappily (< 0.25 sec) even when I am searching 500+ PDFs.

---
## **ERD**

<img src="./pdfsearch/public/images/ERD.png" alt="ERD" width="350"/>

---
## **Routing Chart**

<img src="./pdfsearch/public/images/RESTful Routing Chart.png" alt="RESTful Routing Chart" width="700"/>

---
## **Wireframes**

![Landing Page Wireframe](./pdfsearch/public/images/wireframes/Slide1.PNG)

![User Home Wireframe](./pdfsearch/public/images/wireframes/Slide2.PNG)

![Import/Index Wireframe](./pdfsearch/public/images/wireframes/Slide3.PNG)

![Search Wireframe (no query)](./pdfsearch/public/images/wireframes/Slide4.PNG)

![Search Wireframe (with query)](./pdfsearch/public/images/wireframes/Slide5.PNG)


---
## **Approach, Process, & Hurdles**

At my current level of coding skills, implementing a new technology on my own is possible, but difficult enough that the pace of developing any given functionality feels truly glacial. I first attempted to follow tutorials to set up the React-DRF-Django stack and ensure that I could send user input (just text to start with) from the interface to the database. Having succeeded at that, I attempted to follow tutorials to set up file upload, but the minor differences between the tutorials and my setup were enough that I could not make it work. I started an entirely new repo and followed one of the upload tutorials exactly, which got me to file upload functionality. I was then able to implement viewing pdfs in the repo. 

With only one day of project work time left, I decided to attempt adding functionality to extract the text from a pdf and store the extracted text in the database. For this step, I could find no tutorials that covered even a significant piece of the setup process.

Hurdles:
- Documentation for many languages/packages is often still only partially readable/accessible at my current level of understanding. And missing 25% of the meaning/vocab can mean that you get 0% of the learning you would need to successfully implement.
- Tutorials:
  - Seem to often have crucial points of ambiguity, especially when written (less in video). 
  - Focus almost exclusively on the 'what/how' and rarely if ever on the 'why'.
- Overall, well-written coding instruction that focuses on providing accessible, conceptual-level understanding seems a rare beast indeed.  
