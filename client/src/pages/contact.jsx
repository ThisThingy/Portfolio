import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Contact = () => {
  const navigate = useNavigate();

  // State to capture form input values
  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    email: "",
    phone: "",
    message: ""
  });

  // Update state when input changes
  const handleChange = (e) => {
    setFormData({...formData, [e.target.name]: e.target.value});
  };

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData); // Capture form data
    alert("Message submitted!");
    navigate("/"); // Redirect to Home
  };

  return (
    <div className="content contact">
      {/* Page heading */}
      <h1>Contact Me</h1>

      {/* Contact form */}
      <form onSubmit={handleSubmit}>
        <input name="firstName" placeholder="First Name" onChange={handleChange} required />
        <input name="lastName" placeholder="Last Name" onChange={handleChange} required />
        <input name="email" type="email" placeholder="Email" onChange={handleChange} required />
        <input name="phone" placeholder="Contact Number" onChange={handleChange} />
        <textarea name="message" placeholder="Your Message" onChange={handleChange} required />
        <button type="submit">Send Message</button>
      </form>
    </div>
  );
};

export default Contact;
