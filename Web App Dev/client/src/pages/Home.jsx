import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

const slides = [
  { image: '/src/assets/about.png', alt: 'About Me', link: '/about' },
  { image: '/src/assets/project.jpg', alt: 'Projects', link: '/projects' },
  { image: '/src/assets/services.jpg', alt: 'Services', link: '/services' },
  { image: '/src/assets/contact.png', alt: 'Contact', link: '/contact' },
];

const Home = () => {
  const [current, setCurrent] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrent((prev) => (prev + 1) % slides.length);
    }, 4000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="content home">
      <h1>Welcome to My Game Programming Portfolio</h1>
      <p>
        Hello! I’m Isaiah Rabanillo, a Game Programmer passionate about building immersive 
        and interactive experiences. 
        
      </p>

      <div className="carousel">
  {slides.map((slide, index) => {
    let position = 'nextSlide';

    if (index === current) {
      position = 'activeSlide';
    } else if (
      index === (current - 1 + slides.length) % slides.length
    ) {
      position = 'prevSlide';
    } else if (
      index === (current + 1) % slides.length
    ) {
      position = 'nextSlide';
    } else {
      position = 'hiddenSlide'; // optional: for slides not immediately next/prev
    }

    return (
      <Link
        key={index}
        to={slide.link}
        className={`slide ${position}`}
      >
        <img src={slide.image} alt={slide.alt} />
      </Link>
    );
  })}
</div>

    </div>
  );
};

export default Home;
