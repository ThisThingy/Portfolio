import React from 'react';

const services = [
  {
    title: "Game Programming",
    description: "Design and develop engaging, interactive games using Unity, Unreal Engine, and custom game mechanics.",
    icon: "src/assets/game-dev.png", // placeholder for an icon or image
  },
  {
    title: "Web Development",
    description: "Create responsive and functional web applications using modern web technologies like React, Node.js, and more.",
    icon: "src/assets/web-dev.png",
  },
  {
    title: "Art & Design",
    description: "Produce original digital and traditional artwork for games, illustrations, and visual storytelling.",
    icon: "src/assets/art.jpg",
  },
];

const Services = () => {
  return (
    <div className="content services">
      <h1>Services I Offer</h1>
      <p>
        Combining technical expertise and creativity, I provide a range of services for interactive projects, web applications, and visual arts.
      </p>

      <div className="service-cards">
        {services.map((service, index) => (
          <div key={index} className="service-card">
            <img src={service.icon} alt={service.title} />
            <h2>{service.title}</h2>
            <p>{service.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Services;
