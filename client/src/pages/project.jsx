import React from 'react';

const Projects = () => {
  // Array of project objects with title, image, description, role, and link
  const projects = [
    {
      title: "Project One",
      img: "/src/assets/project1.png",
      description: "A short game coded for Grade 11 final. Built using CS Academy, utilizing Python",
      role: "My role: Main Developer.",
      link: "https://github.com/ThisThingy/project-one" // external link or GitHub
    },
    {
      title: "Project Two",
      img: "src/assets/project2.png",
      description: "A short description of Project Two.",
      role: "My role: frontend developer.",
      link: "https://github.com/ThisThingy/project-two"
    },
    {
      title: "Project Three",
      img: "/assets/project3.jpg",
      description: "A short description of Project Three.",
      role: "My role: full stack developer.",
      link: "https://github.com/yourusername/project-three"
    }
  ];

  return (
    <div className="content projects">
      {/* Page heading */}
      <h1>Projects</h1>

      {/* Grid container for project cards */}
      <div className="projects-grid">
        {projects.map((p, i) => (
          <a 
            key={i} 
            href={p.link} 
            target="_blank" 
            rel="noopener noreferrer"
            style={{ textDecoration: 'none', color: 'inherit' }}
          >
            <div className="project-card" style={{ animationDelay: `${i * 0.2}s` }}>
              {/* Project image */}
              <img src={p.img} alt={p.title} />
              {/* Project title */}
              <h2>{p.title}</h2>
              {/* Project description */}
              <p>{p.description}</p>
              {/* Role in project */}
              <p><strong>{p.role}</strong></p>
            </div>
          </a>
        ))}
      </div>
    </div>
  );
};

export default Projects;
