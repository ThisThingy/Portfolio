import React from 'react';

const Education = () => {
  const education = [
    { year: "2020-24", degree: "High School Diploma", 
        institution: "Saint Patrick Catholic Secondary School" }
  ];

  return (
    <div className="page education">
      <h1>Education</h1>
      <ul>
        {education.map((edu, i) => (
          <li key={i}>
            <strong>{edu.year}</strong> - {edu.degree}, {edu.institution}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Education;
