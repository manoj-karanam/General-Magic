import React, { useState } from 'react';
import axios from 'axios'; 
import { useNavigate } from 'react-router-dom';
import '../Css/SignUp.css'; 
import { Link } from 'react-router-dom';

const Signup = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    fullname: '',
    email: '',
    password: '',
    confirmPassword: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      navigate('/');
      // const response = await axios.post('http://127.0.0.1:8000/api/register/', {
      //   fullname: formData.fullname,
      //   email: formData.email,
      //   password: formData.password,
      //   confirmpassword: formData.confirmPassword
      // });
      
      // // Assuming the response contains a message indicating successful registration
      // if (response.data.message === 'User registered successfully') {
      //   // Navigate to the login page after successful registration
      //   navigate('/login');
      // } else {
      //   // Handle registration failure
      //   alert('Registration failed, please try again!');
      // }
    } catch (error) {
      console.error('Error signing up:', error);
      alert('An error occurred while signing up, please try again.');
    }
  };

  return (
    <div>
      <header className='header-nav'>
        <h1>General Magic</h1>
      </header>
      <nav className="signup-nav">
        <ul>
          <li><Link to="/">Login</Link></li>
          <li><Link to="/signup">Sign Up</Link></li>
        </ul>
      </nav>
      <div className="signup-container">
        <h2>Sign Up</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="fullname">Full Name</label>
            <input
              type="text"
              id="fullname"
              name="fullname"
              value={formData.fullname}
              onChange={handleChange}
              required
              className='signup-name'
            />
          </div>
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
              className='signup-email'
            />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              required
              className='signup-pwd'
            />
          </div>
          <div className="form-group">
            <label htmlFor="confirm-password">Confirm Password</label>
            <input
              type="password"
              id="confirm-password"
              name="confirmPassword"
              value={formData.confirmPassword}
              onChange={handleChange}
              required
              className='signup-pwd'
            />
          </div>
          <button type="submit" className='signup-button'>Sign Up</button>
        </form>
      </div>
    </div>
  );
};

export default Signup;
