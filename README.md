# Great Minds

## Project Overview

The goal of this project is to create a comprehensive, interactive web-based encyclopedia dedicated to 
history's greatest minds. The application aggregates biographies, masterpieces, quotes, and historical influences 
between notable figures spanning across arts, music, and science 
(e.g., Leonardo da Vinci, Johann Sebastian Bach, Nikola Tesla, Thomas Edison, Henry Ford).

The solution is designed to handle complex relationships between historical eras, individuals, and their works. 
Beyond standard biographies, the platform introduces an interactive "Fun Facts" section, highlighting curious, 
lesser-known, and sometimes humorous real-life events from the lives of these great minds. 
This adds an engaging and humanizing layer to the historical data, making history accessible and entertaining.

## Contents

**Setup Tutorials**
- [Project Setup](docs/project_setup.md)

**Key Parts**
  - Models
  - Views & Forms
  - Templates & UI

**Key Components**
  - Data Architecture & Relationships
  - Custom Template Tags
  - Form Validation & User Experience
- Justification of Design Decisions
- Future Roadmap

---

## Key Components

### Data Architecture & Relationships

We have distinct models to represent the historical context and the figures:
- **`Era` & `Category`**: Provide a taxonomic structure (e.g., Renaissance, Baroque, Industrial Revolution, Painting, Music, Science).
- **`Person`**: The core model representing a historical figure, linked to an `Era` via a ForeignKey. It also includes a `fun_fact` field to store engaging, lesser-known trivia.
- **`Work`**: Represents a masterpiece or invention, linked to a `Person` via ForeignKey and to a `Category` via a ManyToManyField.
- **`Influence`**: A self-referential model (two ForeignKeys to `Person`) that maps the graph of who influenced whom. This allows us to visualize the lineage of ideas (e.g., Nikola Tesla influencing modern engineering, or Bach influencing Mozart).
- **`Quote`**: Keeps the most famous sayings of the figures, linked via ForeignKey.

### Custom Template Tags & Filters

To keep the logic out of the templates (following the "Fat Models, Thin Templates" principle), custom template tags and filters were implemented.
- A custom filter is used to dynamically format the lifespan of a person (e.g., "1452 – 1519").
- Inclusion tags are used to render reusable UI components (like a "Person Card") across different pages, ensuring DRY (Don't Repeat Yourself) principles in the frontend.

### Form Validation & User Experience

- **Custom Validation**: Forms (like `PersonForm`) implement custom `clean_*` methods to ensure data integrity (e.g., a person cannot die before they are born, or birth years cannot be set in the future).
- **UI/UX**: Forms and the overall layout are styled using **Tailwind CSS**. The design follows a mobile-first approach, utilizing utility classes for a clean, modern, and highly customizable interface. A confirmation step is mandatory before any deletion (via a dedicated `DeleteView` template), preventing accidental data loss.

---

## Justification of Design Decisions

### Modular Architecture
The project is divided into three distinct Django apps (`core`, `encyclopedia`, `gallery`). This approach ensures the **Separation of Concerns** principle. 
- `core` handles global site logic (home, 404).
- `encyclopedia` handles people, eras, and history.
- `gallery` handles artworks, inventions, and masterpieces.

### Use of Many-to-Many and ForeignKey Relationships
Instead of duplicating data, we utilized Django's ORM capabilities:
- `ForeignKey` is used where the relationship is strictly hierarchical (One Era has Many People).
- `ManyToManyField` is used where the relationship is complex (One Work can belong to multiple Categories).

### Inheritance and Abstraction in Views
The project heavily utilizes Django's Class-Based Views (CBVs). 
- Generic views (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`) were inherited and customized. This demonstrates strong OOP principles, reduces boilerplate code, and ensures a consistent CRUD experience across the application.

### Custom 404 Handling
A custom `404.html` template is implemented at the root level. This ensures that even when a user navigates to a non-existent page, they are presented with a branded, user-friendly interface that matches the rest of the application.

---

## Future Roadmap (Post-Exam Enhancements)

While the core functionality focuses on the Django Basics requirements, the platform is designed with scalability and community engagement in mind. Future updates will include:

- **User Authentication & Contributions:** Allowing registered users to suggest new historical figures or submit missing facts for review.
- **Interactive Media:** Integrating short-form video content (e.g., YouTube Shorts) directly into the person's profile.
- **Historical News Feed:** A dynamic section for recent discoveries or historical anniversaries.
- **Community Engagement:** A voting system for "Person of the Month".
- **Events & Performances Integration:** A dedicated section linking historical figures to real-world, upcoming events. For example, users could see upcoming concerts featuring the works of Bach or Mozart in their city, bridging the gap between historical legacy and modern cultural life.
- **Personal Media Galleries:** Extending the Person model to support a gallery of multiple images for each historical figure, allowing users to explore their life and works visually.